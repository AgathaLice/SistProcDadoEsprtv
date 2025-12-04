
class Controller:
    
    def __init__(self, model) -> None:
        
        self.model = model

    def todosOsAtletas(self) -> list[dict]:
        return self.model.todosOsAtletas()
    
    def salvar(self, atleta) -> None:
        self.model.salvar(atleta)
        print(f'controller: {atleta}')
        return None
    
    def editarAtleta(self, id, event):
        return self.model.editarAtleta(id, event)
    
    def getGrafico(self):
        return self.model.getGrafico()
    
    def sair(self, e) -> None:
        self.model.sair(e)
