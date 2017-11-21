# -*- coding: utf-8 -*-

import zlib
import socket
import struct
import threading
import pickle


def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = zlib.compress(pickle.dumps(msg, protocol=2), 3)
    length = len(msg)
    msg = struct.pack('>I', length) + msg
    sock.sendall(msg)


def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = sock.recv(4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)


def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    total_data = []
    data = b''
    byte_recved = 0
    while byte_recved < n:
        packet = sock.recv(n - byte_recved)
        if not packet:
            return None
        total_data.append(packet)
        byte_recved = byte_recved + len(packet)
    data = b''.join(total_data)
    return pickle.loads(zlib.decompress(data))


class RpcClient(object):
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        errno = self.sock.connect_ex((address, port))
        if errno != 0:
            print("connectting to server failed")

    def __getattr__(self, name):
        """实现远程调用功能"""

        # 执行远程调用任务
        def dorpc(*args, **kwargs):
            # 生成请求
            req = [name, args, kwargs]

            send_msg(self.sock, req)
            repb = recv_msg(self.sock)
            return repb

        return dorpc
