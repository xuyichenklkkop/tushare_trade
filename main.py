import manger.tushare_manager as ts_manager
import manger.mysql_helper as sql_helper
import manger.Condition as condition

import threading

if __name__ == '__main__':
    pro = ts_manager.get_tushare_pro()
    """查询公司基本信息"""
    # basic_df = ts_manager.get_stock_name_data(pro)
    # sql_helper.write_stock_name_data(basic_df)

    """查询公司业务信息"""
    # company_business = ts_manager.get_company_business(pro)
    # sql_helper.write_company_business(company_business)

    """查询现金流量表"""
    # t0 = threading.Thread(target=ts_manager.get_income,args=(pro,))
    """查询负债表"""
    # t1= threading.Thread(target=ts_manager.get_balance,args=(pro,))
    """查询利润表"""
    # t2 = threading.Thread(target=ts_manager.get_income,args=(pro,))
    # t0.start()
    # t1.start()
    # t2.start()

    #交易日历
    #ts_manager.get_trade_day(pro)

    # 复权因子
    ts_manager.get_adj_factor_all(pro)

    #每日行情
    #ts_manager.get_daily_trade(pro)
    print("daily finished")
