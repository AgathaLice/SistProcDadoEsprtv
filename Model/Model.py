
from sys import exit

import pymongo

from Model.Elos.salvarAtleta import EloSalvar
from Model.Elos.getAtletas import EloGetAll
from Model.Elos.idsListNparray import EloNpArray
from Model.Elos.escalonarDados import EloEscala
from Model.Elos.aplicarPeso import EloPeso
from Model.Elos.InitKmeans import EloInitKmeans
from Model.Elos.getOne import EloGetOne
from Model.Elos.decomposition import EloDecomposicao
from Model.Elos.getDadosGraph import EloGetDataGraph
from Model.Elos.graficar import EloGrafico
from Model.Elos.updateKmeans import EloUpdateKmeans

'''
- #*verificar dados (opcional)
- #!salvar no bd
- #!criar e treinar o KMeans
- #!pegar todos os dados no bd
- atualizar o KMeans
- #!diminuir as dimensões dos dados
- criar gráfico com os dados
- #!salvar os dados de treinamento no mongodb (para atualizar kmeans posteriormente)
'''

class Model:

    def __init__(self) -> None:
        dbMain = pymongo.MongoClient("mongodb://localhost:27017/")
        queimada = dbMain["Queimada"]
        self.atletas = queimada["Atletas"]
        self.dadosTreino = queimada["dadosTreino"]
        self.dadosBson = queimada["treinoBson"]
        self.dadosGrafico = queimada["DadosGrafico"]
        self.inicializacao()

    def inicializacao(self) -> None:
        plotar = EloGrafico(None)
        decomposicao = EloDecomposicao(plotar)
        getDadosGraph = EloGetDataGraph(decomposicao)
        eloInitKmeans = EloInitKmeans(getDadosGraph)
        eloPeso = EloPeso(eloInitKmeans)
        eloEscalonar = EloEscala(eloPeso)
        eloNpArray = EloNpArray(eloEscalonar)
        eloGetAll = EloGetAll(eloNpArray)

        retorno = eloGetAll.run(tabela=self.dadosTreino,
                                tabelaGrafico=self.dadosGrafico,
                                tabelaBson=self.dadosBson)
        self.grafico = retorno['img']
        self.kmeans = retorno['kmeans']
        self.escal = retorno['escalonador']
        self.pca = retorno['pca']
        self.axes=retorno['grafico']

        return None
    
    def getGrafico(self):
        return self.grafico

    def todosOsAtletas(self):
        eloGetAll = EloGetAll(None)

        lista = eloGetAll.run(tabela=self.dadosTreino,
                           tabelaGrafico=self.dadosGrafico,
                           tabelaBson=self.dadosBson)
        if lista == None:
            lista = {'listaAtletas': []}
        lista = lista['listaAtletas']
        return lista

    def salvar(self, atleta):
        eloSalvar = EloSalvar(None)
        return eloSalvar.run(atleta=atleta,
                             tabela=self.dadosTreino,
                             kmeans=self.kmeans,
                             pca=self.pca,
                             escal=self.escal,
                             grafico=self.grafico)
                             

    def editarAtleta(self, id, event):
        eloUm = EloGetOne(None)
        print(eloUm.run(tabela=self.dadosTreino, id=id))  # TODO
    

    def sair(self, e) -> None:
        exit()
        return None
