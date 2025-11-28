
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

"""
- Tela de menu,
- Tela de inserção de dados,
- Tela de carregamento,
- Tela de visualização de dados + gráfico,
- Tela de listagem de users,
- Tela de edição de dados.
"""

class View():
    
    def __init__(self, controller) -> None:

        self.controller = controller
        self.load = False
        
        self.root = ctk.CTk()
        self.root.title("Queimada") #provisório
        self.root.geometry("400x150") #vai ser zoomed dps

        self.telaMenu()
        self.telaInsertEdit()
        #self.telaLoad()
        self.telaData()
        self.telaList()
        
        self.root.bind("<Escape>", self.sair)

        self.root.mainloop()

    def telaMenu(self) -> None:
        
        menu = ctk.CTkFrame(self.root)

        menu.columnconfigure([0, 2],
                             weight=1)
        menu.columnconfigure(1,
                             weight=1)
        menu.rowconfigure([0, 3],
                          weight=3)
        menu.rowconfigure([1, 2],
                          weight=1)
        
    def telaInsertEdit(self) -> None:
            return None
        
    def telaLoad(self) -> None:
            return None
        
    def telaData(self) -> None:
            return None
        
    def telaList(self) -> None:
            return None
    
    def sair(self, e = None) -> None:
           self.controller.sair(e)
