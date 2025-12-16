import json
import logging
from pathlib import Path
from typing import Iterator, Type, TypeVar, Union

from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)

logger = logging.getLogger(__name__)

def parse_jsonl(file_path: Union[str, Path], model_class: Type[T]) -> Iterator[T]:
    """
    Parses a JSONL file and yields Pydantic model instances.
    
    Args:
        file_path: Path to the JSONL file.
        model_class: The Pydantic model class to validate against.
        
    Yields:
        Instances of the specified model class.
        Skips lines that fail validation or JSON decoding, logging errors instead.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                # Pydantic v2 method to validate from JSON string
                yield model_class.model_validate_json(line)
            except ValidationError as e:
                logger.error(f"Validation error in {path.name} at line {line_num}: {e}")
            except json.JSONDecodeError as e:
                logger.error(f"JSON decode error in {path.name} at line {line_num}: {e}")
