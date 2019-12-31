from enum import Enum
from enum import auto


class Request:
    def __init__(self, plan: str, entame_free: str):
        self.plan = plan
        self.entame_free = entame_free

