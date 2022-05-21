import os
import subprocess

from publisher.utility.utility_names import create_slug_from_name

_repo_root = None


def _create_repo_root() -> str:
    process = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('ascii').rstrip()


def get_repo_root() -> str:
    """Get the absolute path to the root of the Git repository

    Returns:
        str: Returns the absolute path of the Git repository
    """
    global _repo_root

    if _repo_root is None:
        _repo_root = _create_repo_root()
    return _repo_root


def get_repo_root_path(*paths) -> str:
    """Get the absolute path to the newly generated path

    Returns:
        str: Returns the absolute path
    """
    return os.path.join(get_repo_root(), *paths)


def get_default_blogs_path() -> str:
    """Returns the default path to where the blogs are stored in the repository.

    Returns:
        str: The absolute path to where the blogs are stored in the repository.
    """
    return os.path.abspath(os.path.join(get_repo_root(), "blogs"))


def get_default_collections_path() -> str:
    """Get the default collections path

    Returns:
        str: Returns the absolute path to the blog collections
    """
    return os.path.abspath(os.path.join(get_default_blogs_path(), "collections"))


def get_collection_path(collection_name: str, collections_path: str = None) -> str:
    if not collection_name:
        raise ValueError("The name of the collection is invalid or null")
    collection_slug_name = create_slug_from_name(collection_name)
    if not collection_slug_name:
        raise ValueError("The slug name is invalid or null")
    return os.path.join(get_default_collections_path(), collection_slug_name)


def get_collection_metadata_filepath(collection_name: str) -> str:
    if not collection_name:
        raise ValueError("The name of the collection is invalid or null")
    collection_path = get_collection_path(collection_name)
    return os.path.join(collection_path, ".metadata", "collection.json")


def get_blog_path(blog_name: str, collection_name: str = None) -> str:
    collection_name = collection_name if collection_name is not None else "default"
    return os.path.join(get_collection_path(collection_name), blog_name)


def get_blog_metadata_filepath(blog_name: str, collection_name: str) -> str:
    if not collection_name:
        raise ValueError("The name of the collection is invalid or null")
    blog_path = get_blog_path(blog_name, collection_name)
    return os.path.join(blog_path, ".metadata", "blog.json")


def get_default_export_path():
    """Get the default path to where blogs are exported to

    Returns:
        _type_: _description_
    """
    return os.path.abspath(os.path.join(get_repo_root(), "exported"))


def get_project_root():
    """Get the absolute path to the root of the project

    Returns:
        str: The absolute path to the root of of the project
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def get_project_path(*paths) -> str:
    """Generate the project path based on the elements specified in the list

    Returns:
        str: The absolute path
    """
    return os.path.join(get_project_root(), *paths)


def get_default_collection_name() -> str:
    return "default"


def get_default_user_config_filename() -> str:
    return "user.ini"


def get_default_config_filename() -> str:
    return "default.ini"


def get_default_config_filepath() -> str:
    """Get the absolute path to the default configuration file

    Returns:
        str: The absolute path to the default configuration file
    """
    return os.path.join(get_project_root(), "publisher", "data", "config", "default.ini")


def get_default_user_config_filepath() -> str:
    """Get the default user configuration file path
+F
    Returns:
        str: Returns the absolute path to the user configuration path
    """
    return os.path.join(get_project_root(), "config", "user.ini")
