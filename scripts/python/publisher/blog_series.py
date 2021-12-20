import os, sys
class BlogSeries(object):
    def __init__(self, **kwargs) -> None:
        for key in kwargs:
            value = kwargs[key]
        super().__init__()

    @classmethod
    def get_series(cls, blogs_path):
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
