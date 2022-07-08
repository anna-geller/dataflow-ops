import pandas as pd
import sqlalchemy


def get_db_connection_string(user: str, password: str) -> str:
    return f"postgresql://{user}:{password}@localhost:5432/postgres"


def get_df_from_sql_query(table_or_query: str) -> pd.DataFrame:
    db = get_db_connection_string()
    engine = sqlalchemy.create_engine(db)
    return pd.read_sql(table_or_query, engine)
