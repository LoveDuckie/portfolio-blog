from typing import Any
import os, sys
import json
class Blog(object):
    def __init__(self, **kwargs) -> None:
        self.properties = {}
        for key in kwargs:
            self.__dict__[key] = kwargs[key]
        super().__init__()

    @property.getter
    def blog_name(self):
        return 
    
    @property.getter
    def blog_slug(self):
        return

    @property.getter
    def blog_description():
        return

    def __getattribute__(self, __name: str) -> Any:
        return super().__getattribute__(__name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        return super().__setattr__(__name, __value)

    def __getitem__(self, key):
        return self.__dict__[key]
    
    def get_blog_series():
        return
    
    @classmethod
    def load_blog(cls, blog_path):
        if blog_path is None or blog_path == '':
            raise ValueError("The blog path is invalid or null")
        
        if not os.path.isdir(blog_path):
            raise IOError(f'The path \"{blog_path}\" is not a valid directory. It must be a directory.')
        
        blog_metadata_filepath = os.path.join(blog_path, "blog.json")
        
        if not os.path.isfile(blog_metadata_filepath):
            raise IOError(f'The file \"{blog_metadata_filepath}\" is not a valid file')
        
        if not os.path.exists(blog_metadata_filepath):
            raise Exception(f'Unable to find the metadata file \"{blog_metadata_filepath}\".')
        
        blog_metadata = None
        
        with open(blog_metadata_filepath, 'r') as file:
            blog_metadata = file.read()
            if blog_metadata is None:
                raise ValueError("The blog metadata is invalid or null")
        
        if blog_metadata is None:
            raise ValueError("The loaded metadata is invalid or null")
        
        loaded_metadata = json.loads(blog_metadata)
        if loaded_metadata is None:
            raise ValueError("")
        
        return cls(loaded_metadata)