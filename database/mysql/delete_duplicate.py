import pymysql

def conn_mysqldb():
    MYSQL_HOST = 'localhost'
    MYSQL_CONN = pymysql.connect(
        host=MYSQL_HOST,
        port=3306,
        user='root',
        passwd='1234',
        db='test_database',
        charset='utf8'
    )
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN

conn = conn_mysqldb()

# 중복 제거 SQL문 Version 1
with conn.cursor() as cursor:
    SQL = f"DELETE s1 FROM TABLE s1, TABLE s2 WHERE s1.created_at = s2.created_at AND s1.IDX < s2.IDX;"
    print(SQL)
    print(cursor.execute(SQL))
    conn.commit()