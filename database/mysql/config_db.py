import platform


def get_dev_op():
    if platform.system() == "Darwin":
        TEST_DB_INFO = {
            'host': '127.0.0.1',
            'db': 'test',
            'user': 'root',
            'password': 'test',
            'port': 3306
        }
    else: # 운영서버인 경우 환경설정

        TEST_DB_INFO = {
            'host': '127.0.0.1',
            'db': 'test',
            'user': 'root',
            'password': 'test',
            'port': 3306
        }

    return TEST_DB_INFO