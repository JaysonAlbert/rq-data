# -*- coding: utf-8 -*-
from rqdata.rpc.client import RpcClient

if __name__ == '__main__':
    host = 'localhost'
    port = 1111

    client = RpcClient(host, port)
    date = client.latest_date("CF0000", type='future')
    date = client.latest_date("IC0000", type='future')
    print(date)
