"""
https://dev.mysql.com/doc/refman/8.0/en/insert.html
"""

def insert_ignore(data):
    table_name = "TEST"
    conn = get_user_info_conn()
    with conn.cursor() as cursor:
        sql = f"INSERT IGNORE INTO {table_name} (co1, col2, col3) VALUES (%s,%s,%s)"
        cursor.executemany(sql, (data))
        conn.commit()
    conn.close()

def SELECT_DATA(customerCode):
    conn = get_user_info_conn()
    TABLE = f"USER_{customerCode}"
    with conn.cursor() as cursor:
        SELECT_QUERY = f"SELECT co1, col2, col3 FROM {TABLE} WHERE A = 'B'"
        cursor.execute(SELECT_QUERY)
        sql_data = cursor.fetchall()

        return sql_data