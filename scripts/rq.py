from rpc.rpc import RpcClient
import datetime
import logging
import pandas as pd
import click
import time

'''
rice quant code to download minute bars data

'''


def get_stock_list():
    df_instruments = all_instruments(type="CS")
    stocks = list(df_instruments["order_book_id"])
    stocks = list(map(lambda x: str(x), stocks))
    return stocks


def insert_one(client, code, default_start='20050104'):
    start_date = client.latest_date(code)
    start_date = start_date + datetime.timedelta(1) if start_date else default_start
    end_date = pd.to_datetime('today').strftime("%Y%m%d")
    df = get_price(code, start_date=start_date, end_date=end_date, adjust_type='none', frequency='1m')
    if not df.empty:
        df['dt'] = df.index
        client.insert(code, df.to_dict('record'))


def test():
    host = 'www.carniejq.cn'
    port = 31245
    code = "000007.XSHE"
    client = RpcClient(host, port)
    with click.progressbar(get_stock_list(),
                           label="Fetching minute bars:",
                           item_show_func=lambda e: e if e is None else str(e),
                           ) as bar:
        bar.is_hidden = False
        for code in bar:
            insert_one(client, code, default_start='20171111')
    client.stop_all()


test()
