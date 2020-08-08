# gRPC demo


## 安装
pip install grpcio

pip install grpcio-tools


## 编译
python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/newadmin.proto