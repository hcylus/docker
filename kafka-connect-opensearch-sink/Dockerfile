FROM quay.io/strimzi/kafka:0.34.0-kafka-3.4.0
USER root:root
RUN curl --connect-timeout 600 https://github.com/aiven/opensearch-connector-for-apache-kafka/releases/download/v3.0.0/opensearch-connector-for-apache-kafka-3.0.0.zip -o opensearch-connector-for-apache-kafka-3.0.0.zip
RUN mkdir -p plugins/opensearch-connector-for-apache-kafka 
RUN ls -l && mv opensearch-connector-for-apache-kafka-3.0.0.zip plugins/opensearch-connector-for-apache-kafka
RUN cd plugins/opensearch-connector-for-apache-kafka && ls -l && unzip opensearch-connector-for-apache-kafka-3.0.0.zip && rm -f opensearch-connector-for-apache-kafka-3.0.0.zip
USER 1001
