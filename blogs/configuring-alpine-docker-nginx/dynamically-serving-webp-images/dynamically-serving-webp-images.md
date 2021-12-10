# Overview

In this article, I will describe what's required to enable for NGINX to dynamically serve .webp images from existing static image assets.

## HTTP Image Filter Module

[Read more documentation about ngx_http_image_filter_module.](http://nginx.org/en/docs/http/ngx_http_image_filter_module.html)

There is an existing module available for NGINX that can be used for serving .webp images from existing .jpeg, .png, and even .gif image assets from the server itself, as opposed to converting the images ahead of time and storing them alongside the original version.

## WebP Command-line Tooling

If you're not interested in using the ngx_http_image_filter module, the alternative is to use the readily available .webp command-line interface tooling available from Google's website, and injecting a `map` operator as part of your server's configuration.

Refer to the configuration sample below for more information.

```nginx
map $http_accept $webp_suffix 
{
  default   "";
  "~*webp"  ".webp";
}

...

server 
{
  listen 443 ssl http2;
  listen [::]:443 ssl http2;
  server_name ${WEBSITE_DOMAIN_NAMES};
  server_tokens off;
  charset utf-8;

  location ~* /assets/.+\.(?<extension>jpe?g|png|gif|webp)$ 
  {
    gzip_static on;
    gzip_types image/png image/x-icon image/webp image/svg+xml image/jpeg image/gif;

    add_header Vary Accept;
    expires max;
    sendfile on;
    try_files "${request_uri}${webp_suffix}" $uri =404;
  }

}

```