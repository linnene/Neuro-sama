# Neuro-sama Project

本项目用于收集和管理 VTB 相关对话数据，支持多直播间数据隔离。

**当前架构**：
- **无后端服务**：不再运行 FastAPI 服务或数据库。
- **数据同步**：通过文件传输（如 SCP）将爬虫生成的 JSON 数据同步到本地。
- **数据处理**：本地脚本读取数据文件，使用 Pydantic 模型进行校验和清洗。

## 📚 文档索引

- **[项目结构 (Project Structure)](PROJECT_STRUCTURE.md)**
- **[开发日志 (Dev Log)](DEV_LOG.md)**
- **[测试指南 (Testing)](TESTING.md)**
- **[路线图 (Roadmap)](ROADMAP.md)**

## 快速开始

### 环境准备

本项目使用 `uv` 进行包管理，Python 版本要求 `>=3.14`。

```bash
uv sync
```

### 核心依赖

- **Python 3.14+**
- **Pydantic**: 用于数据结构定义和校验。

### 常用命令

- **运行测试**:
  ```bash
  uv run pytest
  ```

- **添加依赖**:
  ```bash
  uv add <package_name>
  ```

## 数据模型

项目核心定义了两个数据模型（位于 `src/neuro_sama/models/`）：

1.  **Stream**: 直播流元数据（ID, 标题, 主播, 时间等）。
2.  **Dialogue**: 对话数据（问题, 回答, 时间戳, 置信度等）。

这些模型用于验证从爬虫同步过来的 JSON 数据格式。
