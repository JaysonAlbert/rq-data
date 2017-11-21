# -*- coding: utf-8 -*-
from rqdata.rpc.client import *

from six import PY2

if PY2:
    import SocketServer
else:
    import socketserver as SocketServer


class RpcHandler(SocketServer.StreamRequestHandler):
    __functions = {}

    def handle(self):
        while self.request:
            data = recv_msg(self.request)
            if not data:
                break
            name, args, kwargs = data
            func = RpcHandler.__functions[name]
            rt = func(*args, **kwargs)
            send_msg(self.request, rt)

    @staticmethod
    def register(func):
        RpcHandler.__functions[func.__name__] = func


def hello(a):
    return 2 * a


if __name__ == '__main__':
    host = 'localhost'
    port = 1111
    RpcHandler.register(hello)
    server = SocketServer.TCPServer((host, port), RpcHandler)
    server.serve_forever()
