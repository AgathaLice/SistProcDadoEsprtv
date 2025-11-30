
# Imports
from Model.Chain import Link, Last

from sys import exit
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

import pymongo as mog
import joblib
import bson.binary


class Model:
    
    def __init__(self) -> None:
        return None
    
    def todosOsAtletas(self) -> list[dict] | None:
        #!Find...
        #! TEMPORÁRIO --=PARA TESTE=--
        atletas = [{"nome": "nome1", "idade1": 1}, {"nome": "nome2", "idade2": 2},
                   {"nome": "nome3", "idade3": 3}, {"nome": "nome4", "idade4": 4},
                   {"nome": "nome5", "idade5": 5}, {"nome": "nome6", "idade6": 6}]
        return atletas
    

    
    def sair(self, e):
        exit()
    
    