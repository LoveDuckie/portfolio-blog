import os
from typing import List
from publisher.blogs.blog import Blog, BlogMetadata
from publisher.blogs.blog_collection import BlogCollection, BlogCollectionMetadata
from publisher.utility.utility_names import create_id_from_name

from publisher.utility.utility_paths import get_blog_metadata_filepath, get_blog_path, get_collection_metadata_filepath, get_collection_path, get_default_collection_name, get_default_collections_path

_collection_dirs = ['.metadata', 'assets', 'blogs']
_blog_dirs = ['.metadata', 'assets']


def is_valid_collection(collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path()) -> bool:
    if collection_id is None or not collection_id:
        raise ValueError("The blog collection ID is invalid or null")

    if not os.path.exists(collections_path):
        return False

    collection_path = get_collection_path(collection_id, collections_path)

    if not collection_path:
        raise ValueError("The collection path is invalid or null")

    if not os.path.exists(collection_path):
        return False

    return True


def is_valid_blog(blog_id: str, collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path()) -> bool:
    # sourcery skip: raise-specific-error
    if blog_id is None:
        raise ValueError("The blog slug name is invalid or null")

    if not is_valid_collection(collection_id):
        raise Exception("The blog collection slug name is invalid or null")

    collection_path = get_collection_path(collection_id, collections_path)
    if not os.path.exists(collection_path):
        return False

    collection_metadata_filepath = os.path.join(
        collection_path, "collection.json")

    if not os.path.exists(collection_metadata_filepath):
        return False

    return True


def create_blog_paths(target_path: str) -> None:
    """Create the paths for a new blog at the target path specified.

    Args:
        target_path (str): The absolute path to the directory to create the paths in

    Raises:
        ValueError: The absolue target path is invalid or null
        IOError: The absolute target path does not exist
    """
    global _blog_dirs
    if target_path is None:
        raise ValueError("The path was not specified. Unable to continue.")

    if not os.path.isabs(target_path):
        raise IOError(
            f"The path \"{target_path}\" is not an absolute path. Unable to continue.")

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for path in _blog_dirs:
        new_path = os.path.join(target_path, path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)


def create_collections_paths(target_path: str) -> None:
    """Create the paths for the collection

    Args:
        target_path (str): The absolute path to the target directory

    Raises:
        ValueError: If the target path was not defined.
    """
    global _collection_dirs
    if target_path is None:
        raise ValueError("The target path is invalid or null")

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for path in _collection_dirs:
        os.makedirs(os.path.join(target_path, path))


def create_blog_metadata_file(blog_id: str, collection_id: str, collections_path: str = get_default_collections_path(), **kwargs) -> BlogMetadata:
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null.")

    if collection_id is None:
        raise ValueError("The collection ID is invalid or null.")

    if not os.path.exists(collections_path):
        raise IOError(f"The path \"{collections_path}\" does not exist.")

    blog_path = get_blog_path(blog_id, collection_id, collections_path)
    if not os.path.exist(blog_path):
        os.makedirs(blog_path)

    blog = BlogMetadata.create(os.path.dirname(get_blog_metadata_filepath(
        blog_id, collection_id, collections_path)), **kwargs)
    if blog is None:
        raise ValueError("The blog is invalid or null")

    return blog


def create_blog(blog_id: str, collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path(), **kwargs):
    global _blog_dirs
    if not blog_id:
        raise ValueError("The blog ID is invalid or null")
    blog_path = get_blog_path(blog_id, collection_id, collections_path)

    if not os.path.exists(blog_path):
        os.makedirs(blog_path)

    blog_slug = create_id_from_name(blog_id)
    if blog_slug is None or blog_slug == '':
        raise ValueError("The blog slug name is invalid or null")

    create_blog_paths(get_blog_path(blog_id, collection_id))
    create_blog_metadata_file()


def create_collection(collection_name: str = get_default_collection_name(), collections_path: str = get_default_collections_path(), **kwargs):
    """Create the blog collection

    Args:
        collection_name (str): The name or slug name of the collection
        collections_path (str, optional): The absolute path to where the blog collections are. Defaults to get_default_collections_path().

    Raises:
        ValueError: The collection name is invalid or null.
        ValueError: The blog collection is not considered valid.
    """
    global _collection_dirs
    if collection_name is None:
        raise ValueError("The collection name is invalid or null")

    collection_id = create_id_from_name(collection_name)

    if is_valid_collection(collection_id, collections_path):
        raise Exception(f"The \"{collection_id}\" already exists.")

    collection_path = get_collection_path(collection_id, collections_path)

    if not os.path.exists(collection_path) and not kwargs['force']:
        os.makedirs(collection_path)

    for path in _collection_dirs:
        new_path = os.path.join(collection_path, path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)

    create_collection_metadata_file(collection_id, collections_path, **kwargs)


def create_collection_metadata_file(collection_id: str, collections_path: str = get_default_collections_path(), **kwargs) -> BlogCollectionMetadata:
    if collection_id is None:
        raise ValueError("The collection name is invalid or null")

    if not is_valid_collection(collection_id, collections_path):
        create_collection(collection_id, collections_path)

    collection_path = get_collection_path(collection_id, collections_path)
    if not collection_path:
        raise ValueError(
            "The absolute path to the collection is invalid or null")

    collection_metadata_filepath = get_collection_metadata_filepath(
        collection_id, collections_path)
    collection_metadata_path = os.path.dirname(collection_metadata_filepath)
    if not os.path.exists(collection_metadata_path):
        os.makedirs(collection_metadata_path)

    collection_metadata = BlogCollectionMetadata.create(
        collection_metadata_filepath, **kwargs)

    if not collection_metadata:
        raise ValueError("The collection metadata is invalid or null")

    return collection_metadata


def get_collections(collections_path: str = get_default_collections_path()) -> List[BlogCollection]:
    """Get a list of blog collections

    Args:
        collections_path (str, optional): The absolute path to blog collections.. Defaults to get_default_collections_path().

    Raises:
        ValueError: The collections path specified is invalid or null
        IOError: The collections path does not exist.
        IOError: The collection path does not exist.

    Returns:
        List[BlogCollection]: A list of collections.
    """
    if collections_path is None:
        raise ValueError("The path specified is invalid or null")

    if not os.path.exists(collections_path):
        raise IOError(
            f"The path \"{collections_path}\" does not exist. Unable to continue.")

    collections = []

    for collection_id in os.listdir(collections_path):
        collection_path = os.path.join(collections_path, collection_id)
        if not os.path.exists(collection_path):
            raise IOError(
                f"Failed: unable to find the path \"{collection_path}\"")

        if not is_valid_collection(collection_id, collections_path):
            raise Exception(
                f"The collection \"{collection_id}\" is not valid.")

        collection = BlogCollection(BlogCollectionMetadata.load(
            get_collection_metadata_filepath(collection_id, collections_path)))
        collections.append(collection)

    return collections


def get_collection(collection_id: str, collections_path: str = get_default_collections_path()) -> BlogCollection:
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")

    if collections_path is None:
        raise ValueError("The collections path specified is invalid or null")

    collection_metadata_filepath = get_collection_metadata_filepath(
        collection_id, collections_path)
    
    if not os.path.exists(collection_metadata_filepath):
        raise IOError(f"Failed: unable to find metadata filepath \"{collection_metadata_filepath}\"")
    collection_metadata = BlogCollectionMetadata.load(
        collection_metadata_filepath)
    if collection_metadata is None:
        raise ValueError("The collection metadata is invalid or null")

    return BlogCollection(collection_metadata)


def get_blogs(collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path()) -> List:
    blogs = []

    collection_path = get_collection_path(collection_id, collections_path)
    metadata_filepath = get_collection_metadata_filepath(
        collection_id, collections_path)
    if metadata_filepath is None:
        raise ValueError("The metadata filepath is invalid or null")

    if not os.path.exists(metadata_filepath):
        raise IOError(
            f"Failed: unable to find the file \"{metadata_filepath}\"")
    
    for blog_id in os.listdir(collection_path):
        blog_metadata_filepath = get_blog_metadata_filepath(
            blog_id, collection_id, collections_path)

        blog_metadata = BlogMetadata.load(blog_metadata_filepath)
        blogs.append(Blog(blog_metadata))

    return blogs
