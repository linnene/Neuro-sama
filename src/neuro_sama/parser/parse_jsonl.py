import json
import logging
from pathlib import Path
from typing import Iterator, Type, TypeVar, Union
from datetime import datetime
from pydantic import BaseModel, ValidationError

from neuro_sama.models.dialogue import BaseMes


T = TypeVar("T", bound=BaseModel)

logger = logging.getLogger(__name__)

def parse_jsonl_file(
    file_path: Union[str, Path],
    model_class: Type[T],
) -> list[T]:
    messages: list[T] = []

    for raw in parse_jsonl(file_path):
        try:
            data = {
                "content": raw.get("content", ""),
                "speaker": raw.get("speaker", ""),
                "timestamp": _parse_timestamp(raw.get("data_ct")),
            }
            messages.append(model_class(**data))
        except ValidationError as e:
            logger.warning(
                "消息校验失败，已跳过：%s",
                e,
            )

    return messages

def parse_jsonl(file_path: Union[str, Path]) -> Iterator[dict]:
    file_path = Path(file_path)

    with file_path.open("r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            # 跳过 META 行
            #TODO: 未来可考虑解析 META 行为 MetaEvent 对象
            if line.startswith("#META#"):
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as e:
                logger.warning(
                    "第 %d 行 JSON 解析失败，已跳过：%s",
                    lineno,
                    e,
                )


def _parse_timestamp(value: str|None = None) -> Union[datetime, None]:
    """
    _parse_timestamp:
    处理时间元数据
    
    :param value: 说明
    :type value: str | None
    :return: 说明
    :rtype: datetime | None
    """
    if not value:
        return None

    try:
        # 如果 data_ct 是类似 12181034 这种字符串
        return datetime.strptime(value, "%m%d%H%M")
    except ValueError:
        return None


def save_as_jsonl(messages: list[BaseMes], output_path: Union[str, Path]):
    """
    save_as_jsonl:
    将消息列表保存为标准可处理的 JSONL 文件，
    自动在文件名上追加 _pend 后缀
    """
    output_path = Path(output_path)

    # 确保父目录存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 生成带 _pend 的文件名
    target_path = output_path.with_name(
        f"{output_path.stem}_pend{output_path.suffix}"
    )

    with target_path.open("w", encoding="utf-8") as f:
        for msg in messages:
            f.write(msg.model_dump_json(ensure_ascii=False))
            f.write("\n")
