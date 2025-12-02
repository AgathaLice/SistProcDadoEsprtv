
from Model.Chain import Link
import pickle
from bson.binary import Binary 
import pymongo
import numpy


class EloSalvarTreino(Link):

    def run(self, **kwargs):

        if ('idAtletas' and
            'npAtletas' and
            'grupos' and
            'escalonador' and
            'kmeansSalvo' and
            'tabelaGrafico' and
            'tabelaBson') in kwargs:
            kmeans = pickle.dumps(kwargs['kmeansSalvo'])
            escalonador = pickle.dumps(kwargs['escalonador'])
            dadosBson = {
                'kmeans': Binary(kmeans),
                'escalonador': Binary(escalonador)
            }
            kwargs['tabelaBson'].insert_one(dadosBson)
            print(dadosBson)
            dadosGrafico = {
                'idsLista': list(kwargs['idAtletas']),
                'dadosLista': kwargs['npAtletas'].tolist(),
                'clusters': kwargs['grupos'].tolist()
            }
            kwargs['tabelaGrafico'].insert_one(dadosGrafico)
        else:
            print("ERRO, FALTA KWARGS PARA SALVAR BSON")

        if self.next != None:
            return self.next.run(None)
        else:
            return self.last()
