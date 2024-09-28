import pandas as pd
from sqlalchemy import create_engine


engine_ts = create_engine('mysql://root:jtt0304xu@localhost:3306/tushare_stock?charset=utf8mb4&use_unicode=1')


def build_complex_query(*columns, table_name, conditions):
    # 构建 SELECT 查询
    columns_str = ', '.join(columns)
    query = f"SELECT {columns_str} FROM {table_name}"

    # 构建 WHERE 子句
    if conditions:
        where_clauses = [cond.to_sql_clause() for cond in conditions]
        where_clause = ' AND '.join(where_clauses)
        query += f" WHERE {where_clause}"

    return query


def read_common_df_by_sql(sql):
    # sql = f"""SELECT * FROM stock_basic  where 1=1 {where_str} """
    df = pd.read_sql_query(sql, engine_ts)
    return df


def write_stock_name_data(df):
    res = df.to_sql('stock_basic', engine_ts, index=False, if_exists='append', chunksize=5000)
    print(res)


def write_company_business(df):
    res = df.to_sql('stock_company', engine_ts, index=False, if_exists='append', chunksize=5000)