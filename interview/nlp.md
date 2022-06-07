# https://wikidocs.net/31379

머신러닝과 딥러닝의 차이가 무엇인가요?
- 심층 신경망을 학습시킨다고 하여, 딥 러닝(Deep Learning)

머신러닝의 주요 작업
데이터 수집 -> 데이터 분석(탐색) / EDA와 시각화 -> Feature Engineering -> 모델링 -> 예측

# 딥러닝 학습시 설정했던 주요 파라미터
1. 어떤 모델을 쓸 것인가
- 사이즈(keelectra는 사이즈가 상대적으로 작음, )

2. max_len
- 데이터 길이 구한 후 패

3. LR = 3e-5
- 학습 보폭
- Adamizer를 사용

• Tokenizaiton (Word & Sentence) : 단어와 문장의 경계
• Cleaning & Normalization
• Stopwords (필요없는 데이터 제거)
• Build your vocabulary
• Integer Encoding (컴퓨터가 인식할 수 있는 수자로 변환)
• Padding (단어의 길이 조정)
• Vectorization (원-핫인코딩->TF-IDF, 워드임베딩, BERT)

# 원핫인코딩
- 원핫인코딩 : 차원이 매우 커진다.

# Linear Regression
- y = wx + b
- '평균 제곱 오차'. 실제값과 예측값에 대한 오차
- 인공 신경망은 기본적으로 Cost function을 최소화하는 w와 b를 찾는 것이 목적!
- 옵티마이저 알고리즘 사용. 

- activation: sigmoid(0, 1)
- Logistic Regression
- BinaryCrossEntroypy()
- Softmax Regression : 다중분류

# Attention
- 하나의 문장 내 단어들 간 유사도를 구하므로서 어텐션을 수행
• 입력 문장의 길이와 상관없이 고정된 크기의 벡터에 정보를 모두 압축한다.
• 고정된 크기의 벡터에 정보가 다 압축되지 않아 정보 손실이 발생. (Bottleneck)
• RNN 계열의 고질적인 장기 의존성 문제로 초기 정보가 손실되며 전달.
Attention(Q, K, V) = Attention Value
- 

# BERT(Bidirectional Encoder Representations from Transformers)
- Word2Vec
- 문제점 : 문맥을 고려하지 못 하여 다의어나 동음이의어를 구분하지 못한다.
- 다른 작업에 대해서 파라미터 재조정을 위한 추가 훈련 과정을 파인 튜닝(Fine-tuning)이라고 합니다.
- 학습시 신경망의 파라미터가 조정이 됨. (x * w + b)의 식으로 정의되며, weight들이 재조정 됨.
