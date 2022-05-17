import os
import subprocess

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


def get_default_blogs_path() -> str:
    return os.path.abspath(os.path.join(get_repo_root(), "blogs"))


def get_default_collections_path() -> str:
    """Get the default collections path

    Returns:
        str: Returns the absolute path to the blog collections
    """
    return os.path.abspath(os.path.join(get_repo_root, "collections"))


def get_blog_collection_path(collection_name: str) -> str:
    return os.path.join(get_repo_root(), "blogs", "collections")


def get_blog_path(blog_name: str, collection_name: str = None) -> str:
    collection_name = collection_name if collection_name is not None else "default"
    return os.path.join(get_blog_collection_path(collection_name), blog_name)


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


def get_default_config_filepath() -> str:
    return os.path.join(get_project_root(), "publisher", "data", "config", "default.ini")

def get_default_user_config_filepath() -> str:
    """Get the default user configuration file path

    Returns:
        str: Returns the absolute path to the user configuration path
    """
    return os.path.join(get_project_root(), "config","user.ini")