# Publisher

A command-line Python tool that is responsible for exporting and publishing articles that are authored in Markdown format.

## Platforms

Find below the number of platforms that are currently supported.

- **Hashnode**
  - **Website:** [https://hashnode.com/](https://hashnode.com/)
- **Dev.to**
  - **Website:** [https://dev.to/](https://dev.to/)
- **Silverstripe**
  - **Website:** [https://silverstripe.org](https://www.silverstripe.org/)

## Uploaders

An "Uploader" is a Python type responsible for uploading a blog to a target platform after it has been rendered or rasterized. It forms part of a pipeline for rendering and ultimately publishing the blog content to the platform specified.

## Exporters

An "Exporter" is a Python type responsible for rendering or producing file in another format from Markdown source.

- **PDF**
  - Render a PDF document form a Markdown source file. The rendered output is customizable with various parameters.
- **HTML**
  - Render a HTML page or collection of pages from a Markdown source file.
- **Silverstripe (HTML)**
  - Renders the Markdown source file as a HTML page, with syntax highlighting and image assets available. Supports the [silverstripe/blog](https://addons.silverstripe.org/add-ons/silverstripe/blog) module.

## Structure

This tool manages blog posts or articles by placing them into "collections". A "collection" can be considered as a series of related blog posts. They are synonymous with a book whereby a "chapter" from a book represents a single blog post or article.

### Example

Insert example here.

## Usage

This tool is installable from PyPi by running the following command.

```bash
#!/bin/bash

pip install publisher
```

The tool should then be usable from the command-line by running the following.

### Creating a Blog Collection

```bash
#!/bin/bash

python -m publisher collections create <collection name>
```

Alternatively, the same command can be expressed as the following.

```bash
#!/bin/bash

publisher collections create <collection name>
```

```bash
#!/bin/bash

publisher collections list
```

### Images

Images are automatically uploaded to image sharing websites should there be configured API keys.

### Configuration

The default configuration file is found under `publisher/data/config/default.ini`.
