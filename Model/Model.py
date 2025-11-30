
# Imports
from Model.Chain import Link, Last

from sys import exit
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

import pymongo
import joblib
import bson.binary


class Model:
    
    def __init__(self) -> None:
        dbMain = pymongo.MongoClient("mongodb://localhost:27017/")
        queimada = dbMain["Queimada"]
        self.atletas = queimada["atletas"]
    
    def todosOsAtletas(self) -> list[dict]:
        #!Find...
        #! TEMPORÁRIO --=PARA TESTE=--
        atletas = [{"_id": "a1", "nome": "nome1", "idade": 1}, {"_id": "a2", "nome": "nome2", "idade": 2},
                   {"_id": "a3", "nome": "nome3", "idade": 3}, {"_id": "a4", "nome": "nome4", "idade": 4},
                   {"_id": "a5", "nome": "nome5", "idade": 5}, {"_id": "a6", "nome": "nome6", "idade": 6}]
        return atletas
    

    
    def sair(self, e):
        exit()
    
    