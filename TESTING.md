# 测试指南 (Testing Guide)

本项目使用 `pytest` 作为测试框架。

## 运行测试

确保你已经安装了依赖：

```bash
uv sync
```

运行所有测试：

```bash
uv run pytest
```

或者直接使用 python 运行（如果已激活虚拟环境）：

```bash
python -m pytest
```

## 编写测试

测试文件位于 `test/` 目录下。

### 示例测试 (`test/test_basic.py`)

```python
import unittest
from neuro_sama import hello

class TestNeuroSama(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello from neuro-sama package!")
```

### 数据库测试 (`test/test_database.py`)

包含对真实数据库连接的测试以及使用内存数据库进行的模型 CRUD 测试。

### 添加新测试

1. 在 `test/` 目录下创建以 `test_` 开头的 Python 文件。
2. 导入你要测试的模块。
3. 编写测试类或测试函数。

## API 测试

对于 FastAPI 接口测试，建议使用 `TestClient`。

```python
from fastapi.testclient import TestClient
from neuro_sama.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
```
