
from sys import exit

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


import pymongo
import joblib
import bson.binary

'''
- #*verificar dados (opcional)
- #!salvar no bd
- criar e treinar o KMeans
- #!pegar todos os dados no bd
- atualizar o KMeans
- diminuir as dimensões dos dados
- criar gráfico com os dados
- salvar os dados de treinamento no mongodb (para atualizar kmeans posteriormente)
'''

class Model:
    
    def __init__(self) -> None:
        dbMain = pymongo.MongoClient("mongodb://localhost:27017/")
        queimada = dbMain["Queimada"]
        self.atletas = queimada["atletas"]
    
    def todosOsAtletas(self) -> list[dict]:
        #!Find...
        #! TEMPORÁRIO --=PARA TESTE=--
        listagem = [{"_id": "a1", "nome": "nome1", "idade": 1}, {"_id": "a2", "nome": "nome2", "idade": 2},
                   {"_id": "a3", "nome": "nome3", "idade": 3}, {"_id": "a4", "nome": "nome4", "idade": 4},
                   {"_id": "a5", "nome": "nome5", "idade": 5}, {"_id": "a6", "nome": "nome6", "idade": 6}]
        
        return listagem
    
    def salvar(self, atleta) -> None:
        atleta = atleta.__dict__
        self.atletas.insert_one(atleta)
    
    def sair(self, e) -> None:
        exit()
        return None

    
    
