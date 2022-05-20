FROM python:3.7.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade installed packages
RUN apt-get update && apt-get upgrade -y && apt-get clean

RUN apt-get update

# Upgrade pip to latest version
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py --force-reinstall && rm get-pip.py

# 기본 파일 설치
RUN apt-get install -y curl vim wget build-essential


RUN apt-get install -y locales
RUN locale-gen ko_KR.UTF-8
ENV LANG en_US.UTF-8
ENV PYTHONIOENCODING=UTF-8
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./dir1/dir2 /code/
COPY ./dir1 /code/dir2
