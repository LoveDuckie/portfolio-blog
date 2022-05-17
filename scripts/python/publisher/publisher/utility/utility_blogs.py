import re
import datetime
from typing import Tuple
from publisher.tool import get_blog_collections_root_path

from publisher.utility.utility_paths import get_default_collections_path


def get_formatted_timestamp() -> str:
    return datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%y_%H-%M-%S')


def is_valid_collection(collection_slug: str):
    if collection_slug is None or not collection_slug:
        raise ValueError("The blog collection slug name is invalid or null")

    blog_collection_root_path = get_blog_collections_root_path()
    if blog_collection_root_path is None or blog_collection_root_path == '':
        raise ValueError("The blog collection root paht is invalid or null")
    if not os.path.exists(blog_collection_root_path):
        raise IOError(
            f'The path \"{blog_collection_root_path}\" was not found.')

    return


def is_valid_blog(blog_slug_name: str, collection_slug: str = "default"):
    if blog_slug_name is None:
        raise ValueError("The blog slug name is invalid or null")

    if not is_valid_collection(collection_slug):
        raise Exception("The blog collection slug name is invalid or null")

    blog_collections_root = get_blog_collections_root_path()


def create_slug_from_name(blog_name: str):
    if blog_name is None or not blog_name:
        raise ValueError("The blog name defined is invalid or null")

    formatted = re.sub('[^a-zA-Z\_\-0-9]+', '-', blog_name)
    if formatted is None or formatted == '':
        raise ValueError("The formatted slug name is invalid or null")
    return formatted.lower()


def create_blog(blog_name: str, collection_name: str = None):
    collection_name = collection_name if collection_name is not None else "default"
    collections_path = get_default_collections_path()
    if collections_path is None:
        raise ValueError("The collections path is invalid or null")


def create_blog_collection(blog_collection_name: str):
    # sourcery skip: raise-specific-error
    if blog_collection_name is None:
        raise Exception("The collection name is invalid or null")


def get_blog_collections() -> Tuple:
    return


def get_blogs(collection_name: str = None) -> Tuple:
    collection_name = collection_name if collection_name is not None else "default"
