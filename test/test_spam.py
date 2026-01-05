import pytest
from pathlib import Path
from datetime import datetime


from neuro_sama.parser.screen_spam import (
    read_jsonl_file,
    build_repeat_segments_Iterator,
    normalize_content,
    parse_timestamp
)
from neuro_sama.models.dialogue import BaseMes




def test_read_jsonl_file(tmp_path: Path):
    test_file = tmp_path / "test.jsonl"
    test_data = [
        '{"content": "Hello", "speaker": "User", "timestamp": "2024-01-01T12:00:00Z"}\n',
        '{"content": "World", "speaker": "Bot", "timestamp": "2024-01-01T12:01:00Z"}\n',
        '#META# This is a meta line\n',
        '{"content": "!", "speaker": "User", "timestamp": "invalid-timestamp"}\n'
    ]
    test_file.write_text(''.join(test_data), encoding='utf-8')

    messages = list(read_jsonl_file(str(test_file)))
    assert len(messages) == 2
    assert messages[0].content == "Hello"
    assert messages[0].speaker == "User"
    assert messages[1].content == "World"
    assert messages[1].speaker == "Bot"

def test_build_repeat_segments():
    from datetime import datetime, timezone
    messages = [
        BaseMes(content="Spam message", speaker="User", timestamp=datetime(1, 1, 12, 0, tzinfo=timezone.utc)),
        BaseMes(content="Spam message", speaker="User", timestamp=datetime(1, 1, 12, 1, tzinfo=timezone.utc)),
        BaseMes(content="Spam message", speaker="User", timestamp=datetime(1, 1, 12, 2, tzinfo=timezone.utc)),
        BaseMes(content="Different message", speaker="User", timestamp=datetime(1, 1, 12, 3, tzinfo=timezone.utc)),
        BaseMes(content="Spam message", speaker="User", timestamp=datetime(1, 1, 12, 4, tzinfo=timezone.utc)),
        BaseMes(content="Spam message", speaker="User", timestamp=datetime(1, 1, 12, 5, tzinfo=timezone.utc)),
        BaseMes(content="Spam message", speaker="User", timestamp=datetime(1, 1, 12, 6, tzinfo=timezone.utc)),
        BaseMes(content="Spam message", speaker="User", timestamp=None),  # This should be skipped
    ]
    segments = build_repeat_segments_Iterator(iter(messages))
    assert len(segments) == 2
    assert segments[0].content == "Spammessage"
    assert segments[0].count == 3
    assert segments[1].content == "Spammessage"
    assert segments[1].count == 3

def test_normalize_content():
    assert normalize_content(" Hello World! ") == "HelloWorld"
    assert normalize_content("\nSpam Message!!!") == "SpamMessage"
    assert normalize_content("NoSpecialChars") == "NoSpecialChars"


def test_parse_timestamp_iso_format():
    ts = parse_timestamp("2025-12-22T12:26:24.386275+08:00")

    assert isinstance(ts, datetime)
    assert ts.year == 2025
    assert ts.month == 12
    assert ts.day == 22
    assert ts.hour == 12
    assert ts.minute == 26
    assert ts.second == 24
    assert ts.tzinfo is not None