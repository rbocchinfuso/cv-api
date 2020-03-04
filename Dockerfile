FROM alpine:latest
MAINTAINER Richard Bocchinfuso "rbocchinfuso@gmail.com"
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*
COPY config.ini /app
COPY cv-api.py /app
COPY cv.json /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["cv-api.py"]

