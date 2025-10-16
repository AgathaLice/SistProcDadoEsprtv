
# -- Imports --
from abc import ABC, abstractmethod


class Link(ABC):
    
    def __init__(self, next) -> None:
        self.next = next
        return None
    
    @abstractmethod
    def run(self):
        pass


class Last:
    
    def __init__(self, retorno):
        return retorno