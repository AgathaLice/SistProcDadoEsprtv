
from sys import exit

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

import pymongo

from Model.Elos.salvarAtleta import EloSalvar

from Model.Elos.getAtletas import EloGetAll
from Model.Elos.idsListNparray import EloNpArray
from Model.Elos.escalonarDados import EloEscala
from Model.Elos.aplicarPeso import EloPeso
from Model.Elos.InitKmeans import EloInitKmeans
from Model.Elos.salvarTreino import EloSalvarTreino

'''
- #*verificar dados (opcional)
- #!salvar no bd
- #!criar e treinar o KMeans
- #!pegar todos os dados no bd
- atualizar o KMeans
- diminuir as dimensões dos dados
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

    def inicializacao(self):
        eloInitKmeans = EloInitKmeans(None)
        '''
         Vai retornar em "dados": 
           - lista de ids,
           - lista de dados num nparray,
           - o escalonador,
           - grupos(classificação),
           - o kmeans para salvar (dps do fit)
        '''
        eloPeso = EloPeso(eloInitKmeans)
        eloEscalonar = EloEscala(eloPeso)
        eloNpArray = EloNpArray(eloEscalonar)
        eloGetTrainData = EloGetAll(eloNpArray)

        dados = eloGetTrainData.run(tabela=self.dadosTreino)
        self.salvarTreino(dados)

    def salvarTreino(self, dados):
        eloSalvarTreino = EloSalvarTreino(None)
        eloSalvarTreino.run(idAtletas=dados['idAtletas'],
                            npAtletas=dados['npAtletas'],
                            escalonador=dados['escalonador'],
                            grupos=dados['grupos'],
                            kmeansSalvo=dados['kmeansSalvo'],
                            tabelaGrafico=self.dadosGrafico,
                            tabelaBson=self.dadosBson)

    def todosOsAtletas(self) -> list[dict]:
        #!Find...
        #! TEMPORÁRIO --=PARA TESTE=--
        listagem = [{"_id": "a1", "nome": "nome1", "idade": 1}, {"_id": "a2", "nome": "nome2", "idade": 2},
                    {"_id": "a3", "nome": "nome3", "idade": 3}, {
                        "_id": "a4", "nome": "nome4", "idade": 4},
                    {"_id": "a5", "nome": "nome5", "idade": 5}, {"_id": "a6", "nome": "nome6", "idade": 6}]

        return listagem

    def salvar(self, atleta):
        tabela = self.atletas
        eloSalvar = EloSalvar(None)
        return eloSalvar.run(atleta=atleta, tabela=tabela)

    def sair(self, e) -> None:
        exit()
        return None
