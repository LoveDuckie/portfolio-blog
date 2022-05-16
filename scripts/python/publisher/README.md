# Publisher

A command-line Python tool that is responsible for exporting and publishing articles that are authored in Markdown format.

## Platforms

Find below the number of platforms that are currently supported.

- **Hashnode**
- **Dev.to**
- **Silverstripe**

## Structure

This tool manages blog posts or articles by placing them into "collections". A "collection" can be considered as a series of related blog posts. They are synonymous with a book whereby a "chapter" from a book represents a single blog post or article.

### Example

Insert example here.

## Usage

This tool is installable from PyPi by running the following command.

```shell
#!/bin/bash

pip install publisher

```

The tool should then be usable from the command-line by running the following.

### Creating a Blog Collection

```shell
#!/bin/bash

python -m publisher collections create <collection name>

```

### Images

Images are automatically uploaded to image sharing websites should there be configured API keys.

### Configuration