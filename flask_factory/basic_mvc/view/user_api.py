import traceback
from dacite import from_dict
from flask import Blueprint, make_response, jsonify, request
import logging.config

from config.log_config_basic import config_basic
from domain.user import UserInfo
from control.user_info import sign_up, UserValueException
from utility.log_color import CustomFormatter

from utility.slack_alarm import SlackAlarm

user_info = Blueprint('user_info', __name__)

logging.config.dictConfig(config_basic)
logger = logging.getLogger('simple_log')

stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(CustomFormatter(config_basic['formatters']['complex']['format']))

logger.addHandler(stdout_handler)


@user_info.route("/user_info", methods=['GET', "POST"])
def user_signup():

    """ 사용자 회원가입 """

    return_json = {
        "code": 500,
        "message": "fail",
    }
    logger.error({'status': 'access', 'user_ip': request.remote_addr, "request_path": request.path,
                 "return": "no_value"})
    try:
        input_json = request.get_json()
        row_affected = sign_up(user_point=from_dict(UserInfo, input_json))

        if row_affected < 1:
            logger.info({'status': 'success', 'user_ip': request.client.host, "request_path": request.url.path,
                         "return": "no_value"})
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
        logger.error(
            {'status': 'fail', 'user_ip': request.client.host, "request_path": request.url.path, "message": ve})
        return make_response(jsonify(return_json), 200)

    except Exception as e:
        tf = traceback.format_exc()
        SlackAlarm.send_slack_alarm("user_info", tf) # 슬랙 알람 or 로그
        return_json['message_detail'] = tf
        logger.critical({'status': 'fail', 'user_ip': request.client.host, "request_path": request.url.path, "message": tf})
        return make_response(jsonify(return_json), 500)

    return_json['code'] = 200
    return_json['message'] = "success"
    return make_response(jsonify(return_json), 200)

