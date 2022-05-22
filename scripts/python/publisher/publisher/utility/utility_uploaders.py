import pkgutil
from typing import List
from publisher import image_uploaders
from publisher.utility.utility_blogs import is_valid_collection
from publisher.utility.utility_paths import get_default_collection_name, get_default_collections_path
from utility_blogs import is_valid_blog
import os


def get_image_uploader_modules() -> List:
    return list(map(lambda x: x.name, filter(lambda x: not x.name.endswith("interface") and not x.ispkg, pkgutil.iter_modules([os.path.dirname(image_uploaders.__file__)]))))


def upload_collection(collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path()):
    if collection_id is None:
        raise ValueError("The collection is invalid or null")
    if not is_valid_collection(collection_id):
        raise Exception(
            f"The collection {collection_id} is not valid. Unable to continue.")


def upload_blog(blog_name: str, collection_id: str = None, collections_path: str = get_default_collections_path()):
    # sourcery skip: raise-specific-error
    if not is_valid_blog(blog_name, collection_id, collections_path):
        raise Exception(
            f"The blog \"{blog_name}\" is not valid. Check that it exists, and try again.")
    return
