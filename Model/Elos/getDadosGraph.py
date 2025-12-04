
from Model.Chain import Link
import pymongo


class EloGetDataGraph(Link):

    def run(self, **kwargs):
#TODO  fzr find dos ids e pegar os nomes no lugar dos ids
        if ('idAtletas' and
            'npAtletas' and
            'grupos' and
            'escalonador' and
            'kmeansSalvo' and
            'tabelaGrafico' and
            'tabelaBson') in kwargs:
            dadosGrafico = {
                'idsLista': list(kwargs['idAtletas']),
                'dadosLista': kwargs['escalAtletas'].tolist(),
                'clusters': kwargs['grupos'].tolist()
            }
            kwargs['tabelaGrafico'].insert_one(dadosGrafico)
            dadosAtletas = list(kwargs['tabelaGrafico'].find({}))
            
        else:
            print('ERRO NA BUSCA PARA GRAFICO')

        if self.next != None:
            return self.next.run(dadosAtletas=dadosAtletas,
                                 kmeansSalvo=kwargs['kmeansSalvo'],
                                 escalonador=kwargs['escalonador'])
        else:
            return self.last(dadosAtletas=dadosAtletas,
                             kmeansSalvo=kwargs['kmeansSalvo'],
                             escalonador=kwargs['escalonador'])

