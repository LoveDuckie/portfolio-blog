import os

def get_default_blogs_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".." , "..", "..", "..", "blogs"))

def get_default_blog_collection_path():
    return os.path.abspath(os.path.join(get_default_blogs_path(), "collection"))

def get_default_export_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".." , "..", "..", "..", "exported"))