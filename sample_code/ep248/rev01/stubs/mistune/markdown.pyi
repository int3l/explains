from .renderer import BaseRenderer


class Markdown:
    def __init__(self, renderer: BaseRenderer) -> None: ...
    def __call__(self, s: str) -> str: ...
