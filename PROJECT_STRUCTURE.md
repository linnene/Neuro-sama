# 项目结构说明 (Project Structure)

本项目采用标准的 Python `src` 布局，结合 FastAPI 和 SQLModel 构建。

## 目录树

```text
.
├── .github/                # GitHub Actions CI/CD 配置
├── .venv/                  # Python 虚拟环境 (由 uv 管理)
├── src/
│   └── neuro_sama/         # 核心源码包
│       ├── api/            # API 接口层
│       │   └── routes/     # 路由定义 (Endpoints)
│       ├── core/           # 核心基础设施
│       │   └── database.py # 数据库连接与 Session 管理
│       ├── models/         # 数据模型 (SQLModel)
│       │   └── dialogue.py # 对话数据表定义
│       ├── main.py         # FastAPI 应用工厂与配置
│       └── __init__.py
├── test/                   # 测试代码目录
├── Dockerfile              # 容器构建文件
├── main.py                 # 项目启动入口
├── pyproject.toml          # 项目依赖与元数据配置
├── uv.lock                 # 依赖锁定文件
└── README.md               # 项目主文档
```

## 关键模块说明

### 1. `src/neuro_sama/models/`

存放数据库模型定义。目前包含 `Dialogue` 模型，用于存储 VTB 对话特征数据。

### 2. `src/neuro_sama/core/`

存放项目的基础设施代码，如数据库引擎 (`engine`) 和依赖注入用的 `get_session` 函数。

### 3. `src/neuro_sama/api/`

存放 FastAPI 的路由逻辑。`routes/dialogue.py` 定义了对话数据的增删改查接口。

### 4. `src/neuro_sama/main.py`

FastAPI 应用的初始化位置，负责组装路由、中间件和事件处理（如启动时创建数据库表）。

### 5. `main.py` (根目录)

生产环境或开发环境的启动脚本，调用 `uvicorn` 运行应用。
