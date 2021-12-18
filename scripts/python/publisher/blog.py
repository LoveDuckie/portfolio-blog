class Blog(object):
    def __init__(self, **kwargs) -> None:
        self.properties = {}
        super().__init__()

    @property.getter
    def blog_name():
        return
    
    @property.getter
    def blog_slug():
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