import os
import subprocess
from publisher.utility.utility_names import create_id_from_name

_repo_root = None


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


def get_default_collection_metadata_filename() -> str:
    return "collection.json"


def get_default_blog_metadata_filename() -> str:
    return "blog.json"


def get_default_config_filepath() -> str:
    """Get the absolute path to the default configuration file

    Returns:
        str: The absolute path to the default configuration file
    """
    return os.path.join(get_project_root(), "publisher", "data", "config", get_default_config_filename())


def get_default_user_config_filepath() -> str:
    """Get the default user configuration file path
+F
    Returns:
        str: Returns the absolute path to the user configuration path
    """
    return os.path.join(get_project_root(), "config", get_default_user_config_filename())


def _create_repo_root() -> str:
    """Resolve the absolute path to the root of the repository.

    Returns:
        str: The absolute path to the root of the repository.
    """
    process = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('ascii').rstrip()


def get_repo_root() -> str:
    """Get the absolute path to the root of the Git repository.

    Returns:
        str: Returns the absolute path of the Git repository.
    """
    global _repo_root

    if _repo_root is None:
        _repo_root = _create_repo_root()
    return _repo_root


def get_repo_root_path(*paths) -> str:
    """Get the absolute path to the newly generated path.

    Returns:
        str: Returns the absolute path.
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
        str: Returns the absolute path to the blog collections.
    """
    return os.path.abspath(os.path.join(get_default_blogs_path(), "collections"))


def get_default_collection_path() -> str:
    """Get the default absolute path to the collection

    Returns:
        str: Get the absolute path to the default collection.
    """
    return get_collection_path(get_default_collection_name())


def get_collection_path(collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path()) -> str:
    if not collection_id:
        raise ValueError("The name of the collection is invalid or null")
    collection_id = create_id_from_name(collection_id)
    if not collection_id:
        raise ValueError("The slug name is invalid or null")
    return os.path.join(collections_path, collection_id)


def get_collection_metadata_path(collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path()) -> str:
    if collection_id is None:
        raise ValueError("The name of the collection is invalid or null")
    collection_id = create_id_from_name(collection_id)
    return os.path.join(collections_path, collection_id, ".metadata")


def get_collection_metadata_filepath(collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path()) -> str:
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")
    if collections_path is None:
        raise ValueError("The collections path is invalid or null")
    return os.path.join(get_collection_metadata_path(collection_id, collections_path), "collection.json")


def get_blog_path(blog_id: str, collection_id: str = None, collections_path: str = get_default_collections_path()) -> str:
    collection_id = collection_id if collection_id is not None else get_default_collection_name()
    return os.path.join(get_collection_path(collection_id, collections_path), blog_id)


def get_blog_metadata_path(blog_id: str, collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path()) -> str:
    if blog_id is None:
        raise ValueError("The blog ID is invalid or null")
    if collection_id is None:
        raise ValueError("The collection ID is invalid or null")

    return os.path.join(get_blog_path(blog_id, collection_id, collections_path), ".metadata")


def get_blog_metadata_filepath(blog_id: str, collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path()) -> str:
    if not blog_id:
        raise ValueError("The ID of the blog is invalid or null")
    if not collection_id:
        raise ValueError("The ID of the collection is invalid or null")

    return os.path.join(get_blog_metadata_path(blog_id, collection_id, collections_path), "blog.json")


def get_default_export_path(*paths) -> str:
    """Get the default export path for exporting or rendering blogs out to.

    Returns:
        str: Returns the newly generaed path.
    """
    path_combined = os.sep.join(paths)
    return os.path.abspath(os.path.join(get_repo_root(), "exported", path_combined))


def get_blog_export_path(blog_id: str, collection_id: str = get_default_collection_name(), collections_path: str = get_default_collections_path()) -> str:
    if blog_id is None:
        raise ValueError("The blog is not considered valid.")
    if collection_id is None:
        raise ValueError("The collection is not considered valid.")

    return get_default_export_path("collections", collection_id, "blogs", blog_id)
