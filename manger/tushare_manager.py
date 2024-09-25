
import tushare as ts


def get_tushare_pro():
    access_token = 'f6402ff7aa2f4c8c29d80a90fbc1f4e56c238cadce1ce554cbc0074a'
    pro = ts.pro_api(access_token)
    return pro


def get_stock_name_data(pro):
    df = pro.stock_basic()
    return df



