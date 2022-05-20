
# 동작 로직

1. 로직 1 설명
2. 로직 2 설명
3. 로직 3 설명

# API document

RequestAPI:

- chat_middleware 컨테이너 -> chat_api_mrc 컨테이너에 응답 요청
- chat_objects의 하나씩 받음

| 파라미터                 | 타입        | 필수여부 | 설명        |
|----------------------|-----------|------|-----------|
| test_param1          | string    | N    | 설명1       |
| test_param2          | boolean   | Y    | 설명2       |
| req 속성               | -         | -    | -         |
| user_id              | string    | Y    | 설명3       |
| user_ip              | ip        | Y    | 설명4       |
| system_response_time | timefield | Y    | 시스템 요청 시간 |


ResponseAPI:


| 파라미터                 | 타입        | 필수여부 | 설명          |
|----------------------|-----------|------|-------------|
| system_response_time | timefield | Y    | 시스템 응답 시간   |