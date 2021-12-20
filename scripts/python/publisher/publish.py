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

from blog_series import BlogSeries
from blog import Blog

def get_default_blogs_path():
    """Get the default path for where logs are stored

    Returns:
        string: The absolute path to where the logs are stored.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","..","blogs"))

def get_default_export_path():
    """Get the default path for where blogs should be exported

    Returns:
        string: The absolute path to where the blogs are to be exported.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","..","exported"))

def create_slug_from_name(blog_name):
    """Create the slug identifier from the name speified

    Args:
        blog_name (string): The name of the blog

    Raises:
        ValueError: If the blog name was not specified correctly

    Returns:
        string: The newly formatted slug name from the blog nameW
    """
    if blog_name is None or blog_name == '':
        raise ValueError("The blog name defined is invalid or null")
    
    formatted = re.sub('[^a-zA-Z\_\-0-9]+', '-', blog_name)
    if formatted is None or formatted == '':
        raise ValueError("The formatted slug name is invalid or null")
    return formatted.lower()

def get_formatted_timestamp():
    today_date = datetime.datetime.strftime(datetime.datetime.now, '%d-%m-%y_%H-%M-%S')
    return today_date

def get_default_logs_path_name():
    return "logs"

def get_log_filename():
    """Generate the log filename to use as a default

    Returns:
        string: The name of the log file to use
    """
    return f'publish-log-{get_formatted_timestamp()}.log'

def get_default_log_filepath():
    """Get the absolute path to the log file that is being written

    Returns:
        string: The absolute path to the log file that we are writing to
    """
    logs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "logs"))
    return os.path.join(logs_path ,get_log_filename())

arg_parser = argparse.ArgumentParser(description='Publish or export blogs')

arg_parser_group_publish = arg_parser.add_argument_group("Publish")
arg_parser_group_publish.add_argument('--publisher', dest='publishers', type=str, action='append', required=False)

arg_parser_group_export = arg_parser.add_argument_group("Export")
arg_parser_group_export.add_argument('--export-path', type=str, help='The absolute path for exported blogs (HTML format).', required=False, default=get_default_export_path())

arg_parser_group_create = arg_parser.add_argument_group("Create")
arg_parser_group_create.add_argument('--blog-name', type=str, help='The name of the blog to create', default=None, required=True)
arg_parser_group_create.add_argument('--blog-series-name', type=str, help='The name of the blog series', default='default', required=False)

arg_parser.add_argument('--blog-series', dest='blog_series', type=str, help='The slug name for the blog series', required=False, default=None)
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

def list_all_blogs(blog_series_name):
    if parsed_args is None:
        raise Exception("The parsed arguments are invalid or null")
    return

def list_all_series():
    if parsed_args is None:
        raise Exception("The parsed arguments are null or invalid")
    
    return

def publish_blog():
    blog_name = parsed_args.blog_name
    blog_series = parsed_args.blog_series
    
    if parsed_args is None:
        raise ValueError("The parsed command-line arguments are invalid or null")
    
    if parsed_args.publishers is None:
        raise ValueError("The list of publishers is invalid or null")
    
    if not any(parsed_args.publishers):
        raise ValueError("No publishers were found.")
    
    return

def get_all_series():
    blogs_path = parsed_args.blogs_path
    for blog_path in os.listdir(blogs_path):
        continue
    return

def create_blog(blog_name, blog_series_name='default'):
    if blog_name is None or blog_name == '':
        raise ValueError("The blog name is invalid or null")
    if blog_series_name is None or blog_series_name == '':
        raise ValueError("The blog name is invalid or null")
    
    blog_slug_name = create_slug_from_name(blog_name)
    if blog_slug_name is None or blog_slug_name == '':
        raise ValueError("The blog slug name is invalid or null")

def export_blog(blog_name, blog_series_name='default'):
    if parsed_args is None:
        raise ValueError("The parsed arguments are invalid or null")
    
    if parsed_args.blog is None or parsed_args.blog == '':
        raise ValueError("The blog name is invalid or null")
    
    return

def get_blog_series_path(blog_series_name):
    if blog_series_name is None or blog_series_name == '':
        raise ValueError("The blog series name is invalid or null")
    
    slug_name = create_slug_from_name(blog_series_name)
    blog_series_path = os.path.join(parsed_args.blogs_path, slug_name)

    return blog_series_path

def get_blog_series_metadata(blog_series_name):
    blog_series_metadata_filepath = os.path.join(get_blog_series_path(blog_series_name), "series.json")
    if not os.path.exists(blog_series_metadata_filepath):
        raise FileExistsError(f'Failed to find the file \"{blog_series_metadata_filepath}\"')
    
    metadata = None
    
    with open(blog_series_metadata_filepath, 'r') as file:
        metadata = file.read()
        
    if metadata is None:
        raise ValueError("The meta data is invalid or null")
    
    loaded_data = json.loads(metadata)
    return loaded_data    

def get_all_blogs_from_series(series_slug_name):
    if series_slug_name is None or series_slug_name == '':
        raise ValueError("The blog series name specified is invalid or null")

    return

def main(args):
    return

if __name__ == "__main__":
    main(sys.argv)