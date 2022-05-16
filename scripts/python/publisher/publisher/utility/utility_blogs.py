import re
import datetime
from typing import Tuple

def get_formatted_timestamp() -> str:
    return datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%y_%H-%M-%S')

def create_slug_from_name(blog_name: str):
    if blog_name is None or not blog_name:
        raise ValueError("The blog name defined is invalid or null")

    formatted = re.sub('[^a-zA-Z\_\-0-9]+', '-', blog_name)
    if formatted is None or formatted == '':
        raise ValueError("The formatted slug name is invalid or null")
    return formatted.lower()

def create_blog(blog_name: str):  # sourcery skip: raise-specific-error
    
    if blog_name is None:
        raise Exception("The name of the blog is invalid or null")
    pass

def create_blog_collection(blog_collection_name: str):
    # sourcery skip: raise-specific-error
    if blog_collection_name is None:
        raise Exception("The collection name is invalid or null")

def get_blog_collections() -> Tuple:
    return

def get_blogs(blog_collection_name: str) -> Tuple:
    return