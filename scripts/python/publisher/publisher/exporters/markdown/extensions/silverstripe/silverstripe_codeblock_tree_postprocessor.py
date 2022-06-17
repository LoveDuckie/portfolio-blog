from typing import Any
from markdown.treeprocessors import Treeprocessor

class SilverStripeCodeblockTreePostprocess(Treeprocessor):
    def __init__(self, md: Any | None = ...) -> None:
        super().__init__(md)