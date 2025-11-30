
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

'''
- Tela de menu,
- Tela de inserção de dados,
- Tela de carregamento,
- Tela de visualização de dados + gráfico,
- Tela de listagem de users,
- Tela de edição de dados.
'''


class View():

    def __init__(self, controller) -> None:

        self.controller = controller
        self.iniciaLoad = False

        self.root = ctk.CTk()
        self.root.title('Queimada')  # provisório
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.telaMenu()
        self.telaInsertEdit()
        self.telaLoad()
        self.telaData()
        self.telaLista()

        self.root.bind('<Escape>', self.sair)

        self.root.state('zoomed')
        self.menu.tkraise()
        self.root.mainloop()

    def telaMenu(self) -> None:
        self.menu = ctk.CTkFrame(self.root)
        self.menu.grid(row=0, column=0, sticky='nsew')

        self.menu.columnconfigure([0, 1, 2],
                                  weight=1)
        self.menu.rowconfigure(0,
                               weight=3)
        self.menu.rowconfigure([1, 2, 3, 4],
                               weight=1)

        insert = ctk.CTkButton(self.menu, text='Novo Atleta',
                               command=lambda: self.insertEdit.tkraise())  # ! Mudar dps
        graph = ctk.CTkButton(self.menu, text='Abrir Gráfico',
                              command=lambda: self.data.tkraise())
        lista = ctk.CTkButton(self.menu, text='Todos os Atletas',
                              command=lambda: self.lista.tkraise())
        sair = ctk.CTkButton(self.menu, text='Sair',
                             command=lambda: self.sair())

        #! Logo aq
        insert.grid(row=1, column=1)
        graph.grid(row=2, column=1)
        lista.grid(row=3, column=1)
        sair.grid(row=4, column=1)

    def telaInsertEdit(self) -> None:
        self.insertEdit = ctk.CTkFrame(self.root)
        self.insertEdit.grid(row=0, column=0, sticky='nsew')

        self.insertEdit.columnconfigure([0, 1],
                                        weight=1)
        self.insertEdit.rowconfigure(0,
                                     weight=3)
        self.insertEdit.rowconfigure([1, 2, 3, 4, 5, 6],
                                     weight=1)

        titulo = ctk.CTkLabel(self.insertEdit, text='Insira suas Informações')
        nomeFr = ctk.CTkFrame(self.insertEdit)
        nomeLbl = ctk.CTkLabel(nomeFr, text='Nome:')
        nomeEnt = ctk.CTkEntry(nomeFr)
        idadeFr = ctk.CTkFrame(self.insertEdit)
        idadeLbl = ctk.CTkLabel(idadeFr, text='Idade:')
        idadeEnt = ctk.CTkEntry(idadeFr)
        flexFr = ctk.CTkFrame(self.insertEdit)
        flexibilidadeLbl = ctk.CTkLabel(flexFr, text='Flexibilidade:')
        flexibilidadeEnt = ctk.CTkEntry(flexFr)
        abdomFr = ctk.CTkFrame(self.insertEdit)
        abdominaisEmUmMinLbl = ctk.CTkLabel(
            abdomFr, text='Abdominais em Um Minuto:')
        abdominaisEmUmMinEnt = ctk.CTkEntry(abdomFr)
        arremFr = ctk.CTkFrame(self.insertEdit)
        arremecoDeBolaMedLbl = ctk.CTkLabel(
            arremFr, text='Distância do Arremeço de Bola Medicinal:')
        arremecoDeBolaMedEnt = ctk.CTkEntry(arremFr)
        distFr = ctk.CTkFrame(self.insertEdit)
        distEmSaltoHorzLbl = ctk.CTkLabel(
            distFr, text='Distância em Salto Horizontal:')
        distEmSaltoHorzEnt = ctk.CTkEntry(distFr)
        insertEditBtsFr = ctk.CTkFrame(self.insertEdit)
        cancelar = ctk.CTkButton(insertEditBtsFr, text='Cancelar')
        salvar = ctk.CTkButton(insertEditBtsFr, text='Salvar')

        titulo.grid(row=0, column=0, columnspan=1)
        nomeFr.grid(row=1, column=0, sticky='nse')
        nomeLbl.pack()
        nomeEnt.pack()
        idadeFr.grid(row=1, column=1)
        idadeLbl.pack()
        idadeEnt.pack()
        flexFr.grid(row=2, column=0, sticky='nse')
        flexibilidadeLbl.pack()
        flexibilidadeEnt.pack()
        abdomFr.grid(row=3, column=0, sticky='nse')
        abdominaisEmUmMinLbl.pack()
        abdominaisEmUmMinEnt.pack()
        arremFr.grid(row=4, column=0, sticky='nse')
        arremecoDeBolaMedLbl.pack()
        arremecoDeBolaMedEnt.pack()
        distFr.grid(row=5, column=0, sticky='nse')
        distEmSaltoHorzLbl.pack()
        distEmSaltoHorzEnt.pack()
        insertEditBtsFr.grid(row=6, column=1, sticky='nsw')
        cancelar.pack()
        salvar.pack()

    def telaLoad(self) -> None:
        self.load = ctk.CTkFrame(self.root)
        self.load.grid(row=0, column=0, sticky='nsew')

        self.load.columnconfigure([0, 2],
                                  weight=1)
        self.load.columnconfigure(1,
                                  weight=8)
        self.load.rowconfigure([0, 2],
                               weight=4)
        self.load.rowconfigure(1,
                               weight=1)

        loading = ctk.CTkLabel(self.load, text='Carregando...')
        self.barra = ctk.CTkProgressBar(
            self.load, orientation='horizontal', mode='indeterminate')

        loading.grid(row=0, column=1)
        self.barra.grid(row=1, column=1)

    def telaData(self) -> None:
        self.data = ctk.CTkFrame(self.root)
        self.data.grid(row=0, column=0, sticky='nsew')

    def telaLista(self) -> None:
        self.lista = ctk.CTkFrame(self.root)
        self.lista.grid(row=0, column=0, sticky='nsew')

        self.lista.rowconfigure([0, 1, 2, 4],
                                weight=1)
        self.lista.rowconfigure(3,
                                weight=6)
        self.lista.columnconfigure([0, 1, 3],
                                   weight=1)
        self.lista.columnconfigure(2,
                                   weight=7)

        menu = ctk.CTkButton(self.lista, text="Menu",
                             command=lambda: self.menu.tkraise())
        titulo = ctk.CTkLabel(self.lista, text="Listagem")
        newAtleta = ctk.CTkButton(self.lista, text="Novo Atleta",
                                 command=lambda: self.insertEdit.tkraise())
        listagemFr = ctk.CTkScrollableFrame(self.lista) #!IMPORTANTE

        

        menu.grid(row=1, column=1)
        titulo.grid(row=1, column=2, sticky='nsw')
        newAtleta.grid(row=2, column=1)
        listagemFr.grid(row=3, column=1, columnspan=2, sticky='nsew')

    def raiseInsertEdit(self, nome) -> None:  # TODO
        return None

    def sair(self, e=None) -> None:
        self.controller.sair(e)


class Atleta():

    def __init__(self, nome, idade,
                 flexibilidade,
                 abdominaisEmUmMin,
                 arremecoDeBolaMed,
                 distEmSaltoHorz) -> None:
        self.nome = nome
        self.idade = idade
        self.flexibilidade = flexibilidade
        self.abdominaisEmUmMin = abdominaisEmUmMin
        self.arremecoDeBolaMed = arremecoDeBolaMed
        self.distEmSaltoHorz = distEmSaltoHorz
