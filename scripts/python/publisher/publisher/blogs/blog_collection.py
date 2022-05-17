from __future__ import annotations
import os
from typing import Any, List, Optional
from pydantic import BaseModel


class BlogCollectionMetadata(BaseModel):
    name: str
    description: str
    summary: str
    filepath: Optional[str]
    slug: str

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

    @classmethod
    def load_metadata(cls, metadata_filepath: str) -> BlogCollectionMetadata:
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

        return cls.parse_raw(raw)
    
    
    def save(self, filepath: str = None):
        pass


class BlogCollection:
    def __init__(self, metadata: BlogCollectionMetadata) -> None:
        super().__init__()
        if metadata is None:
            raise ValueError("The metadata is invalid or null")
        self.metadata = metadata

    @property
    def _name(self) -> str:
        return self.name

    @property
    def _slug(self) -> str:
        return self.name

    @property
    def _description(self) -> str:
        return self.description

    @property
    def _summary(self) -> str:
        return self.summary
    
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
