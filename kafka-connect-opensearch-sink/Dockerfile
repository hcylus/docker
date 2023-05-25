FROM quay.io/strimzi/kafka:0.34.0-kafka-3.4.0
USER root:root
RUN mkdir -p /opt/kafka/plugins/opensearch-connector-for-apache-kafka && cd /opt/kafka/plugins/opensearch-connector-for-apache-kafka && curl https://github.com/aiven/opensearch-connector-for-apache-kafka/releases/download/v3.0.0/opensearch-connector-for-apache-kafka-3.0.0.zip -o opensearch-connector-for-apache-kafka-3.0.0.zip && unzip opensearch-connector-for-apache-kafka-3.0.0.zip && rm -f opensearch-connector-for-apache-kafka-3.0.0.zip
USER 1001
