
class Controller:
    
    def __init__(self, model) -> None:
        
        self.model = model

    def todosOsAtletas(self) -> list[dict]:
        return self.model.todosOsAtletas()
    
    def salvar(self, atleta) -> None:
        # self.model.salvar(atleta)
        print(atleta)
        return None
    
    def sair(self, e) -> None:
        self.model.sair(e)
