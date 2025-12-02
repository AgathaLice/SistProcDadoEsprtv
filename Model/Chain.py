
from abc import ABC, abstractmethod


class Link(ABC):
    
    def __init__(self, next) -> None:
        self.next = next
        return None
    
    @abstractmethod
    def run(self, **kwargs):
        pass

    def last(self, **kwargs):
        if self.next == None:
            return kwargs
        else:
            print("ERRO NO LAST")

