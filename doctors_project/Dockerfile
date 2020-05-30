FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    python-dev \
    python-pip \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev

RUN pip install \
    --upgrade pip \
    scrapy \
    psycopg2-binary

COPY . .

RUN chmod +x /wait-for-it.sh


