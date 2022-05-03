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

# 중복 제거 SQL문 Version 1 - 시간이 오래 걸린다.
with conn.cursor() as cursor:
    SQL = f"DELETE s1 FROM TABLE s1, TABLE s2 WHERE s1.created_at = s2.created_at AND s1.IDX < s2.IDX;"
    print(SQL)
    print(cursor.execute(SQL))
    conn.commit()


# 중복 제거 SQL문 Version 2 - 더 빠르고 정확하다.
TABLE = "TEST"
with conn.cursor() as cursor:
    SQL = f"select FOREIGN_IDX from(select TABLE_NAME, KEYWORD, FOREIGN_IDX, count(*) as cnt from {TABLE} group by TABLE_NAME, KEYWORD, FOREIGN_IDX) a where cnt > 1"

    result = cursor.execute(SQL)
    if result > 0:
        foreign_range = [x[0] for x in cursor.fetchall()]

        SQL_IN_RANGE = f"select IDX, KEYWORD, FOREIGN_IDX, SERIAL_NUMBER, USER_SPEAK from {TABLE} where FOREIGN_IDX in {tuple(foreign_range)};"
        cursor.execute(SQL_IN_RANGE)
        result_in_range = cursor.fetchall()

        tmp_delete_target = []
        tmp_duplicate_dict = {}
        for result_in_range_item in result_in_range:
            original_key = str(result_in_range_item[1]) + str(result_in_range_item[2])
            duplicate_found = tmp_duplicate_dict.get(original_key, None)
            if duplicate_found is None:
                print("origin", result_in_range_item[0], result_in_range_item[2], result_in_range_item[3],
                      result_in_range_item[4])
                tmp_duplicate_dict[original_key] = result_in_range_item[0]
            else:
                print("dup", result_in_range_item[0], result_in_range_item[2], result_in_range_item[3],
                      result_in_range_item[4])
                tmp_delete_target.append(result_in_range_item[0])

        SQL_DELETE = f"DELETE FROM {TABLE} WHERE IDX in {tuple(tmp_delete_target)};"

        cursor.execute(SQL_DELETE)
        conn.commit()