import pkgutil
from typing import List
from publisher import image_uploaders
from publisher.utility.utility_blogs import is_valid_collection
from utility_blogs import is_valid_blog
import os


def get_image_uploader_modules() -> List:
    return list(map(lambda x: x.name, filter(lambda x: not x.name.endswith("interface") and not x.ispkg, pkgutil.iter_modules([os.path.dirname(image_uploaders.__file__)]))))


def upload_collection(collection_name: str):
    if collection_name is None:
        raise ValueError("The collection is invalid or null")
    if not is_valid_collection(collection_name):
        raise Exception(
            f"The collection {collection_name} is not valid. Unable to continue.")


def upload_blog(blog_name: str, collection_name: str = None):
    # sourcery skip: raise-specific-error
    if not is_valid_blog(blog_name, collection_name):
        raise Exception(
            f"The blog \"{blog_name}\" is not valid. Check that it exists, and try again.")
    return
