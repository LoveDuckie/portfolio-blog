from __future__ import annotations
import json
import os
from typing import Any, List, Optional
from pydantic import BaseModel


class BlogMetadata(BaseModel):
    id: str  # The ID or identifier
    name: str
    checksum: str
    summary: str
    tags: Optional[List[str]]
    path: str  # The path to where the blog is located.
    filepath: str

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

    @classmethod
    def create(cls, metadata_filepath: str, **kwargs) -> BlogMetadata:
        if metadata_filepath is None:
            raise ValueError(
                "The filepath to the metadata is invalid or null.")

        metadata_path = os.path.dirname(metadata_filepath)
        if not os.path.exists(metadata_path):
            os.makedirs(metadata_path)

        metadata = cls(**kwargs)
        return metadata

    def load_blog(self) -> Blog:
        return Blog(self)

    @classmethod
    def load(cls, metadata_filepath: str) -> BlogMetadata:
        if metadata_filepath is None:
            raise ValueError(
                "The filepath to the metadata is invalid or null.")
        return

    def save(self, metadata_filepath: str = None):
        metadata_filepath = metadata_filepath if metadata_filepath is not None else self.filepath
        if not metadata_filepath:
            raise ValueError(
                "The metadata file path is invalid or null. Unable to continue.")

    @classmethod
    def load(cls, metadata_filepath: str) -> BlogMetadata:
        """The load the metadata file

        Args:
            metadata_filepath (str): The absolute path to the metadata

        Raises:
            ValueError: If the metadata file path is invalid or null
            IOError: If the metadata file does not exist

        Returns:
            BlogMetadata: The newly deserialized meta data
        """
        if metadata_filepath is None:
            raise ValueError("The metadata is invalid or null")
        if not os.path.exists(metadata_filepath):
            raise IOError(
                f"Failed: the file \"{metadata_filepath}\" is invalid or null")

        file_content = None

        with open(metadata_filepath, "r") as f:
            file_content = f.read()
            if file_content is None:
                raise ValueError("The content of the file is invalid or null")

        metadata = BlogMetadata.parse_raw(
            file_content, content_type='application/json')
        if metadata is None:
            raise ValueError(
                "The loaded metadata is invalid or null. Unable to continue.")


class Blog:
    def __init__(self, metadata: BlogMetadata) -> None:
        if metadata is None:
            raise ValueError("The metadata for this blog is invalid or null")
        self._metadata = metadata
        self._loaded = False
        super().__init__()

    @property
    def metadata(self):
        return self._metadata

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, value):
        self._slug = value

    @property
    def description(self):
        return self._description

    @property
    def content(self):
        if self._loaded == False:
            return
        return self._content

    @property
    def collection(self):
        return self._collection

    @classmethod
    def load_blog(cls, blog_path):  # sourcery skip: raise-specific-error
        if blog_path is None or blog_path == '':
            raise ValueError("The blog path is invalid or null")

        if not os.path.isabs(blog_path):
            raise IOError(
                f'The path \"{blog_path}\" is not an absolute path. Unable to continue.')

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
