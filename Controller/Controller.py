
class Controller:
    
    def __init__(self, model) -> None:
        
        self.model = model

    def todosOsAtletas(self) -> list[dict]:
        return self.model.todosOsAtletas()
    
    def sair(self, e) -> None:
        self.model.sair(e)
