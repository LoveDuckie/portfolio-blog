import os

class BlogCollectionMetadata:
    def __init__(self) -> None:
        pass

class BlogCollection:
    def __init__(self, **kwargs) -> None:
        for key in kwargs:
            self.__dict__[key] = kwargs[key]
        super().__init__()
        
    @property.getter
    def _name(self):
        return self.name
    
    @property.getter
    def _slug(self):
        return self.name
    
    @property.getter
    def _description(self) -> str:
        return self.description
    
    @property.getter
    def _summary(self) -> str:
        return self.summary