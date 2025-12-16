from datetime import datetime
from neuro_sama.models import Stream, Dialogue

def test_stream_model():
    stream = Stream(
        stream_id="123",
        title="Test Stream",
        streamer="Neuro",
        start_time=datetime.now()
    )
    assert stream.stream_id == "123"
    assert stream.title == "Test Stream"

def test_dialogue_model():
    dialogue = Dialogue(
        dialogue_id="d1",
        stream_id="123",
        question="Hi",
        answer="Hello",
        timestamp=datetime.now()
    )
    assert dialogue.question == "Hi"
    assert dialogue.answer == "Hello"
