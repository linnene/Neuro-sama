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
        role="question",
        content="Hello?",
        speaker="User",
        timestamp=datetime.now()
    )
    assert msg.role == "question"
    assert msg.content == "Hello?"

def test_qapair_model():
    q = Message(role="question", content="Hi", speaker="A")
    a = Message(role="answer", content="Hello", speaker="B")
    
    pair = QAPair(question=q, answer=a)
    assert pair.question.content == "Hi"
    assert pair.answer.content == "Hello"

def test_qapair_validation():
    q = Message(role="question", content="Hi", speaker="A")
    a = Message(role="answer", content="Hello", speaker="B")
    
    # Test valid pair
    pair = QAPair.validate_pair(q, a)
    assert pair is not None
    
    # Test invalid roles
    try:
        QAPair.validate_pair(a, q) # Wrong order
        assert False, "Should raise ValueError"
    except ValueError:
        pass

