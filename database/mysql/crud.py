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

