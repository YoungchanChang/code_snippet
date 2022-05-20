import logging.config

from flask_factory.simple_mvc.model import insert_values
from config.log_config import config_basic
from domain.user import UserInfo
from domain.custom_error import UserValueException

logging.config.dictConfig(config_basic)
logger = logging.getLogger('simple_log')


def sign_up(user_point: UserInfo):
    """회원 가입"""
    if not isinstance(user_point.user_name, str) or not isinstance(user_point.user_email, str):
        raise UserValueException

    return insert_values(user_name=user_point.user_name, user_email=user_point.user_email)