import functools
import time
import traceback
import types


def log_basic(logger, path=None):
    def log_decorated(func):
        @functools.wraps(func)
        def log_wrapper(*args, **kwargs):
            st = time.perf_counter()

            try:
                func_result = func(*args, **kwargs)

                return_func_result = func_result
                if isinstance(func_result, types.GeneratorType):
                    return_func_result = list(func_result)

                debug_info = {"path": path, "method": func.__name__, "args": args, "kwargs": kwargs,
                              "return": return_func_result,
                              "total_time": round(time.perf_counter() - st, 3)}
                logger.debug(debug_info)
                return return_func_result

            except Exception as e:

                exception_info = {"path": path,  "method": func.__name__, "args": args, "kwargs": kwargs,
                                  "exception_class": e,
                                  "exception_reason": traceback.format_exc(),
                                  "total_time": round(time.perf_counter() - st, 3)}
                logger.critical(exception_info)
                raise
        return log_wrapper
    return log_decorated
