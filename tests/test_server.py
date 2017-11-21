from six import PY2

if PY2:
    import SocketServer
else:
    import socketserver as SocketServer
from rqdata.rpc.server import RpcHandler
import pickle

host = 'localhost'
port = 1111
RpcHandler.register(print)
server = SocketServer.TCPServer((host, port), RpcHandler)
server.serve_forever()