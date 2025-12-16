# 使用 Python 3.14 slim 版本作为基础镜像
FROM python:3.14-slim

# 从官方镜像中复制 uv 工具
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# 设置工作目录
WORKDIR /app

# 设置环境变量
# 防止 Python 生成 .pyc 文件
ENV PYTHONDONTWRITEBYTECODE=1
# 确保 Python 输出直接打印到终端
ENV PYTHONUNBUFFERED=1

# 复制依赖定义文件
COPY pyproject.toml uv.lock README.md ./

# 安装依赖
# --frozen: 严格按照 uv.lock 安装
# --no-dev: 不安装开发依赖
# --no-install-project: 只安装依赖，不安装当前项目（因为源码还没复制）
RUN uv sync --frozen --no-dev --no-install-project

# 复制项目源代码
COPY . .

# 再次同步，安装当前项目
RUN uv sync --frozen --no-dev

# 将虚拟环境添加到 PATH
ENV PATH="/app/.venv/bin:$PATH"

# 暴露端口
EXPOSE 8000

# 启动应用
CMD [ "uv", "run", "python", "main.py" ]

