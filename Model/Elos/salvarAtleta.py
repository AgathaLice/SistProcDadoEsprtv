
from Model.Chain import Link
import pymongo

class EloSalvar(Link):

    def run(self, **kwargs):

        if ('atleta' and 'tabela' and 'kmeans' and 'escal' and 'pca' and 'grafico') in kwargs:
            atleta = kwargs['atleta'].__dict__
            kwargs['tabela'].insert_one(atleta)
            print(atleta)
        else:
            print("ERRO, FALTA KWARGS PARA SALVAR")

        if self.next != None:
            return self.next.run(atleta=atleta,
                                 tabela=kwargs['tabela'],
                                 kmeans=kwargs['kmeans'],
                                 escal=kwargs['escal'],
                                 pca=kwargs['pca'],
                                 grafico=kwargs['grafico'])
        else:
            return self.last(atleta=atleta,
                             tabela=kwargs['tabela'],
                             kmeans=kwargs['kmeans'],
                             escal=kwargs['escal'],
                             pca=kwargs['pca'],
                             grafico=kwargs['grafico'])