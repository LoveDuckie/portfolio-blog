import json
import os
from typing import Any, Optional
from pydantic import BaseModel

class BlogMetadata(BaseModel):
    name: str
    checksum: str
    summary: str
    slug: str
    path: Optional[str]
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

class Blog:
    def __init__(self, metadata: BlogMetadata) -> None:
        if metadata is None:
            raise ValueError("The metadata for this blog is invalid or null")
        super().__init__()

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        if value is None:
            raise ValueError("The name is invalid or null")
        self.name = value

    @property
    def slug(self):
        return self.slug

    @slug.setter
    def slug(self, value):
        return

    @property
    def description(self):
        return self.description
    
    @property
    def content(self):
        return self.content

    @property
    def collection(self):
        return self.collection

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
