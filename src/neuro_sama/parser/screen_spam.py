"""
neuro_sama.parser.screen_spam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module for screen spam parsing functionalities.
Provides tools to parse and handle screen spam data.
"""
import re
import json
import logging
from datetime import datetime
from typing import Iterator, Optional, List

from neuro_sama.models.dialogue import BaseMes, RepeatSegment

logger = logging.getLogger(__name__)

#read jsonl file and yield BaseMes objects
def read_jsonl_file(file_path: str) -> Iterator[BaseMes]:
    with open(file_path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#META#"):
                continue
            try:
                raw = json.loads(line)
                timestamp = parse_timestamp(raw.get("timestamp"))
                if timestamp is None:
                    continue
                yield BaseMes(
                    content=raw.get("content", ""),
                    speaker=raw.get("speaker", ""),
                    timestamp=timestamp
                )
            except Exception as e:
                logger.warning("第 %d 行解析失败：%s", lineno, e)


# 根据消息列表构建重复数据段
def build_repeat_segments(
    messages: Iterator[BaseMes],
) -> List[RepeatSegment]:
    segments: List[RepeatSegment] = []

    current_content: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    count = 0

    for msg in messages:
        if msg.timestamp is None:
            logger.warning("跳过没有时间的消息：%s", msg.content)
            continue
        if current_content is None:
            current_content = normalize_content(msg.content)
            # current_content = msg.content
            start_time = msg.timestamp
            end_time = msg.timestamp
            count = 1
            continue

        if normalize_content(msg.content) == current_content:
            count += 1
            end_time = msg.timestamp
        else:
            if count >= 4 and start_time and end_time :
                segments.append(
                    RepeatSegment(
                        content=current_content,
                        start_time=start_time,
                        end_time=end_time,
                        count=count,
                    )
                )
            current_content = normalize_content(msg.content)
            start_time = msg.timestamp
            end_time = msg.timestamp
            count = 1
            
    return segments

# 解析时间字符串为 datetime 对象
def parse_timestamp(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value)
    except ValueError as e:
        logger.warning("时间解析失败：%s", e)
        return None

# 规范化消息内容，去除多余空白，标点符号等
def normalize_content(content: str) -> str:
    """
    修复版：去除空格和所有标点符号
    """
    if not content:
        return ""
    
    pattern = r'[^\w]'  # \w 匹配字母、数字、下划线
    
    cleaned_text = re.sub(pattern, '', content)
    
    return cleaned_text