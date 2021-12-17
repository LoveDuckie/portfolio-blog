"""
    Publish

    A simple script for publishing and exporting blogs that are stored in this repository.
"""
import os, sys
import argparse
from typing import Any
import json

arg_parser = argparse.ArgumentParser(description='')
arg_parser.add_argument('action', type=int, help='The action to perform (publish, export etc.)', default='list')
arg_parser.add_argument('blog-series', type=str, help='The slug name for the blog series', default=None)
arg_parser.add_argument('blog', type=str, help='The specific blog we wish to interact with', default=None)
arg_parser.add_argument('blogs-path', type=str, help='The relative or absolute path to where the blogs are located', default=None)

parsed_args = arg_parser.parse_known_args()

if parsed_args is None:
    raise ValueError("The parsed arguments are invalid or null")

actions = {
    'list' : lambda x : print("something"),
    'publish' : lambda x : print("something"),
    'export' : lambda x : print("something")
}

class Blog(object):
    def __init__(self, blog_name, blog_slug='', blog_description='') -> None:
        self.properties = {}
        super().__init__()

    @property.getter
    def blog_name():
        return
    
    @property.getter
    def blog_slug():
        return

    @property.getter
    def blog_description():
        return

    def __getattribute__(self, __name: str) -> Any:
        return super().__getattribute__(__name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        return super().__setattr__(__name, __value)

    def __getitem__(self, key):
        return self.__dict__[key]

class BlogSeries(object):
    
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_series(cls,blogs_path):
        return

def list_all_blogs():
    return

def list_all_series():
    return

def publish_blog():
    return

def get_all_series():
    return

def get_all_blogs_from_series(series_slug_name):
    return

def main(args):
    return

if __name__ == "__main__":
    main(sys.argv)