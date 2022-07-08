import pandas as pd
from sqlalchemy import create_engine


def get_snowflake_connection_string(
    user: str,
    password: str,
    account_id: str,
    database: str = "DEV",
    schema: str = "JAFFLE_SHOP",
    warehouse_name: str = "COMPUTE_WH",
    role: str = "SYSADMIN",
) -> str:
    return f"snowflake://{user}:{password}@{account_id}/{database}/{schema}?warehouse={warehouse_name}&role={role}"


def get_df_from_sql_query(
    table_or_query: str,
    user: str,
    password: str,
    account_id: str,
    database: str = "DEV",
    schema: str = "JAFFLE_SHOP",
    warehouse_name: str = "COMPUTE_WH",
    role: str = "SYSADMIN",
) -> pd.DataFrame:
    db = get_snowflake_connection_string(
        user, password, account_id, database, schema, warehouse_name, role
    )
    engine = create_engine(db)
    return pd.read_sql(table_or_query, engine)


def load_df_to_snowflake(
    df: pd.DataFrame,
    table_name: str,
    user: str,
    password: str,
    account_id: str,
    database: str = "DEV",
    schema: str = "JAFFLE_SHOP",
    warehouse_name: str = "COMPUTE_WH",
    role: str = "SYSADMIN",
) -> None:
    conn_string = get_snowflake_connection_string(
        user, password, account_id, database, schema, warehouse_name, role
    )
    db_engine = create_engine(conn_string)
    conn = db_engine.connect()
    # conn.execute(f"TRUNCATE TABLE DEV.{schema}.{table_name};")
    df.to_sql(
        table_name, schema=schema, con=db_engine, if_exists="replace", index=False
    )
    conn.close()
