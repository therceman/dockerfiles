FROM maven:3-jdk-8

ENV MAVEN_OPTS="-Xms256m -Xmx512m"
ENV OPENSSL_CONF="/etc/ssl/"

RUN apt-get update && apt-get install dos2unix

COPY src /src
COPY script /script

RUN dos2unix /script/fg-run-annotate.sh \
    && dos2unix /script/fg-run-user-repository.sh \
    && dos2unix /script/fg-run-repository.sh \
    && dos2unix /script/fg-run-leos.sh \
    && dos2unix /script/fg-run-akn4euutil.sh

RUN chmod +x /script/fg-run-annotate.sh \
    && chmod +x /script/fg-run-user-repository.sh \
    && chmod +x /script/fg-run-repository.sh \
    && chmod +x /script/fg-run-leos.sh \
    && chmod +x /script/fg-run-akn4euutil.sh

WORKDIR /src

RUN cd ./modules/annotate && mvn clean install -Dmaven.test.skip=true
