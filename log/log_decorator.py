"""로그 데코레이터 포맷
# https://hwangheek.github.io/2019/python-logging/
# https://greeksharifa.github.io/%ED%8C%8C%EC%9D%B4%EC%8D%AC/2019/12/13/logging/
# https://hamait.tistory.com/880
# https://velog.io/@otzslayer/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A1%9C%EA%B9%85-%EB%A9%8B%EC%A7%80%EA%B2%8C-%ED%95%98%EA%B8%B0

## https://hwangheek.github.io/2019/python-logging/

# 로그 데코레이터 활용
- logger_setting : 외부 로거 삽입
  - 데코레이터를 활용하는 쪽에서 추가 정보 삽입
  - 없어도 동작 가능
- log_decorated : 데코레이터로 감싸는 부분
- log_function : 실제 함수가 수행되는 부분
"""

import functools
import time
import traceback

import logging

formatter = "%(asctime)s.%(msecs)03d\t%(levelname)s\t[%(name)s]\t%(message)s"
logging.basicConfig(level=logging.DEBUG, format=formatter, datefmt='%m/%d/%Y %I:%M:%S')
loggers = logging.getLogger(__name__)
loggers.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter( "%(asctime)s.%(msecs)03d\t%(levelname)s\t[%(name)s]\n%(message)s")
ch.setFormatter(formatter)
example_sentence = "Get Plenty of Sleep."
loggers.addHandler(ch)
loggers.propagate = 1

def logger_setting(logger, meta_info=None):
    def log_decorated(func):
        @functools.wraps(func)
        def log_function(*args, **kwargs):
            st = time.perf_counter() # 시작 시간 체크

            try:
                func_result = func(*args, **kwargs) # 함수 시행하는 부분

                debug_info = {"method": func.__name__,
                              "doc": func.__doc__,
                              "args": args, "kwargs": kwargs,
                              "return": func_result,
                              "meta_info": meta_info,
                              "total_time": round(time.perf_counter() - st, 3)} #끝난 시간 체크
                logger.debug(debug_info)
                return func_result

            except Exception as e:
                # 예외 발생시 예외를 로그로 남기고 진행
                exception_info = {"method": func.__name__,
                                  "doc": func.__doc__,
                                  "args": args, "kwargs": kwargs,
                                  "exception_class": e,
                                  "exception_reason": traceback.format_exc(),
                                  "meta_info": meta_info,
                                  "total_time": round(time.perf_counter() - st, 3)}
                logger.critical(exception_info)
                raise
        return log_function
    return log_decorated


@logger_setting(logger=loggers, meta_info="SLEEP")
def time_func(second=5):
    """테스트를 위한 sleep 함수"""
    time.sleep(second)


@logger_setting(logger=loggers, meta_info="SUM")
def sum_func(*numbers):
    """테스트를 위한 sleep 함수"""
    if numbers is None:
        raise Exception
    return sum(numbers)


if __name__ == "__main__":
    # time_func(second=1)
    try:
        sum_func(5)
    except Exception as fe:
        print("This is just for test")