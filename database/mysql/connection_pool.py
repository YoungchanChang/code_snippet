"""
connection pool : https://docs.sqlalchemy.org/en/14/core/pooling.html
session : https://docs.sqlalchemy.org/en/14/orm/session_basics.html
wait_timeout : https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html
"""

import time
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.mysql import config_db
from faker import Faker

user_analyzed_engine = create_engine(f'mysql://{config_db.TEST_DB_INFO.get("user")}:{config_db.TEST_DB_INFO.get("password")}@{config_db.TEST_DB_INFO.get("host")}:{config_db.TEST_DB_INFO.get("port")}/{config_db.TEST_DB_INFO.get("db")}', convert_unicode=False, pool_size=20, pool_recycle=500, max_overflow=20)

fake = Faker()


def get_connection():
    MYSQL_CONN = pymysql.connect(
        **config_db.TEST_DB_INFO
    )
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)

    return MYSQL_CONN


def create_user_by_single_conn(name: str, email: str):
    conn = get_connection()
    with conn.cursor() as cursor:
        SQL = f"""
        INSERT INTO user_db (user_name, user_email) VALUES ('{name}', '{email}');
        """
        cursor.execute(SQL)
    conn.commit()


def create_user_by_pool(name: str, email: str):
    with Session(autocommit=False, autoflush=False, bind=user_analyzed_engine) as session:
        SQL = f"INSERT INTO user_db (user_name, user_email) VALUES ('{name}', '{email}');"
        row_count = session.execute(SQL).rowcount
        session.commit()
        return row_count


if __name__ == "__main__":
    st = time.time()

    for i in range(0, 10, 1):
        create_user_by_single_conn(fake.name(), fake.ascii_safe_email())
    print("not_connection_pool", time.time()-st)

    st = time.time()
    for i in range(0, 10, 1):
        create_user_by_pool(fake.name(), fake.ascii_safe_email())

    print("connection_pool", time.time() - st)