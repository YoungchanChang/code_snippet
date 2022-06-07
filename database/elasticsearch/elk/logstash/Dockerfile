FROM docker.elastic.co/logstash/logstash:7.9.3
RUN rm -f /usr/share/logstash/pipeline/logstash.conf
ADD pipeline/ /usr/share/logstash/pipeline/
ADD config/ /usr/share/logstash/config/
COPY mysql-connector-java-8.0.16.jar /usr/share/logstash/mysql-connector-java-8.0.16.jar