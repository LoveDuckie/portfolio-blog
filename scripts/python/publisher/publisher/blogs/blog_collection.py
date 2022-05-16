import os, sys
from pydantic import BaseModel

class BlogCollection(BaseModel):
    def __init__(self, **kwargs) -> None:
        for key in kwargs:
            self.__dict__[key] = kwargs[key]
        super().__init__()
        
    @property.getter
    def blog_collection_name(self):
        return self.name
    
    @property.getter
    def blog_collection_slug(self):
        return self.name
    
    @property.getter
    def blog_collection_description(self) -> str:
        return self.description
    
    @property.getter
    def blog_collection_summary(self) -> str:
        return self.summary

    @classmethod
    def get_all_blog_collections(cls, collections_path):
        if collections_path is None or collections_path == '':
            raise ValueError("The blogs path was nto defined")

        if not os.path.exists(collections_path):
            raise IOError(f"Failed to find the path \"{collections_path}\"")

        for root, dirs, files in os.walk(collections_path,topdown=False):
            for file in files:
                if os.path.isfile(file):
                    return
                
        return []
