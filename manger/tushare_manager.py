
import tushare as ts


def get_tushare_pro():
    access_token = '31ef346b3bfab52fc2a07c87e54ca18ef6dfb9adfd3d099c110b152a'
    pro = ts.pro_api(access_token)
    return pro


def get_stock_name_data(pro):
    df = pro.stock_basic()
    return df


def get_daily_trade_by_tscode(*args: object) -> object:
    """获取每日交易的数据
    :param args:
    :return:
    """
    pass



