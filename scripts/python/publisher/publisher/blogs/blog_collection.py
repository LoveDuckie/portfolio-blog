import os, sys

class BlogCollection(object):
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
    def blog_collection_description(self):
        return self.description
    
    @property.getter
    def blog_collection_summary(self):
        return self.summary

    @classmethod
    def get_all_blog_collection(cls, blogs_path):
        if blogs_path is None or blogs_path == '':
            raise ValueError("The blogs path was nto defined")

        if not os.path.exists(blogs_path):
            raise IOError(f"Failed to find the path \"{blogs_path}\"")

        for root, dirs, files in os.walk(blogs_path,topdown=False):
            for file in files:
                if os.path.isfile(file):
                    return
        return []
