"""기본 로그 포맷

ref : https://docs.python.org/ko/3/howto/logging.html

# 활용 빈도가 높은 로그 포맷
- %(asctime)s.%(msecs)03d 언제 수행됬는지 정확히 알기 위해 필요.
- (levelname)s 내가 의도한 레벨인지 알기 위해 필요.
- (name)s 어디에서 일어난 에러인지 알기 위해 필요
- (message)s 실제 에러 메시지

# 로그 레벨 실제 활용시
- critical : 그냥 Exeception에서 처리. 무조건 봐야하는 에러.
  - 자다가도 뜨면 바로 확인해야 하는 정보
- error : 사용자 정의 Exception에서 사용. 소프트웨어 일부 기능이 수행되지 않을 수 있음.
  - 일하고 있는데 다른 팀에서 요청할 수 있는 에러 정보
- warning : 소프트웨어는 여전히 예상대로 작동합니다.
  - 매일 아침마다 확인해 봐야 하는 에러
- info : 사용자 접근 기록 등에 활용하는 정보
  - 모든 팀원이 필요시마다 확인하는 정보
- debug : 개발시 함수 출력값에 사용
  - 나만 알아도 되는 정보

# 로그 활용 팁
- 로그 포맷은 딕셔너리 형태로 저장
  - 향후 로그 파싱하기 편리하다.
"""

import logging

formatter = "%(asctime)s.%(msecs)03d\t%(levelname)s\t[%(name)s]\t%(message)s"
logging.basicConfig(level=logging.DEBUG, format=formatter, datefmt='%m/%d/%Y %I:%M:%S')

if __name__ == "__main__":
    logging.critical({'message': 'critical'})
    logging.error({'message': 'error'})
    logging.warning({'message': 'warning'})
    logging.info({'message': 'info'})
    logging.debug({'message': 'debug'})
