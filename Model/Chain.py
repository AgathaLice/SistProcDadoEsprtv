
from abc import ABC, abstractmethod


class Link(ABC):
    
    def __init__(self, next) -> None:
        self.next = next
        return None
    
    @abstractmethod
    def run(self, data):
        pass


class Last(Link):
    
    def __init__(self, *args):
        return args