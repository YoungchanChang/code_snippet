"""정상적인 시간 입력시 사용하는 함수

- 문자열을 시간으로 변환 : str_to_time()
- 시간을 문자열로 변환 : time_to_str()
- 날짜를 튜플 형식으려 변환 : tuplize_string_date()

- ref : https://docs.python.org/ko/3/library/datetime.html
- ref : https://minus31.github.io/2018/07/28/python-date/
"""

from datetime import datetime, timedelta, date, time


def str_to_time():
    """문자열을 시간으로 변환"""
    time_str = "2016-09-15 01:00:04.001"
    time_date = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")

    day_before = "2016-09-14"
    time_date_until_day = datetime.strptime(day_before, "%Y-%m-%d")

    return time_date, time_date_until_day


def time_to_str():
    """시간을 문자열로 변환"""
    time_str = "2016-09-15 01:00:04.001"
    time_date = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
    string_today = time_date.strftime('%Y-%m-%d')

    return string_today


def separate_date_time():
    d = date(2018, 7, 28)
    t = time(12, 23, 38)
    dt = datetime.combine(d, t)  # 합치기
    return dt


def tuplize_string_date():
    """날짜를 튜플 형식으려 변환"""
    tuple_time = "2016-01-11 01:00:04.001"
    tuple_day = datetime.strptime(tuple_time, "%Y-%m-%d %H:%M:%S.%f")
    print(tuple_day.timetuple())
    # tm_wday : 정수로 요일을 반환. 월요일은 0이고 일요일은 6
    # tm_yday : 1년에서 얼마가 지났는지
    return tuple_day.timetuple()


def add_time():
    date_info = "2016-09-14"
    date_info = datetime.strptime(date_info, "%Y-%m-%d")
    date_add = date_info + timedelta(days=2,
                                     seconds=27,
                                     microseconds=10,
                                     milliseconds=29000,
                                     minutes=5,
                                     hours=8,
                                     weeks=2)
    return date_add


def minus_time_to_time():
    a_Datetime = datetime.strptime('2018-07-28 00:00:00', '%Y-%m-%d %H:%M:%S')
    b_Datetime = datetime.strptime('2017-05-26 00:00:10', '%Y-%m-%d %H:%M:%S')
    result = a_Datetime - b_Datetime
    # print(result)  # 1 day, 0:00:10
    # print(result.days)  # 1
    # print(result.seconds)  # 10
    return result


def get_only_time(time_str: str):
    time_format = "%H:%M"
    time_str = datetime.strptime(time_str, time_format)
    time_tuple = time_str.timetuple()
    time_only = time(time_tuple.tm_hour, time_tuple.tm_min, time_tuple.tm_sec)
    return time_only


if __name__ == "__main__":
    print("str_to_time() :", str_to_time())
    print("time_to_str() :", time_to_str())
    print("separate_date_time() :", separate_date_time())
    print("tuplize_string_date() :", tuplize_string_date())
    print("add_time() :", add_time())
    print("minus_time_to_time() :", minus_time_to_time())
