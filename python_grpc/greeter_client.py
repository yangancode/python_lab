# coding: utf-8
# @date: 2020-02-14

"""
客户端
"""

import grpc

import helloworld_pb2, helloworld_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50054')

    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='World'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
