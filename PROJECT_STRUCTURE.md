# 项目结构说明 (Project Structure)

本项目采用标准的 Python `src` 布局，专注于数据定义与处理。

## 目录树

```text
.
├── .github/                # GitHub Actions CI/CD 配置
├── .venv/                  # Python 虚拟环境 (由 uv 管理)
├── src/
│   └── neuro_sama/         # 核心源码包
│       ├── models/         # 数据模型定义 (Pydantic)
│       │   ├── __init__.py
│       │   ├── dialogue.py # 对话模型
│       │   └── stream.py   # 直播流模型
│       └── __init__.py
├── test/                   # 测试代码目录
│   └── test_models.py      # 模型验证测试
├── pyproject.toml          # 项目依赖与元数据配置
├── uv.lock                 # 依赖锁定文件
├── Dockerfile              # 容器构建文件 (用于环境一致性)
└── README.md               # 项目主文档
```

## 关键模块说明

### `src/neuro_sama/models/`

存放核心数据结构定义，使用 Pydantic `BaseModel` 实现。

- **`stream.py`**: 定义直播场次信息，如 `stream_id`, `title`, `start_time`。
- **`dialogue.py`**: 定义单次对话交互，如 `question`, `answer`, `confidence`。

这些模型不依赖数据库，仅用于内存中的数据校验和类型提示。
