# 测试指南 (Testing Guide)

本项目当前仅保留基础单元测试（如数据结构相关），不再包含后端 API 或数据库相关测试。

## 运行测试

确保你已经安装了依赖：

```bash
uv sync
```

运行所有测试：

```bash
uv run pytest
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
