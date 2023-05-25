FROM quay.io/strimzi/kafka:0.34.0-kafka-3.4.0
USER root:root
RUN curl https://github.com/aiven/opensearch-connector-for-apache-kafka/releases/download/v3.0.0/opensearch-connector-for-apache-kafka-3.0.0.tar -o opensearch-connector-for-apache-kafka-3.0.0.tar
RUN mkdir -p /opt/kafka/plugins/opensearch-connector-for-apache-kafka && tar xf opensearch-connector-for-apache-kafka-3.0.0.tar -C /opt/kafka/plugins/opensearch-connector-for-apache-kafka && rm -f opensearch-connector-for-apache-kafka-3.0.0.tar
USER 1001
