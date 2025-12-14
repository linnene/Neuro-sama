# 开发日志 (Development Log)

## 2025-12-14

### 架构调整
- 移除后端 API 服务和数据库，改为通过文件同步（如 scp）进行数据传输。
- 删除 Docker、docker-compose、数据库相关配置和测试。
- 保留多直播间数据隔离的数据结构。

## 2025-12-10

### 初始化与重构

- **项目初始化**: 使用 `uv` 初始化项目结构，配置 `pyproject.toml`。
- **CI/CD**: 建立了 GitHub Actions 工作流 (`.github/workflows/ci.yml`)，包含 Python 环境设置和 Docker 构建。
- **环境升级**: 将 Python 版本升级至 3.14。
- **代码重构**:
  - 建立了标准的 `src/neuro_sama` 包结构。
  - 引入 `FastAPI` + `SQLModel` 技术栈。
  - 实现了 `Dialogue` 数据模型，用于存储 VTB 对话数据。
  - 实现了基础的 API 接口 (`POST /dialogues/`, `GET /dialogues/`)。
  - 模块化拆分：将代码拆分为 `api`, `core`, `models` 等子模块。
- **模型重构**:
  - 将 `Dialogue` 模型重构为问答对 (Q&A) 结构，包含 `prompt` (提问) 和 `response` (回答) 两部分。
  - 引入 `SQLAlchemy` 的 `JSON` 类型，支持直接存储字典格式的元数据。
- **代码优化**:
  - 使用 FastAPI 推荐的 `lifespan` 替代了过时的 `on_event("startup")`。
  - 添加了数据库连接测试 (`test/test_database.py`)。
  - 在 CI 中集成了 `pytest` 自动测试。

### 遇到的问题与修复

- **构建错误**: 修复了 `pyproject.toml` 中缺少 `[build-system]` 和 `packages` 配置导致 `uv` 无法识别包的问题。
- **Docker 构建**: 修复了 `Dockerfile` 基础镜像名称错误。
- **服务启动**: 解决了 Windows 下 `0.0.0.0` 访问问题，确认服务在 `localhost:8000` 正常运行。

## 待办事项

- [ ] 完善 API 文档。
- [ ] 添加更多数据字段以支持 AI 微调。
- [ ] 对接爬虫项目数据输入。
