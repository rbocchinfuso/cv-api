FROM alpine:latest
MAINTAINER Richard Bocchinfuso "rbocchinfuso@gmail.com"
RUN apk add --update \
    python3 \
    python3-dev \
    py3-pip \
    build-base \
  && rm -rf /var/cache/apk/*

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /app
ADD ./cv.json /app
ADD ./config.ini /app
ADD ./cv-api.py /app
ADD ./requirements.txt /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["cv-api.py"]
