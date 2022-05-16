import os
import subprocess

def get_default_blogs_path() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".." , "..", "..", "..", "blogs"))

def get_default_blog_collection_path() -> str:
    """Get the default collections path

    Returns:
        str: Returns the absolute path to the blog collections
    """
    return os.path.abspath(os.path.join(get_default_blogs_path(), "collections"))

def get_default_export_path():
    """Get the default path to where blogs are exported to

    Returns:
        _type_: _description_
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".." , "..", "..", "..", "exported"))

def get_repo_root() -> str:
    
    return subprocess.run(["git", "rev-parse", "--show-toplevel"]).stdout.read()

def get_project_root():
    """Get the absolute path to the root of the project

    Returns:
        str: The absolute path to the root of of the project
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__),"..",".."))


def get_project_path(*paths) -> str:
    """Generate the project path based on the elements specified in the list

    Returns:
        str: The absolute path
    """
    return os.path.join(get_project_root(), *paths)
