import os, sys

class BlogSeries(object):
    def __init__(self, **kwargs) -> None:
        for key in kwargs:
            self.__dict__[key] = kwargs[key]
        super().__init__()
        
    @property.getter
    def blog_series_name(self):
        return self.name
    @property.getter
    def blog_series_slug(self):
        return self.name
    
    
    @property.getter
    def blog_series_description(self):
        return self.description
    @property.getter
    def blog_series_summary(self):
        return self.summary

        

    @classmethod
    def get_blog_series(cls, blogs_path):
        if blogs_path is None or blogs_path == '':
            raise ValueError("The blogs path was nto defined")
        
        if not os.path.exists(blogs_path):
            raise IOError(f"Failed to find the path \"{blogs_path}\"")
        
        all_series = []
        
        for root, dirs, files in os.walk(blogs_path,topdown=False):
            for file in files:
                if os.path.isfile(file):
                    return
        return all_series
