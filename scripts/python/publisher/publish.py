"""
    Publish

    A simple script for publishing and exporting blogs that are stored in this repository.
"""
import os, sys, logging
import argparse
from typing import Any
import json
import datetime

def get_default_blogs_path():
    """Get the default path for where logs are stored

    Returns:
        string: The absolute path to where the logs are stored.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..","..","blogs"))

arg_parser = argparse.ArgumentParser(description='Publish or export blogs')
arg_parser.add_argument('--action', dest='action', type=str, help='The action to perform (publish, export etc.)', default='list')
arg_parser.add_argument('--blog-series', dest='blog_series', type=str, help='The slug name for the blog series', default=None)
arg_parser.add_argument('--blog', dest='blog', type=str, help='The specific blog we wish to interact with', default=None)
arg_parser.add_argument('--blogs-path', dest='blogs_path', type=str, required=False, help='The relative or absolute path to where the blogs are located', default=get_default_blogs_path())
arg_parser.add_argument('--debug', required=False, type=bool, help='Enable debugging.', default=None)

parsed_args = arg_parser.parse_known_args()

if parsed_args is None:
    raise ValueError("The parsed arguments are invalid or null")

for path in os.walk(os.path.join(get_default_blogs_path(), "nginx")):
    print(path)

logger = logging.Logger(name='publish-log')
logger.addHandler(logging.FileHandler(filename='publish-log'))
logger.addHandler(logging.ConsoleHandler())

if parsed_args.debug:
    logger.setLevel(logging.DEBUG)

logger.info("Test")



class BlogSeries(object):
    
    def __init__(self, **kwargs) -> None:
        super().__init__()

    @classmethod
    def get_series(cls,blogs_path):
        return

def list_all_blogs():
    if parsed_args is None:
        raise Exception("The parsed arguments are invalid or null")
    return

def list_all_series():
    if parsed_args is None:
        raise Exception("The parsed arguments are null or invalid")
    
    return

def publish_blog():
    return

def get_all_series():
    return

def export_blog():
    return

def get_all_blogs_from_series(series_slug_name):
    return

actions = {
    'list' : list_all_blogs,
    'publish' : publish_blog,
    'export' : export_blog
}

def main(args):
    
    return

if __name__ == "__main__":
    main(sys.argv)