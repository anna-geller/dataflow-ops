# import pandas as pd
# import sqlalchemy
#
#
# def get_db_connection_string(
#     user: str, password: str, host: str = "localhost", db: str = "postgres"
# ) -> str:
#     return f"postgresql://{user}:{password}@{host}:5432/{db}"
#
#
# def get_df_from_sql_query(table_or_query: str) -> pd.DataFrame:
#     db = get_db_connection_string()
#     engine = sqlalchemy.create_engine(db)
#     return pd.read_sql(table_or_query, engine)
