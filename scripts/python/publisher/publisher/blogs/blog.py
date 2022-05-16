import json
import os
from typing import Any


class BlogMetadata:
    def __init__(self) -> None:
        pass


class Blog:
    def __init__(self, **kwargs) -> None:
        self.properties = {}
        for key in kwargs:
            self.__dict__[key] = kwargs[key]
        super().__init__()

    @property
    def name(self):
        return self.name

    @name.getter
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if value is None:
            raise ValueError("The name is invalid or null")
        self.name = value

    @property.getter
    def slug(self):
        return self.slug

    @property.getter
    def description(self):
        return self.description

    @property.getter
    def collection(self):
        return None

    @classmethod
    def load_blog(cls, blog_path):  # sourcery skip: raise-specific-error
        if blog_path is None or blog_path == '':
            raise ValueError("The blog path is invalid or null")

        if not os.path.isdir(blog_path):
            raise IOError(
                f'The path \"{blog_path}\" is not a valid directory. It must be a directory.')

        blog_metadata_filepath = os.path.join(blog_path, "blog.json")

        if not os.path.isfile(blog_metadata_filepath):
            raise IOError(
                f'The file \"{blog_metadata_filepath}\" is not a valid file')

        if not os.path.exists(blog_metadata_filepath):
            raise Exception(
                f'Unable to find the metadata file \"{blog_metadata_filepath}\".')

        blog_metadata = None

        with open(blog_metadata_filepath, 'r') as file:
            blog_metadata = file.read()
            if blog_metadata is None:
                raise ValueError("The blog metadata is invalid or null")

        if blog_metadata is None:
            raise ValueError("The loaded metadata is invalid or null")

        loaded_metadata = json.loads(blog_metadata)

        if loaded_metadata is None:
            raise ValueError("The loaded metadata is invalid or null")

        if not isinstance(loaded_metadata, dict):
            raise TypeError('The loaded metadata was not a dictionary.')

        return cls(**loaded_metadata)
