"""
get_dev_op()
- 개발서버, 운영서버 구분

get_ipaddr()
- ip address구하기.
- MSA구조에 사용
"""

import platform
import requests
import re
import socket


def get_dev_op():
    if platform.system() == "Darwin": # MAC인 경우 환경설정
        ...
    else: # 운영서버인 경우 환경설정
        ...


def get_ipaddr():
    req = requests.get("http://ipconfig.kr")
    print(re.search(r"IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", req.text)[1])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("pwnbit.kr", 443))
    print(sock.getsockname()[0])