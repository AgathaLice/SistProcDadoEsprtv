

class Link:
    
    def __init__(self, next) -> None:
        self.next = next
        return None
    
    def run(self):
        return self.next()
    



class Last:
    
    def __init__(self, retorno):
        return retorno