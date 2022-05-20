import re


def create_slug_from_name(blog_name: str) -> str:
    """Generate the slug name from the name of the blog

    Args:
        blog_name (str): The name to generate a blog name from

    Raises:
        ValueError: If the blog name was not defined.
        ValueError: If the newly formatted blog name is not valid.

    Returns:
        str: The newly generated slug name
    """
    if blog_name is None or not blog_name:
        raise ValueError("The blog name defined is invalid or null")

    formatted = re.sub('[^a-zA-Z\_\-0-9]+', '-', blog_name)
    if formatted is None or formatted == '':
        raise ValueError("The formatted slug name is invalid or null")
    return formatted.lower()
