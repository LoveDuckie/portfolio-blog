# Overview

[The original version of this article can be found on my blog.](https://lucshelton.codes/blog)

In this article, we're going to discuss what is required for installing the [Headers More module](https://www.nginx.com/resources/wiki/modules/headers_more/) for NGINX with the Alpine Docker image.

The [Headers More](https://www.nginx.com/resources/wiki/modules/headers_more/) module enables you to write server configurations that omit or modify response headers before they are served back to the user.

---

Your `docker-compose` project is going to need to look a little like this.


```shell
.
├── containers
│   └── nginx
│       ├── build
│       │   └── Dockerfile
│       ├── configuration
│       │   ├── certificates
│       │   ├── default
│       │   ├── environments
│       │   ├── nginx.conf
│       │   ├── robots.txt
│       │   ├── snippets
│       │   └── templates
│       ├── pages
│       │   ├── 403.html
│       │   ├── 404.html
│       │   ├── 500.html
│       │   ├── bootstrap
│       │   ├── index.html
│       │   └── jquery
│       └── scripts
│           └── entrypoint
├── development.yaml
├── docker-compose.yaml
├── production.yaml
└── source
    └── sites
        └── domain-name-one.com
```
---

## Alpine Docker

There are a few variants of the NGINX Docker container image, depending on which flavour of Linux you wish to concern yourself with. This blog will focus on Alpine Linux, has it consumes the least amount of memory, and less space on disk because of its smaller image size.

## Compiling Headers More

We will focus on compiling the module from source using a separate build stage for achieving this. Upon compiling the module in this build stage, we will then copy the compiled contents into the latter parts of the build.


```Dockerfile
ARG NGINX_VERSION 1.20.1
ARG NGINX_HEADERS_MORE_VERSION 0.33

FROM nginx:${NGINX_VERSION}-alpine AS nginx-builder

ARG NGINX_VERSION 1.20.1
ARG NGINX_HEADERS_MORE_VERSION 0.33

# APK Community Packages
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community/ >> /etc/apk/repositories

RUN apk update
RUN apk add --no-cache --update shadow

# NGINX Headers More
RUN wget "https://github.com/openresty/headers-more-nginx-module/archive/v${NGINX_HEADERS_MORE_VERSION}.tar.gz" -O headers-more.tar.gz

RUN apk add --no-cache --virtual .build-deps \
  git \
  gcc \
  libc-dev \
  make \
  openssl-dev \
  pcre-dev \
  zlib-dev \
  linux-headers \
  curl \
  gnupg \
  libxslt-dev \
  gd-dev \
  geoip-dev

```

The above `Dockerfile` is considered to be the base image that we are going to copy the compiled module for `headers-more` from.
