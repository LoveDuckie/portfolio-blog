from __future__ import annotations
import json
import os
from typing import Any, List, Optional
from pydantic import BaseModel


class BlogCollectionMetadata(BaseModel):
    id: str
    name: str
    description: str
    summary: str
    path: str
    filepath: Optional[str]
    tags: Optional[List[str]]
    metadata: dict[str, dict]

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
        collection_metadata = BlogCollectionMetadata(**kwargs)
        collection_metadata.save(metadata_filepath)

        return

    @classmethod
    def load(cls, metadata_filepath: str) -> BlogCollectionMetadata:
        if metadata_filepath is None:
            raise ValueError("The metadata filepath was not correctly defined")

        if not os.path.abspath(metadata_filepath):
            raise IOError(
                f"Thet path \"{metadata_filepath}\" is not an absolute filepath.")

        if not os.path.exists(metadata_filepath):
            raise IOError(
                "The absolute path to the metadata is invalid or null")

        with open(metadata_filepath, 'r') as f:
            raw = f.read()

        return BlogCollectionMetadata.parse_raw(raw)

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
        self.metadata = metadata

    @property
    def name(self) -> str:
        return self._name

    @property
    def slug(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def summary(self) -> str:
        return self._summary

    @property
    def blogs(self) -> List:
        return

    @classmethod
    def load_collection(cls, blog_collection_path: str) -> BlogCollection:
        if blog_collection_path is None:
            raise ValueError("The blog collection path is invalid or null")

        if not os.path.isabs(blog_collection_path):
            raise IOError(f"The path {blog_collection_path} is not absolute")

        if os.path.isdir(blog_collection_path):
            return
        return
