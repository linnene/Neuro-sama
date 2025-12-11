import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from neuro_sama.main import app
from neuro_sama.core.database import get_session

# 使用内存数据库进行测试，避免污染真实数据库
test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

@pytest.fixture(name="session")
def session_fixture():
    # 在每个测试前创建表
    SQLModel.metadata.create_all(test_engine)
    with Session(test_engine) as session:
        yield session
    # 测试后清理
    SQLModel.metadata.drop_all(test_engine)

@pytest.fixture(name="client")
def client_fixture(session: Session):
    # 覆盖依赖，让应用使用我们的测试 Session
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    
    # 使用 TestClient 上下文管理器触发 lifespan 事件
    with TestClient(app) as client:
        yield client
    
    app.dependency_overrides.clear()

def test_backend_health(client: TestClient):
    """测试后端健康检查接口"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Neuro-sama backend is running"}

def test_create_dialogue_api(client: TestClient):
    """测试创建对话接口"""
    payload = {
        "stream_id": "test_stream_001",
        "prompt_speaker": "Viewer",
        "prompt_content": "Hello Neuro!",
        "response_speaker": "Neuro-sama",
        "response_content": "Hello! Nice to meet you.",
        "prompt_meta": {"badges": ["vip"]},
        "response_meta": {"emotion": "happy"}
    }
    response = client.post("/dialogues/", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["prompt_content"] == "Hello Neuro!"
    assert data["response_meta"] == {"emotion": "happy"}
    assert "id" in data

def test_read_dialogues_api(client: TestClient):
    """测试读取对话接口"""
    # 先插入一条数据
    client.post("/dialogues/", json={
        "prompt_speaker": "A", "prompt_content": "Q",
        "response_speaker": "B", "response_content": "A"
    })
    
    response = client.get("/dialogues/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["prompt_content"] == "Q"
