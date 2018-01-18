from six import PY2

if PY2:
    import SocketServer
else:
    import socketserver as SocketServer
from rqdata.mongo.libs import *
from rqdata.rpc.server import RpcHandler


def run_server():
    mongo_helper = MongoHelper("127.0.0.1", 27017)
    host = 'localhost'
    port = 1111
    RpcHandler.register(mongo_helper.latest_date)
    RpcHandler.register(mongo_helper.insert)
    server = SocketServer.TCPServer((host, port), RpcHandler)
    server.serve_forever()
