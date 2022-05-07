from flask_factory.mvc.model import insert_values
from model import UserInfo


class UserValueException(Exception):
    ...


def sign_up(user_point: UserInfo):
    """회원 가입"""
    if not isinstance(user_point.user_name, str) or not isinstance(user_point.user_email, str):
        raise UserValueException

    return insert_values(user_name=user_point.user_name, user_email=user_point.user_email)