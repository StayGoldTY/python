# 使用官方 Python 运行时作为父镜像
FROM python:3.8

# 创建并设置工作目录
WORKDIR /app

# 复制 requirements.txt 文件到工作目录
COPY requirements.txt ./ 

# 安装 requirements.txt 中列出的所有 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制当前目录中的所有文件到工作目录
COPY . ./

# Streamlit 使用的端口
EXPOSE 8501

# 启动 Streamlit 应用
CMD streamlit run appnew.py