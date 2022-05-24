import pymysql

from database.mysql import config_db
from sqlalchemy import create_engine

TEST_DB_INFO = config_db.get_dev_op()

user_analyzed_engine = create_engine(f'mysql://{TEST_DB_INFO.get("user")}:{TEST_DB_INFO.get("password")}@{TEST_DB_INFO.get("host")}:{TEST_DB_INFO.get("port")}/{TEST_DB_INFO.get("db")}', convert_unicode=False, pool_size=20, pool_recycle=500, max_overflow=20)


def get_connection():
    MYSQL_CONN = pymysql.connect(
        **TEST_DB_INFO
    )
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)

    return MYSQL_CONN
