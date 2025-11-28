
class Controller:
    
    def __init__(self, model) -> None:
        
        self.model = model
    
    def sair(self, e) -> None:
        self.model.sair(e)
