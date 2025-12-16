import json
from datetime import datetime
from neuro_sama.models import QAPair
from neuro_sama.parser.parser import parse_jsonl

def test_parse_qapair_jsonl(tmp_path):
    # Create a dummy jsonl file
    data = [
        {
            "question": {
                "role": "question",
                "content": "Hello?",
                "speaker": "User",
                "timestamp": datetime.now().isoformat()
            },
            "answer": {
                "role": "answer",
                "content": "Hi!",
                "speaker": "Neuro",
                "timestamp": datetime.now().isoformat()
            }
        },
        {
            "question": {
                "role": "question",
                "content": "How are you?",
                "speaker": "User"
            },
            "answer": {
                "role": "answer",
                "content": "Good.",
                "speaker": "Neuro"
            }
        }
    ]
    
    file_path = tmp_path / "test.jsonl"
    with open(file_path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")
            
    # Test parsing
    results = list(parse_jsonl(file_path, QAPair))
    assert len(results) == 2
    assert results[0].question.content == "Hello?"
    assert results[1].answer.content == "Good."

def test_parse_invalid_line(tmp_path):
    file_path = tmp_path / "invalid.jsonl"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write('{"question": {"role": "question"}}\n') # Missing fields
        f.write('invalid json\n')
        # Valid line
        valid_item = {
            "question": {"role": "question", "content": "Q", "speaker": "A"},
            "answer": {"role": "answer", "content": "A", "speaker": "B"}
        }
        f.write(json.dumps(valid_item) + "\n")

    results = list(parse_jsonl(file_path, QAPair))
    assert len(results) == 1
    assert results[0].question.content == "Q"

