# 머신러닝과 딥러닝의 차이점에 대해 설명해주세요.

딥러닝은 머신러닝의 하위 개념으로써,
머신러닝과 딥러닝 모두 데이터를 통해 패턴을 학습하고, 결과를 추론한다는 점은 같습니다. 

- 수시로 변하는 업무 환경, 정책, 사용자의 성향에 따른 애플리케이션 구현의 어려움
- 예측 정확성의 문제
- 여러 특징(feature)들을 if else로 찾기 어렵다.


# 머신러닝
- 주로 사용하는 알고리즘 : 결정 트리, 랜덤 포레스트, GBM
- if-else의 규칙성을 찾는데 특화됬다.
- 데이터를 선형으로 나눌 수 있는 데, 수치적으로 측정이 된 데이터들에 대해서는 머신 러닝을 쓰는 것이 적합하고
- 사용자들의 feature을 추출해서 추천해주는 추천 시스템에도 쓰이는 것으로 알고 있다.

# 딥러닝
- 데이터의 관계가 비선형적으로 맺어진 관계를 예측할 때 쓰인다.
- PyTorch, Tensorflow등을 활용하여 예측을 진행한다.
- NLP, Vision, Voice와 같이 데이터들의 관계를 특정하기 힘든 경우 딥러닝을 활용한다.


# 딥러닝을 제 업무에 왜 적용했느냐
- "팔이 아파"라고 했을 경우, "팔", "아프다" 로 사용자 관심사를 추출
- 뉴스 데이터, TTS가 잘못된 경우(TTS의 정확도는 보통 65%정도 기록)에 대해서 매번 규칙을 추가할 수 없음.
- 앞에 안이 있냐, 아니면 특정 키워드가 있냐 등으로 추가하기에는 거의 무한한 규칙을 추가해야 된다고 판단.
- 따로 계속 공부했던 것에 업무에 적용.

# 머신러닝 작업 순서
1. 데이터 수집
2. 데이터 분석(탐색) - EDA 데이터의 feature을 찾아내서 추가하는 것이 중요.
3. Feature Engineering
4. 모델링
5. 예측
