import SocketServer
from mongo.libs import *
from rpc.server import RpcHandler

mongo_helper = MongoHelper("192.168.0.114",27017)
host = 'localhost'
port = 1111
RpcHandler.register(mongo_helper.latest_date)
RpcHandler.register(mongo_helper.insert)
server = SocketServer.TCPServer((host, port), RpcHandler)
server.serve_forever()