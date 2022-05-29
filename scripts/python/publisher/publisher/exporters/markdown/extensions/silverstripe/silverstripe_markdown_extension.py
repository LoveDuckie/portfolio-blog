from typing import Any
from markdown import Extension


class SilverStripeMarkdownExtension(Extension):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)