import pytest
import json
from pathlib import Path
from datetime import datetime
from pydantic import BaseModel

from neuro_sama.parser.parse_jsonl import (
    parse_jsonl,
    parse_jsonl_file,
    save_as_jsonl,
    _parse_timestamp,
)
from neuro_sama.models.dialogue import BaseMes

#错误的 Pydantic 模型，用于测试
class StrictMes(BaseModel):
    content: str
    speaker: str
    timestamp: datetime

    # 故意加一个限制
    @classmethod
    def model_validate(cls, value):
        raise ValueError("boom")

#测试基本的 parse_jsonl 功能
def test_parse_jsonl_basic(tmp_path: Path):
    content = """#META# {"event": "register"}
{"speaker": "chat", "content": "你好", "data_ct": "12181032"}

{"speaker": "chat", "content": "世界"}
INVALID_JSON
"""
    file = tmp_path / "input.jsonl"
    file.write_text(content, encoding="utf-8")

    rows = list(parse_jsonl(file))

    assert len(rows) == 2
    assert rows[0]["content"] == "你好"
    assert rows[1]["content"] == "世界"


def test_parse_timestamp_valid():
    ts = _parse_timestamp("12181032")
    assert isinstance(ts, datetime)
    assert ts.month == 12
    assert ts.day == 18
    assert ts.hour == 10
    assert ts.minute == 32


def test_parse_timestamp_invalid():
    assert _parse_timestamp("not-a-time") is None
    assert _parse_timestamp("") is None
    assert _parse_timestamp(None) is None


def test_parse_jsonl_file_to_model(tmp_path: Path):
    content = """{"speaker": "chat", "content": "测试", "data_ct": "12181032"}"""
    file = tmp_path / "input.jsonl"
    file.write_text(content, encoding="utf-8")

    msgs = parse_jsonl_file(file, BaseMes)

    assert len(msgs) == 1
    msg = msgs[0]
    assert isinstance(msg, BaseMes)
    assert msg.content == "测试"
    assert msg.speaker == "chat"
    assert isinstance(msg.timestamp, datetime)


def test_parse_jsonl_file_validation_error(tmp_path: Path):
    content = """{"speaker": "chat", "content": "坏数据"}"""
    file = tmp_path / "input.jsonl"
    file.write_text(content, encoding="utf-8")

    msgs = parse_jsonl_file(file, StrictMes)

    assert msgs == []


def test_save_as_jsonl(tmp_path: Path):
    msgs = [
        BaseMes(
            speaker="chat",
            content="一",
            timestamp=datetime(2025, 12, 18, 10, 30),
        ),
        BaseMes(
            speaker="chat",
            content="二",
            timestamp=None,
        ),
    ]

    output = tmp_path / "out.jsonl"
    save_as_jsonl(msgs, output)

    pend_output = tmp_path / "out_pend.jsonl"
    assert pend_output.exists()

    lines = pend_output.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2

    data = json.loads(lines[0])
    assert data["content"] == "一"
    assert data["speaker"] == "chat"
