# Neuro-sama Project

本项目用于收集和管理 VTB 相关对话数据，支持多直播间数据隔离。当前架构不再包含后端 API 服务和数据库，数据将通过定时文件传输（如 scp）进行同步。

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

### 依赖管理

- 添加依赖: `uv add <package_name>`
- 添加开发依赖: `uv add --dev <package_name>`
- 移除依赖: `uv remove <package_name>`

## 数据同步

请通过定时任务将数据文件通过 scp 等方式同步到本地进行处理。
