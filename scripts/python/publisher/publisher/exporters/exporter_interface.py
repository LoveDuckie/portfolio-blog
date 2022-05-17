

from abc import abstractmethod

from publisher.blogs.blog import Blog


class ExporterInterface:
    def __init__(self, blog: Blog) -> None:
        if blog is None:
            raise ValueError("The blog is ivnalid or null")
        self.blog = blog

    def load(self):
        return

    @abstractmethod
    def export(self):
        return
