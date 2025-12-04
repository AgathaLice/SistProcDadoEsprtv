
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from View.AtletaView import Atleta

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
        queimada = ctk.CTkLabel(self.menu, text='Queimada')
        insert = ctk.CTkButton(self.menu, text='Novo Atleta',
                               command=lambda: self.insertEdit.tkraise())  # ! Mudar dps
        graph = ctk.CTkButton(self.menu, text='Abrir Gráfico',
                              command=lambda: self.data.tkraise())
        lista = ctk.CTkButton(self.menu, text='Todos os Atletas',
                              command=lambda: self.lista.tkraise())
        sair = ctk.CTkButton(self.menu, text='Sair',
                             command=lambda: self.sair())

        queimada.grid(row=0, column=1)
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
        self.nomeEnt = ctk.CTkEntry(nomeFr)
        flexFr = ctk.CTkFrame(self.insertEdit)
        flexibilidadeLbl = ctk.CTkLabel(flexFr, text='Flexibilidade:')
        self.flexibilidadeEnt = ctk.CTkEntry(flexFr)
        abdomFr = ctk.CTkFrame(self.insertEdit)
        abdominaisEmUmMinLbl = ctk.CTkLabel(
            abdomFr, text='Abdominais em Um Minuto:')
        self.abdominaisEmUmMinEnt = ctk.CTkEntry(abdomFr)
        arremFr = ctk.CTkFrame(self.insertEdit)
        arremecoDeBolaMedLbl = ctk.CTkLabel(
            arremFr, text='Distância do Arremeço de Bola Medicinal:')
        self.arremecoDeBolaMedEnt = ctk.CTkEntry(arremFr)
        distFr = ctk.CTkFrame(self.insertEdit)
        distEmSaltoHorzLbl = ctk.CTkLabel(
            distFr, text='Distância em Salto Horizontal:')
        self.distEmSaltoHorzEnt = ctk.CTkEntry(distFr)
        insertEditBtsFr = ctk.CTkFrame(self.insertEdit)
        cancelar = ctk.CTkButton(
            insertEditBtsFr, text='Cancelar', command=self.fecharInsert)
        salvar = ctk.CTkButton(
            insertEditBtsFr, text='Salvar', command=self.salvar)

        titulo.grid(row=0, column=0, columnspan=1)
        nomeFr.grid(row=1, column=0, sticky='nse')
        nomeLbl.pack()
        self.nomeEnt.pack()
        flexFr.grid(row=2, column=0, sticky='nse')
        flexibilidadeLbl.pack()
        self.flexibilidadeEnt.pack()
        abdomFr.grid(row=3, column=0, sticky='nse')
        abdominaisEmUmMinLbl.pack()
        self.abdominaisEmUmMinEnt.pack()
        arremFr.grid(row=4, column=0, sticky='nse')
        arremecoDeBolaMedLbl.pack()
        self.arremecoDeBolaMedEnt.pack()
        distFr.grid(row=5, column=0, sticky='nse')
        distEmSaltoHorzLbl.pack()
        self.distEmSaltoHorzEnt.pack()
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

        self.data.rowconfigure(0,
                                weight=1)
        self.data.columnconfigure(0,
                                   weight=1)
        self.grafico()

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
        self.scrollFr = ctk.CTkScrollableFrame(self.lista)  # ! IMPORTANTE
        self.scrollFr.columnconfigure([0, 3],
                                 weight=1)
        self.scrollFr.columnconfigure(1,
                                 weight=6)
        self.scrollFr.columnconfigure(2,
                                 weight=2)
        
        self.buildScrllFr()

        menu.grid(row=1, column=1)
        titulo.grid(row=1, column=2, sticky='nsw')
        newAtleta.grid(row=2, column=1)
        self.scrollFr.grid(row=3, column=1, columnspan=2, sticky='nsew')

    def salvar(self) -> None:
        atleta = Atleta(
            self.nomeEnt.get(),
            self.flexibilidadeEnt.get(),
            self.abdominaisEmUmMinEnt.get(),
            self.arremecoDeBolaMedEnt.get(),
            self.distEmSaltoHorzEnt.get()
        )
        self.controller.salvar(atleta)
        self.fecharInsert()

    def fecharInsert(self) -> None:
        self.nomeEnt.delete(0, ctk.END)
        self.flexibilidadeEnt.delete(0, ctk.END)
        self.abdominaisEmUmMinEnt.delete(0, ctk.END)
        self.arremecoDeBolaMedEnt.delete(0, ctk.END)
        self.distEmSaltoHorzEnt.delete(0, ctk.END)
        self.menu.tkraise()
    
    def updateLista(self):
        for label in self.scrollFr.winfo_children():
            label.destroy()
        self.buildScrllFr()
    
    def buildScrllFr(self):
        atletas = self.controller.todosOsAtletas()
        index = 0
        for atleta in atletas:
            atletaLbl = ctk.CTkLabel(self.scrollFr,
                                     text=f'{atleta['nome']}')
            atletaLbl.bind("<Button-1>",
                           lambda event, id=atleta['nome']: self.editarAtleta(id, event))
            atletaLbl.grid(row=index, column=1)
            index += 1


    def editarAtleta(self, id, event) -> None:  # ! FIX
        atletaEditavel = self.controller.editarAtleta(id, event)
        self.nomeEnt.delete(0, ctk.END)
        self.flexibilidadeEnt.delete(0, ctk.END)
        self.abdominaisEmUmMinEnt.delete(0, ctk.END)
        self.arremecoDeBolaMedEnt.delete(0, ctk.END)
        self.distEmSaltoHorzEnt.delete(0, ctk.END)

        self.nomeEnt.insert(0, atletaEditavel['nome'])
        self.flexibilidadeEnt.insert(0, atletaEditavel['flexibilidade'])
        self.abdominaisEmUmMinEnt.insert(0, atletaEditavel['abdominaisEmUmMin'])
        self.arremecoDeBolaMedEnt.insert(0, atletaEditavel['arremecoDeBolaMed'])
        self.distEmSaltoHorzEnt.insert(0, atletaEditavel['distEmSaltoHorz'])

        return None
    
    def grafico(self):
        imagem = self.controller.getGrafico() 
        canvaGrafico = FigureCanvasTkAgg(imagem, master=self.data)
        tkGrafico = canvaGrafico.get_tk_widget()
        tkGrafico.grid(row=0, column=0, sticky='nsew')

    def raiseInsertEdit(self, nome) -> None:  # TODO
        return None

    def sair(self, e=None) -> None:
        self.root.destroy()
        self.controller.sair(e)

