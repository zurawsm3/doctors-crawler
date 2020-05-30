FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    libreoffice-base \
    default-jre

COPY postgresql-42.2.4.jar postgresql-42.2.4.jar

CMD ["/usr/bin/libreoffice"]



