config_basic = {
    "version": 1,
    'disable_existing_loggers': True,
    "formatters": {
        "simple": {"format": "[%(name)s] [%(levelname)s] %(message)s"},
        "decorator_format": {"format": "[%(name)s] [%(levelname)s] %(message)s"},
        "complex": {
            "format": "%(asctime)s %(levelname)s [%(name)s] [%(pathname)s:%(funcName)s:%(lineno)d] - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG",
            'stream': 'ext://sys.stdout',
        },
        "decorator_handler": {
            "class": "logging.StreamHandler",
            "formatter": "decorator_format",
            "level": "DEBUG",
            'stream': 'ext://sys.stdout',
        },
        "access": {
            "class": "logging.FileHandler",
            "filename": "access.log",
            "formatter": "complex",
            "level": "INFO",
        },
        "warning": {
            "class": "logging.FileHandler",
            "filename": "warning.log",
            "formatter": "complex",
            "level": "WARNING",
        },
        "error": {
            "class": "logging.FileHandler",
            "filename": "error.log",
            "formatter": "complex",
            "level": "ERROR",
        },
        "critical": {
            "class": "logging.FileHandler",
            "filename": "critical.log",
            "formatter": "complex",
            "level": "ERROR",
        },
    },
    "loggers": {
        "simple_log": {"handlers": ["console", "access", "warning", "error", "critical"], "level": "DEBUG"},
        "decorator": {"handlers": ["decorator_handler"], "level": "DEBUG"},
        "parent": {"level": "DEBUG"}, "parent.child": {"level": "DEBUG"},},
}
