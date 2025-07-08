class GameProcessNotFoundError(Exception):
    pass


class MemoryValueNotFoundError(Exception):
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern
