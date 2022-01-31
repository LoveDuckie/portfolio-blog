# Overview

[The original version of this article can be found on my blog.](https://lucshelton.codes/blog)

This blog will cover what's required for customizing the startup behaviour of the Alpine Linux Docker container image for NGINX. When the container starts, it will automatically run a collection of scripts for processing configuration "templates" using a tool called `envsubt` and placing the resulting output under a directory named `/etc/conf.d`.

## Project Layout

Find below the approximate project layout for this blog post.


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
        └── lucshelton.com
```

## Modifying NGINX Container Image

The container image runs a collection of scripts that are located under `/docker-entrypoint.d/` in the container image's filesystem. They all have executable permissions and are owned by `root` user. The scripts are sorted by name, and executed sequentially

The best approach to modifying the startup routine is to update the Dockerfile for the container image, and create a separate root level directory called `/docker-entrypoint-ext.d/` that will contain your collection of scripts to run.

These scripts will be executed by another script that will be placed in the original `/docker-entrypoint.d/`. You can consider this script to be an "injection point" for your other scripts. This approach is more convenient because it means that you can test modifications to scripts found in `/docker-entrypoint-ext.d/` without interfering with any of the vendor supported scripts that are already in `/docker-entrypoint.d/`.

```Dockerfile


```

```shell


```

---

I hope you found this blog post useful! Let me know if you think there should be improvements by opening an issue on GitHub.

 **Follow me on Twitter:** [@TheLoveDuckie](https://twitter.com/theloveduckie)