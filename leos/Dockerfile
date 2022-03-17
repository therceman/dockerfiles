FROM maven:3-jdk-8

ENV MAVEN_OPTS="-Xms256m -Xmx512m"
ENV OPENSSL_CONF="/etc/ssl/"

RUN apt-get update
RUN apt-get install -y libfontconfig1 fontconfig libfontconfig1-dev libfreetype6-dev

COPY src /src
COPY script /script

RUN ["chmod", "+x", "/script/fg-run-annotate.sh"]
RUN ["chmod", "+x", "/script/fg-run-user-repository.sh"]
RUN ["chmod", "+x", "/script/fg-run-repository.sh"]
RUN ["chmod", "+x", "/script/fg-run-leos.sh"]
RUN ["chmod", "+x", "/script/fg-run-akn4euutil.sh"]

WORKDIR /src

RUN cd ./modules/annotate && mvn clean install -Dmaven.test.skip=true
