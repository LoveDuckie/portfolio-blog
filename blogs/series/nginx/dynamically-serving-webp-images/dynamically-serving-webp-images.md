# Dynamically Serving WebP Images

In this article, I will describe what's required to enable for NGINX to dynamically serve `.webp` images from existing static image assets saved in other file formats.

## What is WebP?

Quoted from the Google Developer documentation:

> WebP is a modern image format that provides superior lossless and lossy compression for images on the web. Using WebP, webmasters and web developers can create smaller, richer images that make the web faster.
>
> WebP lossless images are 26% smaller in size compared to PNGs.

In short, `.webp` is a highly-optimized and efficient file format that is widely supported by most modern browsers. In addition, web-tooling like Google PageSpeed Insights rank websites favourably if they render or serve image assets that are using the `.webp` file format, which can be beneficial for search-engine rankings.

## HTTP Image Filter Module

[Read more documentation about ngx_http_image_filter_module.](http://nginx.org/en/docs/http/ngx_http_image_filter_module.html)

There is an existing module available for NGINX that can be used for serving `.webp` images from existing `.jpeg`, `.png`, and even `.gif` image assets from a configured directory, as opposed to converting the images ahead-of-time and storing them alongside their original counterparts.

## WebP Command-line Tooling

You might find in some instances that it's not possible to compile the required  `ngx_http_image_filter` module - possibly because of constraints relating to security. The alternative is to use the readily available `.webp` command-line interface tooling available from Google developer's website, and injecting a `map` operator as part of your server's NGINX configuration.

### Automating WebP Image Creation

Refer to the Python code below for automating the creation of `.webp` files from existing image assets.

```python
import os, sys

def main(argv):
  return


if __name__ == "__main__":
  exit 1

```

Click here to view the repository for this automated tooling, along with required packages.

---

What this configuration does instead the following

1. Detect any incoming requests for a static file asset with a .jpeg, .jpg, .gif, or .png extension.
2. Modify the response, and append the .webp file extension to the request string.
3. Attempt to serve the .webp version of the requested image asset. Return the original if it is not found (Refer: `try_files`).

To achieve this, we must use a feature in NGINX called the `map` operator, which is a operator used within configuration files for defining variables based on the value of another variable.

You could consider this `map` operator to be similar to a `switch` statement in most popular programming languages - based upon a specified parameter, it will return another value if a predefined condition is met.

Refer to the configuration sample below as an example.

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
  server_name your-domain-name.com;
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

The `location` block will be used if the incoming request is for an image that matches one of the specified image file extensions. In this case, it is either .`jpeg`, `.jpg`, `.png`, or `.gif`.

## Applying GZip compression

In addition to serving optimized versions of image file assets, you can also apply another layer of optimization (i.e. reduced transfer size) by enabling gzip compression. This is a mode of transport that is supported by most modern browsers and popular webservers (including in this instance, NGINX).

## Conclusion

If you are conducting an optimization audit of your website or web application, there's no reason to not consider using `.webp` as part of your tech stack. Better yet, if you are using a SPA framework (Single-Page Application) and serving it through a web server like NGINX, you don't have to modify or rip apart your code to achieve this optimization. 

---

I hope you found this blog post useful! Let me know if you think there should be improvements by opening an issue on GitHub.

 **Follow me on Twitter:** [@TheLoveDuckie](https://twitter.com/theloveduckie)