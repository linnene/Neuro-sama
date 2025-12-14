# 项目结构说明 (Project Structure)

本项目采用标准的 Python `src` 布局，所有数据通过文件同步方式管理，不再包含后端 API 服务和数据库。

## 目录树

```text
.
├── .github/                # GitHub Actions CI/CD 配置
├── .venv/                  # Python 虚拟环境 (由 uv 管理)
├── src/
│   └── neuro_sama/         # 核心源码包
│       ├── models/         # 数据模型
│       └── __init__.py
├── test/                   # 测试代码目录
├── pyproject.toml          # 项目依赖与元数据配置
├── uv.lock                 # 依赖锁定文件
└── README.md               # 项目主文档
```

## 关键模块说明

### 1. `src/neuro_sama/models/`

存放数据结构定义，支持多直播间数据隔离。
