from dataclasses import dataclass

import pymysql
TEST_DB_INFO = {
    'host': '127.0.0.1',
    'db': 'mecab_ner',
    'user': 'mecab_ner',
    'password': 'mecab_ner',
    'port': 3307
}


def get_connection():
    """커넥션 객체 생성"""
    MYSQL_CONN = pymysql.connect(
        **TEST_DB_INFO
    )
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)

    return MYSQL_CONN


def select_all():
    """모든 데이터 반환"""
    test_db_conn = get_connection()
    with test_db_conn.cursor() as cursor:
        TABLE = "user_db"
        sql = f"SELECT * FROM {TABLE};"
        return cursor.fetchall(sql)


def insert_values(user_name, user_email):
    """회원가입 요청"""
    test_db_conn = get_connection()
    with test_db_conn.cursor() as cursor:
        TABLE = "user_db"
        sql = f"INSERT INTO {TABLE} (user_name, user_email) VALUES ('{user_name}', '{user_email}');"
        cursor.fetchall(sql)
        results = test_db_conn.affected_rows()

    test_db_conn.close()
    return results


@dataclass
class UserInfo:
    user_name: str
    user_email: str
