from __future__ import annotations
import json
import os
from typing import Any, List, Optional
from pydantic import BaseModel

from publisher.blogs.blog import Blog


class BlogCollectionMetadata(BaseModel):
    id: str
    name: str
    description: str
    summary: Optional[str]
    metadata: dict[str, dict]
    path: Optional[str]
    filepath: Optional[str]
    tags: Optional[List[str]]

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

    @classmethod
    def create(cls, metadata_filepath: str, **kwargs) -> BlogCollectionMetadata:
        if metadata_filepath is None:
            raise ValueError("The metadata file path is invalid or null")

        metadata_path = os.path.dirname(metadata_filepath)
        if not os.path.exist(metadata_path):
            raise IOError(f"The path \"{metadata_path}\" does not exist.")

        os.makedirs(metadata_path)
        collection_metadata = cls(**kwargs)
        collection_metadata.save(metadata_filepath)

    @classmethod
    def load(cls, metadata_filepath: str) -> BlogCollectionMetadata:
        if metadata_filepath is None:
            raise ValueError("The metadata filepath was not correctly defined")

        if not os.path.abspath(metadata_filepath):
            raise IOError(
                f"Thet path \"{metadata_filepath}\" is not an absolute filepath.")

        if not os.path.exists(metadata_filepath):
            raise IOError(
                f"The absolute path to the metadata is invalid or null (\"{metadata_filepath}\")")

        with open(metadata_filepath, 'r') as f:
            raw = f.read()

        collection_metadata = BlogCollectionMetadata.parse_raw(raw)
        collection_metadata.filepath = metadata_filepath
        collection_metadata.path = os.path.dirname(
            os.path.dirname(metadata_filepath))
        return collection_metadata

    def save(self, filepath: str = None):
        if filepath is None and hasattr(self, "filepath"):
            filepath = self.filepath

        content = json.dumps(self)
        if not content:
            raise ValueError("The content is invalid or null")
        with open(filepath, 'w') as f:
            f.write(content)


class BlogCollection:
    def __init__(self, metadata: BlogCollectionMetadata) -> None:
        super().__init__()
        if metadata is None:
            raise ValueError("The metadata is invalid or null")
        self._metadata = metadata

    @property
    def id(self) -> str:
        return self._metadata.id

    @property
    def name(self) -> str:
        return self._metadata.name

    @property
    def description(self) -> str:
        return self._metadata.description

    @property
    def summary(self) -> str:
        return self._metadata.summary

    @property
    def blogs(self) -> List[Blog]:
        if hasattr(self, "blogs"):
            return self.blogs
        blogs = []

        setattr(self, "blogs", blogs)
        return blogs
