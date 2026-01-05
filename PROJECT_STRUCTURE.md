# 项目结构说明 (Project Structure)

本项目采用标准的 Python `src` 布局，专注于数据定义与处理。

## 目录树

```text
.
├── .venv/                  # Python 虚拟环境 (由 uv 管理)
├── config.py               # 项目配置文件
├── data/                   # 数据存储目录
│   ├── cleaned/            # 清洗后的数据
│   ├── events/             # 事件数据 (如 alignment, spam)
│   └── raw/                # 原始数据
│       ├── audio/          # 音频数据
│       └── danmaku/        # 弹幕数据 (JSONL)
├── DEV_LOG.md              # 开发日志
├── Dockerfile              # 容器构建文件
├── main.py                 # 主程序入口
├── PROJECT_STRUCTURE.md    # 项目结构说明
├── pyproject.toml          # 项目依赖与元数据配置
├── README.md               # 项目主文档
├── ROADMAP.md              # 项目路线图
├── src/
│   └── neuro_sama/         # 核心源码包
│       ├── models/         # 数据模型定义 (Pydantic)
│       │   ├── __init__.py
│       │   ├── dialogue.py # 对话模型
│       │   └── stream.py   # 直播流模型
│       ├── parser/         # 数据解析与处理
│       │   ├── __init__.py
│       │   ├── parse_jsonl.py # JSONL 解析器
│       │   └── screen_spam.py # 垃圾弹幕过滤
│       └── __init__.py
├── test/                   # 测试代码目录
│   ├── test_models.py      # 模型验证测试
│   ├── test_parser.py      # 解析器测试
│   └── test_spam.py        # 垃圾过滤测试
├── TESTING.md              # 测试指南
└── uv.lock                 # 依赖锁定文件
```

## 关键模块说明

### `src/neuro_sama/models/`

存放核心数据结构定义，使用 Pydantic `BaseModel` 实现。

- **`stream.py`**: 定义直播场次信息，如 `stream_id`, `title`, `start_time`。
- **`dialogue.py`**: 定义单次对话交互，如 `question`, `answer`, `confidence`。

这些模型不依赖数据库，仅用于内存中的数据校验和类型提示。

### `src/neuro_sama/parser/`

存放数据解析和处理逻辑。

- **`parse_jsonl.py`**: 处理 JSONL 格式的原始数据文件。
- **`screen_spam.py`**: 实现垃圾弹幕和重复内容的过滤逻辑。

### `data/`

数据存储目录，包含原始数据和处理后的数据。

- **`raw/`**: 存放爬虫获取的原始数据。
- **`cleaned/`**: 存放经过解析和清洗后的数据。
- **`events/`**: 存放特定事件的数据分析结果。
