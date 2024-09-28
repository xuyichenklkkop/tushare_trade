import manger.tushare_manager as ts_manager
import manger.mysql_helper as sql_helper
import manger.Condition as condition

if __name__ == '__main__':
    pro = ts_manager.get_tushare_pro()
    """查询公司基本信息"""
    # basic_df = ts_manager.get_stock_name_data(pro)
    # sql_helper.write_stock_name_data(basic_df)

    """查询公司业务信息"""
    # company_business = ts_manager.get_company_business(pro)
    # sql_helper.write_company_business(company_business)

    """查询利润表"""
    ts_manager.get_income(pro);

    # conditions = [
    # condition.Condition('ts_code', '=', '000020.SZ'),
    # ]
    # query = sql_helper.build_complex_query("*", table_name="stock_basic", conditions=conditions)
    # df = sql_helper.read_common_df_by_sql(query)

    # ts_manager.get_daily_trade_by_tscode()
    # print(df)
