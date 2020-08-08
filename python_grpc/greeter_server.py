# coding: utf-8
# @date: 2020-02-14


"""
服务端
"""

import grpc
import time
from concurrent import futures
import helloworld_pb2
import helloworld_pb2_grpc


# 实现定义的方法
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloResponse(message='Hello {msg}'.format(msg=request.name))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50054')
    server.start()
    print('gRPC 服务端已开启，端口为50054...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

