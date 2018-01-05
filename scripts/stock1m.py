from rpc.rpc import RpcClient
import datetime
import logging
import pandas as pd


def get_wind_code(order_book_id):
    stock_code = order_book_id[0:6]
    if order_book_id[9:] == "HG":
        return stock_code + ".SH"
    return stock_code + ".SZ"


def get_stock_list():
    df_instruments = all_instruments(type="CS")
    stocks = list(df_instruments["order_book_id"])
    stocks = list(map(lambda x: str(x), stocks))
    return stocks


def insert_stock(code, client):
    begin_date = client.latest_date(code, type='CS')
    if not begin_date:
        logging.info(code + " failed, begin_date returned None")
        return
    begin_date = datetime.datetime.strptime(str(begin_date), "%Y%m%d") + datetime.timedelta(1)
    end_date = datetime.datetime.now().date()

    df = get_price(code, start_date=begin_date, end_date=end_date, adjust_type="post",
                   frequency="1d", skip_suspended=True)
    if df.empty:
        logging.info(code + "empty df")
        return
    df['time'] = [int(i.strftime("%H%M%S")) for i in df.index]
    df['date'] = [i.strftime("%Y%m%d") for i in df.index]
    df['amt'] = df['total_turnover']
    del df['total_turnover']
    group_data = []
    for name, sub_group in df.groupby('date'):
        dict_data = sub_group.to_dict('list')
        dict_data.update({'date': sub_group['date'].iloc[0]})
        dict_data.update({'order_book_id': code})
        dict_data.update({'wind_code': get_wind_code(code)})
        dict_data.update({'stock_code': code[:6]})
        group_data.append(dict_data)
    client.insert(group_data)


def main():
    # insert_stock(code,client)
    logging.basicConfig(filename='stock_1m.log', level=logging.INFO)
    host = 'www.carniejq.cn'
    port = 1111
    code = "000007.XSHE"
    import time

    client = RpcClient(host, port)
    count = 0
    stock_list = get_stock_list()
    for stock in stock_list:
        insert_stock(stock, client)
        if count % 50 == 0:
            print("\r %f percent complete" % (float(count) / len(stock_list) * 100), end="")
        count = count + 1
    print("\r finished")