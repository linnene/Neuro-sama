# 测试指南 (Testing Guide)

本项目使用 `pytest` 进行单元测试，主要针对数据模型的定义和校验逻辑。

## 运行测试

确保你已经安装了依赖：

```bash
uv sync
```

运行所有测试：

```bash
uv run pytest
```

## 测试文件说明

### `test/test_models.py`

该文件测试 `Stream` 和 `Dialogue` 模型的实例化和字段验证。

**示例代码**:

```python
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
```

## 编写新测试

1. 在 `test/` 目录下创建以 `test_` 开头的 Python 文件。
2. 导入需要测试的模型或函数。
3. 编写以 `test_` 开头的函数进行断言。
