"""
connection pool : https://docs.sqlalchemy.org/en/14/core/pooling.html
session : https://docs.sqlalchemy.org/en/14/orm/session_basics.html
wait_timeout : https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html
"""

import time

from sqlalchemy.orm import Session
from faker import Faker

from database.mysql.conn import *

fake = Faker()

TEST_DB_INFO = config_db.get_dev_op()


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