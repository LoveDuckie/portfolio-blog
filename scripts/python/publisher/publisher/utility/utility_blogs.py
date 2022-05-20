import os
import datetime
from typing import Tuple

from publisher.utility.utility_paths import get_blog_path, get_collection_path, get_default_collections_path


def get_formatted_timestamp() -> str:
    return datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%y_%H-%M-%S')


def is_valid_collection(collection_slug: str) -> bool:
    if collection_slug is None or not collection_slug:
        raise ValueError("The blog collection slug name is invalid or null")

    blog_collection_root_path = get_default_collections_path()
    if blog_collection_root_path is None or blog_collection_root_path == '':
        raise ValueError("The blog collection root paht is invalid or null")
    if not os.path.exists(blog_collection_root_path):
        raise IOError(
            f'The path \"{blog_collection_root_path}\" was not found.')

    return True


def is_valid_blog(blog_slug: str, collection_slug: str = "default") -> bool:
    # sourcery skip: raise-specific-error
    if blog_slug is None:
        raise ValueError("The blog slug name is invalid or null")

    if not is_valid_collection(collection_slug):
        raise Exception("The blog collection slug name is invalid or null")

    blog_collection_path = get_collection_path(collection_slug, blog_slug)
    if not os.path.exists(blog_collection_path):
        raise IOError(
            f"The path {blog_collection_path} does not exist. Unable to continue.")

    blog_collection_metadata_filepath = os.path.join(
        blog_collection_path, "collection.json")


def create_blog(blog_name: str, collection_name: str = None):
    collection_name = collection_name if collection_name is not None else "default"
    blog_path = get_blog_path(blog_name, collection_name)
    if not os.path.exists(blog_path):
        os.makedirs(blog_path)

    paths = ['assets', '.metadata']
    for path in paths:
        new_path = os.path.join(blog_path, path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)


def create_blog_collection(collection_name: str):
    # sourcery skip: raise-specific-error
    if collection_name is None:
        raise Exception("The collection name is invalid or null")
    collection_path = get_collection_path(collection_name)


def get_blog_collections() -> Tuple:
    return


def get_blogs(collection_name: str = None) -> Tuple:
    collection_name = collection_name if collection_name is not None else "default"
