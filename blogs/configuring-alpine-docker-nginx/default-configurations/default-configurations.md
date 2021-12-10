# Overview

[The original version of this article can be found on my blog.](https://lucshelton.codes/blog)

In this blog post, we are going to discuss the importance of having a suitable default configuration that is capable of responding to requests to unsupported domains.

Using myself as an example, I recently encountered a problem when I had multiple domain names with **CNAMES** pointing at the same host as my other domain names that I use for my portfolio. For instance, I had `domain-name-one.com` pointing to the same web server as `domain-name-two.com`. In reality, I only wanted one domain to be served which was `domain-name-two.com`. However, because there was no suitable default configuration being applied by NGINX, it attempted to serve the request anyway and redirecting the traffic to my (unrelated) portfolio website.

Find below a small flowchart diagram of the problem.

## The Impact on SEO Rankings

Failing to address the aforementioned problem can cause for your SEO ranking to tank, as Google will struggle to determine which URLs are considered to be  the canonical URL, even though both domains are pointing to the same host.

---

## Project Layout

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
        └── domain-name-two.com
```

## Default Configuration

This section outlines potential ideas for a suitable default configuration

### Error Pages

Serving error pages.

### Notes

- `server_tokens` informs NGINX whether or not to respond to request with a header indicating what type of webserver is responding to requests.

Find below the complete default configuration for NGINX.

```nginx
server
{
    listen  80 default_server;
    listen  [::]:80 default_server;
    listen  443 ssl default_server;
    listen  [::]:443 ssl default_server;
    server_tokens           off;
    server_name_in_redirect off;
    server_name             default_server;

    charset utf-8;

    access_log  /var/log/nginx/host.access.log  main;
    error_log  /var/log/nginx/host.error.log  warn;

    ssl_certificate /etc/nginx/ssl-default/default-fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl-default/default-privkey.pem;

    root   /var/www/default;
    index  index.html index.htm;

    location ~* ^.+ 
    {
        try_files $uri $uri/ =404;
    }

    location / 
    {
        try_files $uri $uri/ =404;
    }

    error_page 404 /404.html;
    error_page 403 /403.html;
    location = /404.html 
    {
        root   /var/www/default;
    }

    error_page  500 502 503 504 /500.html;
    location = /500.html 
    {
        root   /var/www/default;
    }
}
```