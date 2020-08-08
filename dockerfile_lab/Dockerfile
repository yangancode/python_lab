FROM python:3
# 标明作者
LABEL author="yangan"
# 设置工作目录，即进入容器后的默认路径
WORKDIR /data/docker-test
# 将宿主机的docker-test目录的内容拷贝到容器
ADD ./docker-test /data/docker-test
# 安装Python依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 暴露端口
EXPOSE 10086
# 设置环境变量
ENV PYTHONIOENCODING=utf-8
# 执行Python脚本
CMD [ "python", "./flask_server.py" ]
