import re
import datetime

def get_formatted_timestamp() -> str:
    return datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%y_%H-%M-%S')

def create_slug_from_name(blog_name: str):
    if blog_name is None or not blog_name:
        raise ValueError("The blog name defined is invalid or null")

    formatted = re.sub('[^a-zA-Z\_\-0-9]+', '-', blog_name)
    if formatted is None or formatted == '':
        raise ValueError("The formatted slug name is invalid or null")
    return formatted.lower()