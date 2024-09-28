import tushare as ts
import manger.mysql_helper as sql_helper


def get_tushare_pro():
    access_token = '31ef346b3bfab52fc2a07c87e54ca18ef6dfb9adfd3d099c110b152a'
    pro = ts.pro_api(access_token)
    return pro


def get_stock_name_data(pro):
    """
    获取股票的基本信息
    :param pro:tushare_pro
    :return:df
    """
    df = pro.stock_basic()
    return df


def get_company_business(pro, ts_code=""):
    """
    获取业务范围等信息
    :param pro:tushare_pro
    :param ts_code:code
    :return:df
    """
    df = pro.stock_company(ts_code=ts_code, fields=[
        "ts_code",
        "com_name",
        "com_id",
        "chairman",
        "manager",
        "secretary",
        "reg_capital",
        "setup_date",
        "province",
        "city",
        "website",
        "email",
        "employees",
        "exchange",
        "introduction",
        "office",
        "business_scope",
        "ann_date",
        "main_business"
    ])
    return df


def get_income_kernel(pro, ts_code):
    """
    获取利润表
    :param pro:
    :param ts_code:code代码，必填
    :return:df
    """
    df = pro.income(**{
        "ts_code": ts_code,
        "ann_date": "",
        "f_ann_date": "",
        "start_date": "",
        "end_date": "",
        "period": "",
        "report_type": "",
        "comp_type": "",
        "is_calc": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "ts_code",
        "ann_date",
        "f_ann_date",
        "end_date",
        "report_type",
        "comp_type",
        "end_type",
        "basic_eps",
        "diluted_eps",
        "total_revenue",
        "revenue",
        "int_income",
        "prem_earned",
        "comm_income",
        "n_commis_income",
        "n_oth_income",
        "n_oth_b_income",
        "prem_income",
        "out_prem",
        "une_prem_reser",
        "reins_income",
        "n_sec_tb_income",
        "n_sec_uw_income",
        "n_asset_mg_income",
        "oth_b_income",
        "fv_value_chg_gain",
        "invest_income",
        "ass_invest_income",
        "forex_gain",
        "total_cogs",
        "oper_cost",
        "int_exp",
        "comm_exp",
        "biz_tax_surchg",
        "sell_exp",
        "admin_exp",
        "fin_exp",
        "assets_impair_loss",
        "prem_refund",
        "compens_payout",
        "reser_insur_liab",
        "div_payt",
        "reins_exp",
        "oper_exp",
        "compens_payout_refu",
        "insur_reser_refu",
        "reins_cost_refund",
        "other_bus_cost",
        "operate_profit",
        "non_oper_income",
        "non_oper_exp",
        "nca_disploss",
        "total_profit",
        "income_tax",
        "n_income",
        "n_income_attr_p",
        "minority_gain",
        "oth_compr_income",
        "t_compr_income",
        "compr_inc_attr_p",
        "compr_inc_attr_m_s",
        "ebit",
        "ebitda",
        "insurance_exp",
        "undist_profit",
        "distable_profit",
        "rd_exp",
        "fin_exp_int_exp",
        "fin_exp_int_inc",
        "transfer_surplus_rese",
        "transfer_housing_imprest",
        "transfer_oth",
        "adj_lossgain",
        "withdra_legal_surplus",
        "withdra_legal_pubfund",
        "withdra_biz_devfund",
        "withdra_rese_fund",
        "withdra_oth_ersu",
        "workers_welfare",
        "distr_profit_shrhder",
        "prfshare_payable_dvd",
        "comshare_payable_dvd",
        "capit_comstock_div",
        "continued_net_profit",
        "update_flag",
        "net_after_nr_lp_correct",
        "oth_income",
        "asset_disp_income",
        "end_net_profit",
        "credit_impa_loss",
        "net_expo_hedging_benefits",
        "oth_impair_loss_assets",
        "total_opcost",
        "amodcost_fin_assets"
    ])


def get_income(pro):
    conditions = [
        # condition.Condition('ts_code', '=', '000020.SZ'),
    ]
    query_company = sql_helper.build_complex_query("ts_code", table_name="stock_basic", conditions=conditions)
    company_df = sql_helper.read_common_df_by_sql(query_company)
    print(company_df)
    # for comany in company_df:



def get_daily_trade_by_tscode(*args: object) -> object:
    """
    获取每日交易的数据
    :param args:
    :return:
    """
    pass
