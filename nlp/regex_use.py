import re
import requests


def get_url():
    """url제거시 사용"""
    test_string = "dokdo.go.kr hello world"
    re.sub("((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*", "", test_string)


def get_ip_addr():
    """ip 주소 찾을 시 사용"""
    req = requests.get("http://ipconfig.kr")
    print(re.search(r"IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", req.text)[1])


def delete_number():
    """숫자. 형태 제거시 사용"""
    only_number_delete = r"[0-9]+."


def bracket_english():
    """괄호 안에 있는 영어 정규식"""
    english_in_bracket = r"\([a-zA-Z ]+\)"