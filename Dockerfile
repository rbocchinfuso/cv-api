FROM alpine:latest
MAINTAINER Richard Bocchinfuso "rbocchinfuso@gmail.com"
RUN apk add --update \
    python3 \
    python3-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*
RUN mkdir -p /app
ADD ./cv.json /app
ADD ./config.ini /app
ADD ./cv-api.py /app
ADD ./requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["cv-api.py"]
