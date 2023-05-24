FROM quay.io/strimzi/kafka:0.34.0-kafka-3.4.0
USER root:root
RUN curl https://d1i4a15mxbxib1.cloudfront.net/api/plugins/confluentinc/kafka-connect-elasticsearch/versions/14.0.6/confluentinc-kafka-connect-elasticsearch-14.0.6.zip -o confluentinc-kafka-connect-elasticsearch-14.0.6.zip
RUN unzip confluentinc-kafka-connect-elasticsearch-14.0.6.zip && mv confluentinc-kafka-connect-elasticsearch
RUN ls -l /opt/kafka/plugins/
COPY confluentinc-kafka-connect-elasticsearch/ /opt/kafka/plugins/
RUN ls -l /opt/kafka/plugins/
USER 1001
