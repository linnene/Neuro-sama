from datetime import datetime
from neuro_sama.models import Stream, QAPair, Message

def test_stream_model():
    stream = Stream(
        stream_id="123",
        title="Test Stream",
        streamer="Neuro",
        start_time=datetime.now()
    )
    assert stream.stream_id == "123"
    assert stream.title == "Test Stream"

def test_message_model():
    msg = Message(
        role="que",
        content="Hello?",
        speaker="User",
        timestamp=datetime.now()
    )
    assert msg.role == "que"
    assert msg.content == "Hello?"

def test_qapair_model():
    q = Message(role="que", content="Hi", speaker="A")
    r = Message(role="res", content="Hello", speaker="B")
    
    pair = QAPair(question=q, response=r)
    assert pair.question.content == "Hi"
    assert pair.response.content == "Hello"

def test_qapair_validation():
    q = Message(role="que", content="Hi", speaker="A")
    r = Message(role="res", content="Hello", speaker="B")
    
    # Test valid pair
    pair = QAPair.validate_pair(q, r)
    assert pair is not None
    
    # Test invalid roles
    try:
        QAPair.validate_pair(r, q) # Wrong order
        assert False, "Should raise ValueError"
    except ValueError:
        pass

