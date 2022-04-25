"""
    Publish

    A simple script for publishing and exporting blogs that are stored in this repository.
"""
import os, sys, logging
import argparse
import re
import json
import threading
import datetime
from typing import List

from blogs import BlogCollection, Blog

def create_slug_from_name(blog_name: str):
    if blog_name is None or blog_name == '':
        raise ValueError("The blog name defined is invalid or null")
    
    formatted = re.sub('[^a-zA-Z\_\-0-9]+', '-', blog_name)
    if formatted is None or formatted == '':
        raise ValueError("The formatted slug name is invalid or null")
    return formatted.lower()

def get_formatted_timestamp() -> str:
    today_date = datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%y_%H-%M-%S')
    return today_date

def get_default_logs_path_name() -> str:
    return get_default_logs_path_name()

def get_default_exporters() -> List[str]:
    """
    Get a list of default exporters to use

    Returns:
        list: A list of exporters to use
    """
    return [ "silverstripe", "packaged" ]

def get_log_filename() -> str:
    """
    Get the default filename for the log file

    Raises:
        ValueError: If the formatted timestamp that is returned is considered invalid

    Returns:
        str: The name of the log file to use by default.
    """
    formatted_timestamp = get_formatted_timestamp()
    if formatted_timestamp is None or formatted_timestamp == '':
        raise ValueError("The formatted timestamp is invalid or null")
    return f'publish-log-{get_formatted_timestamp()}.log'

def get_default_log_filepath():
    logs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), get_default_logs_path_name()))
    
    if logs_path is None or logs_path == '':
        raise ValueError("The logs path is invalid or null")
    
    return os.path.join(logs_path, get_log_filename())

arg_parser = argparse.ArgumentParser(description='Publish')

# Publish
arg_parser_group_publish = arg_parser.add_argument_group("Publish")
arg_parser_group_publish.add_argument('--publisher', dest='publishers', type=str, action='append', required=False)

# Export
arg_parser_group_export = arg_parser.add_argument_group("Export")
arg_parser_group_export.add_argument('--export-path', type=str, help='The absolute path for exported blogs (HTML format).', required=False, default=get_default_export_path())
arg_parser_group_export.add_argument('--exporters', dest='exporters', type=str, action='append', help='The list of exporters to use for writing out the blogs.', required=False, default=None)

# Create
arg_parser_group_create = arg_parser.add_argument_group("Create")
arg_parser_group_create.add_argument('--blog-name', type=str, help='The name of the blog to create', default=None, required=True)
arg_parser_group_create.add_argument('--blog-collection-name', type=str, help='The name of the blog collection', default='default', required=False)

arg_parser.add_argument('--blog-collection', dest='blog_collection', type=str, help='The slug name for the blog collection', required=False, default=None)
arg_parser.add_argument('--blog', dest='blog', type=str, help='The specific blog we wish to interact with', required=False, default=None)
arg_parser.add_argument('--blogs-path', dest='blogs_path', type=str, required=False, help='The relative or absolute path to where the blogs are located', default=get_default_blogs_path())
arg_parser.add_argument('--debug', dest='debug', required=False, type=bool, help='Enable debugging.', default=False)
arg_parser.add_argument('--log-filepath', dest='log_filepath', required=False, type=str, help='The absolute path to where the log file is to be written to.', default=get_default_log_filepath())

parsed_args = arg_parser.parse_known_args()[0]

if parsed_args is None:
    raise ValueError("The parsed arguments are invalid or null")

logger = logging.Logger(name='publish-log')

if parsed_args.log_filepath is not None and parsed_args.log_filepath != '':
    logger.addHandler(logging.FileHandler(filename=parsed_args.log_filepath))
    
logger.addHandler(logging.StreamHandler())

class ExportThread(threading.Thread):
    def run():
        return

if parsed_args.debug:
    logger.setLevel(logging.DEBUG)

def list_all_blogs(blog_collection_name = ""):
    if parsed_args is None:
        raise Exception("The parsed arguments are invalid or null")
    
    blogs_path = parsed_args.blogs_path
    
    if blogs_path is None or blogs_path == '':
        raise ValueError("The blogs path is ivnalid or null")
    
    paths = []
    
    for path in os.listdir(blogs_path):
        continue
    
    return paths

def is_valid_blog_collection(blog_collection_slug_name):
    if blog_collection_slug_name is None or blog_collection_slug_name == '':
        raise ValueError("The blog collection slug name is invalid or null")
    
    blog_collection_root_path = get_blog_collections_root_path()
    if blog_collection_root_path is None or blog_collection_root_path == '':
        raise ValueError("The blog collection root paht is invalid or null")
    if not os.path.exists(blog_collection_root_path):
        raise IOError(f'The path \"{blog_collection_root_path}\" was not found.')
    
    return

def is_valid_blog(blog_slug_name, blog_collection_slug_name = "default"):
    if blog_slug_name is None:
        raise ValueError("The blog slug name is invalid or null")
        
    if not is_valid_blog_collection(blog_collection_slug_name):
        raise Exception("")
    
    blog_collections_root = get_blog_collections_root_path()
    
    return

def list_all_collection():
    if parsed_args is None:
        raise Exception("The parsed arguments are null or invalid")
    
    return

def publish_blog():
    blog_name = parsed_args.blog_name
    blog_collection = parsed_args.blog_collection
    
    if parsed_args is None:
        raise ValueError("The parsed command-line arguments are invalid or null")
    
    if parsed_args.publishers is None:
        raise ValueError("The list of publishers is invalid or null")
    
    if not isinstance(parsed_args.publishers, list):
        raise ValueError("The list of publishers is not a list.")
    
    if not any(parsed_args.publishers):
        raise ValueError("No publishers were defined.")
    
    return

def get_all_blog_collection():
    blogs_path = parsed_args.blogs_path
    
    for blog_path in os.listdir(blogs_path):
        continue
    return

def create_blog(blog_name, blog_collection_name='default'):
    if blog_name is None or blog_name == '':
        raise ValueError("The blog name is invalid or null")
    if blog_collection_name is None or blog_collection_name == '':
        raise ValueError("The blog name is invalid or null")
    
    blog_slug_name = create_slug_from_name(blog_name)
    if blog_slug_name is None or blog_slug_name == '':
        raise ValueError("The blog slug name is invalid or null")

def export_blog(blog_name, blog_collection_name='default'):
    if parsed_args is None:
        raise ValueError("The parsed arguments are invalid or null")
    
    if parsed_args.blog is None or parsed_args.blog == '':
        raise ValueError("The blog name is invalid or null")
    
    return

def get_blog_collections_root_path():
    if parsed_args is None:
        raise ValueError("The parsed arguments are invalid.")
    
    if parsed_args.blogs_path is None:
        raise ValueError("The blogs path specified is invalid or null.")
    
    blog_collection_root_path = os.path.join(parsed_args.blogs_path, "collection")
    
    if blog_collection_root_path is None or blog_collection_root_path == "":
        raise ValueError("The blog collection path is invalid or null.")
    
    return blog_collection_root_path

def get_blog_collection_path(blog_collection_name):
    if blog_collection_name is None or blog_collection_name == '':
        raise ValueError("The blog collection name is invalid or null")
    
    blogs_collection_root_path = get_blog_collections_root_path()
    if blogs_collection_root_path is None or blogs_collection_root_path == '':
        raise ValueError("The blog collection path is invalid or null")
    
    slug_name = create_slug_from_name(blog_collection_name)
    blog_collection_path = os.path.join(blogs_collection_root_path, slug_name)
    if blog_collection_path is None or blog_collection_path == '':
        raise ValueError("The blog collection path is invalid or null")
    
    return blog_collection_path

def get_blog_collection_metadata(blog_collection_name):
    blog_collection_metadata_filepath = os.path.join(get_blog_collection_path(blog_collection_name), "collection.json")
    
    if not os.path.exists(blog_collection_metadata_filepath):
        raise FileExistsError(f'Failed to find the file \"{blog_collection_metadata_filepath}\"')
    
    metadata = None
    
    with open(blog_collection_metadata_filepath, 'r') as file:
        metadata = file.read()
        
    if metadata is None:
        raise ValueError("The meta data is invalid or null")
    
    loaded_data = json.loads(metadata)
    return loaded_data    

def get_all_blogs_from_collection(blog_collection_slug_name):
    if blog_collection_slug_name is None or blog_collection_slug_name == '':
        raise ValueError("The blog collection name specified is invalid or null")

    return ""

def main(args):
    return

if __name__ == "__main__":
    main(sys.argv)