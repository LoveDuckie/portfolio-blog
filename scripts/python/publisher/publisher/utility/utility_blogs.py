import os
from typing import List
from publisher.blogs.blog import BlogMetadata
from publisher.blogs.blog_collection import BlogCollection
from publisher.utility.utility_names import create_slug_from_name

from publisher.utility.utility_paths import get_blog_path, get_collection_path, get_default_collection_name, get_default_collections_path


def is_valid_collection(collection_slug: str, collections_path: str = get_default_collections_path()) -> bool:
    if collection_slug is None or not collection_slug:
        raise ValueError("The blog collection slug name is invalid or null")

    blog_collection_root_path = get_default_collections_path()
    if blog_collection_root_path is None or blog_collection_root_path == '':
        raise ValueError("The blog collection root paht is invalid or null")
    if not os.path.exists(blog_collection_root_path):
        raise IOError(
            f'The path \"{blog_collection_root_path}\" was not found.')

    return True


def is_valid_blog(blog_slug: str, collection_slug: str = get_default_collection_name()) -> bool:
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


def create_blog_paths(target_path: str) -> None:
    """Create the paths for a new blog at the target path specified.

    Args:
        target_path (str): The absolute path to the directory to create the paths in

    Raises:
        ValueError: The absolue target path is invalid or null
        IOError: The absolute target path does not exist
    """
    paths = ['assets', '.metadata']
    if target_path is None:
        raise ValueError("The path was not specified. Unable to continue.")

    if not os.path.isabs(target_path):
        raise IOError(
            f"The path \"{target_path}\" is not an absolute path. Unable to continue.")

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for path in paths:
        os.makedirs(os.path.join(target_path, path))


def create_collections_paths(target_path: str) -> None:
    paths = ['assets', '.metadata', 'blogs']
    if target_path is None:
        raise ValueError("The target path is invalid or null")
    return


def create_blog(blog_name: str, collection_name: str = None, collections_path: str = None):
    collection_name = collection_name if collection_name is not None else get_default_collection_name()
    blog_path = get_blog_path(blog_name, collection_name)
    if not os.path.exists(blog_path):
        os.makedirs(blog_path)

    paths = ['assets', '.metadata']
    for path in paths:
        new_path = os.path.join(blog_path, path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)


def create_collection(collection_name: str, collections_path: str = None):
    if collection_name is None:
        raise ValueError("The collection name is invalid or null")
    collections_path = collections_path if collections_path is not None else get_default_collections_path()
    collection_path = get_collection_path(collection_name, collections_path)
    if not os.path.exists(collection_path):
        os.makedirs(collection_path)

    paths = ['assets', '.metadata']
    for path in paths:
        new_path = os.path.join(collection_path, path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)


def create_collection_metadata_file(collection_name: str, force: bool = False):
    if collection_name is None:
        raise ValueError("The collection name is invalid or null")

    if not is_valid_collection(collection_name):
        create_collection(collection_name)

    collection_path = get_collection_path(collection_name)
    if not collection_path:
        raise ValueError(
            "The absolute path to the collection is invalid or null")


def get_collections(path: str) -> List[BlogCollection]:
    if path is None:
        raise ValueError("The path specified is invalid or null")
    return []


def get_collection(path: str) -> BlogCollection:
    if path is None:
        raise ValueError("The path specified is invalid or null")

    return


def get_blogs(collection_name: str = None) -> List:
    collection_name = collection_name if collection_name is not None else get_default_collection_name()

    collection_path: str = get_collection_path(collection_name)
    if collection_path is None:
        raise ValueError("The collection path is invalid or null")

    return [BlogMetadata.load() for _ in os.listdir(collection_path)]


def create_blog(blog_name, collection_name=get_default_collection_name()):
    if blog_name is None or blog_name == '':
        raise ValueError("The blog name is invalid or null")
    if collection_name is None or collection_name == '':
        raise ValueError("The blog name is invalid or null")

    blog_slug = create_slug_from_name(blog_name)
    if blog_slug is None or blog_slug == '':
        raise ValueError("The blog slug name is invalid or null")

    create_blog_paths(get_blog_path(blog_name, collection_name))
