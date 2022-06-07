FROM elasticsearch:7.9.3

### 노리 설치
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch analysis-nori

### 사전 추가하기
WORKDIR /usr/share/elasticsearch/config
RUN mkdir analysis
COPY analysis /usr/share/elasticsearch/config/analysis/

