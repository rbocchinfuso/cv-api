---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
marp: true
---

![bg left:40% 80%](https://www.pinclipart.com/picdir/big/379-3792862_resume-rsum-clipart.png)

# **My CV API**

A DevOps Project
By: Rich Bocchinfuso

- [GitHub Repo](https://github.com/rbocchinfuso/cv-api)
- [Project Blog](http://gotitsolutions.org/2020/02/06/dominate-thy-destiny/)
- [This Preso-as-Code](https://github.com/rbocchinfuso/cv-api/blob/master/CV-PRESO.md)

---

# My Pipeline

![width:30cm height:12cm](./assets/img/mypipeline-v2.png)

---

# Why

![bg left:30% 80%](https://i.pinimg.com/originals/eb/f2/ee/ebf2eeffb64eb76b902a1aa574c9c413.png)

- Just **for fun**
- Because **I can**
- Inflight **boredom** and shitty United WiFi
- Because we **learn by doing**
- Because we live in an **API driven world**
- Because my dad taught me to not expect others to do things you can't do yourself

---

# How

![bg left:30% 80%](https://miro.medium.com/max/2404/1*-fv9rPMKmVNuZZbaJltKag.png)

- **Create** a JSON structure for CV details
- **Build** API with Python and Flash
- **Package** and containerize API
- **Test and document** the API with Postman
- **Document** with a good README.md
- **CI/CD** pipeline
- **Test** with lgtm, sonararcloud, loader.io
- **Instrument and monitor** with Sentry, Prometheus and Grafana

---

# Project Overview

![bg left:30% 90%](https://imgur.com/2GBz7F1.jpg)

- [**config.ini**](https://github.com/rbocchinfuso/cv-api/blob/master/config.ini): Config params; typically excluded from commit with .gitignore
- [**cv-api.py**](https://github.com/rbocchinfuso/cv-api/blob/master/cv-api.py): The applicaiton
- **cv.json**: JSON file containing CV details
- [**CV-PRESO.md**](https://github.com/rbocchinfuso/cv-api/blob/master/CV-PRESO.md): Presentation-as-code :wink:
- [**docker-compose.yml**](https://github.com/rbocchinfuso/cv-api/blob/master/docker-compose.yaml): File that constructs applicaiton infrastucture
- [**Dockerfile**](https://github.com/rbocchinfuso/cv-api/blob/master/Dockerfile): Build app container
- [**README.md**](https://github.com/rbocchinfuso/cv-api/blob/master/README.md): Documentation

---

# CV in JSON

![bg left:30% 70%](https://cdn.iconscout.com/icon/free/png-512/json-file-1-504451.png)

```JSON
{
  "basics": {
    "name": "Richard Bocchinfuso",
    "label": "Engineering Leader",
    "picture": "https://www.amazon.com/photos/...",
    "email": "rbocchinfuso@gmail.com",
    "phone": "(732) 713-5671",
    "website": "http://bocchinfuso.net",
    "summary": "As a passionate and dedicated...",
    "location": {
      ...
      "region": "Northeast"
    },
    ...
  }
  ```

---

# Dockerfile Explained

![bg left:30% 70%](https://developers.redhat.com/sites/default/files/styles/article_feature/public/blog/2014/05/homepage-docker-logo.png?itok=zx0e-vcP)

Pull Alpline Linux image, update and install Python (JeOS)

```Dockerfile
FROM alpine:latest
MAINTAINER Richard Bocchinfuso "rbocchinfuso@gmail.com"
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*
```

---

# Dockerfile Explained Cont'd

<!-- ![bg left:30% 70%](https://developers.redhat.com/sites/default/files/styles/article_feature/public/blog/2014/05/homepage-docker-logo.png?itok=zx0e-vcP) -->


Copy app code into container.

```Dockerfile
RUN mkdir -p /app
ADD ./cv.json /app
ADD ./config.ini /app
ADD ./cv-api.py /app
ADD ./requirements.txt /app
```

---

# Dockerfile Explained Cont'd

<!-- ![bg left:30% 70%](https://developers.redhat.com/sites/default/files/styles/article_feature/public/blog/2014/05/homepage-docker-logo.png?itok=zx0e-vcP) -->

Set app directory, install requirements, start application.

```Dockerfile
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["cv-api.py"]
```

---

# Docker Compose Explained

Starts NGINX contianer for reverse proxy

![bg left:30% 80%](https://miro.medium.com/max/700/1*s8I4jBW2KKP687LqWh3OtQ.png)


```Dockerfile
services:
  nginx-proxy:
    restart: always
    image: jwilder/nginx-proxy
    container_name: nginx-proxy
    ports:
      - "80:80"
    volumes:
      - /var/run/docker.sock:/tmp/docker.sock:ro
```

---

# Docker Compose Explained Cont'd

Starts CV API container and application

```Dockerfile
cv-api:
#   build: ./
    restart: always
#   image: local/cv-api
    image: rbocchinfuso/cv-api:latest
    container_name: cv-api
#    ports:
#     - "5000:5000"
    expose:
     - "5000"
    volumes:
     - .:/code
```

---

# Docker Compose

Registered with NGINX proxy as reverse proxy address

```Dockerfile
environment:
     - VIRTUAL_HOST=cv.bocchinfuso.net
```

Private network on which NGINX communicates with CV API

```Dockerfile
networks:
  default:
    external:
      name: nginx-proxy
```

---
# Nginx Reverse Proxy

![bg left:30% 80%](https://iconape.com/wp-content/png_logo_vector/nginx.png)

docker-compose automagically registers the virtual host with the Nginx container

```json
server {
  listen 80;
  listen [::]:80;

  server_name cv.bocchinfuso.net;

  location / {
      proxy_pass http://localhost:5000/;
  }
}
```

---

# What

![bg left:30% 100%](https://www.lightcastlebd.com/wp-content/uploads/2014/09/Lean-StartUp.png)

- **Deploy NGINX** container and expose port 80
- **Build and deploy cv-api** container from source
- **Expose port 5000 to NGINX** revese proxy
- **Register** virtual hostname "cv.bocchinfuso.net"
- Allow user with bearer token make a CV API REST calls

---

# Demo Time

![bg left:30% 190%](https://media.istockphoto.com/vectors/video-tutorial-concept-vector-id899153838?k=6&m=899153838&s=612x612&w=0&h=Dd9ngL7Bc6x9Mynx7Fho6Rt-dWNZ4OipdpqD7PH_-h4=)

## :grin: Release the Kraken! :grin:

- Test API Request: http://bit.ly/2wA1Ykw

- Read full API docs: http://bit.ly/2v1b35G


---

# Appendix

![bg left:30% 80%](https://icon-library.com/images/markdown-icon/markdown-icon-28.jpg)

- Project Timeline: It's my lifestyle.
- [This Preso-as-Code](https://github.com/rbocchinfuso/cv-api/blob/master/CV-PRESO.md)
- [CV API Trello Board](http://bit.ly/2PTC3uX)

_Note: [GitPitch](https://gitpitch.github.io/gitpitch/#/) is gone :cry:,  so I had to refactor [PITCHME.MD](https://github.com/rbocchinfuso/cv-api/PITCHME.md), which I did using [Marp](https://marp.app/)._
