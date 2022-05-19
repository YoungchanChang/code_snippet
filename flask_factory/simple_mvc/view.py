import traceback
from dacite import from_dict
from flask import Blueprint, make_response, jsonify, request

from model import UserInfo
from flask_factory.simple_mvc.control import sign_up, UserValueException

from utility import SlackAlarm

user_info = Blueprint('user_info', __name__)


@user_info.route("/user_info", methods=["POST"])
def user_signup():

    """ 사용자 회원가입 """

    return_json = {
        "code": 500,
        "message": "fail",
    }
    try:
        input_json = request.get_json()
        row_affected = sign_up(user_point=from_dict(UserInfo, input_json))

        if row_affected < 1:
            raise ValueError

    except UserValueException as uve:
        return_json['code'] = 200
        return_json['message'] = "fail"
        return_json['message_detail'] = str(uve)
        return make_response(jsonify(return_json), 200)

    except ValueError as ve:
        return_json['code'] = 200
        return_json['message'] = "fail"
        return_json['message_detail'] = str(ve)
        return make_response(jsonify(return_json), 200)

    except Exception as e:
        tf = traceback.format_exc()
        SlackAlarm.send_slack_alarm("user_info", tf) # 슬랙 알람 or 로그
        return_json['message_detail'] = tf
        return make_response(jsonify(return_json), 500)

    return_json['code'] = 200
    return_json['message'] = "success"
    return make_response(jsonify(return_json), 200)