
from Model.Chain import Link
import pymongo


class EloGetAll(Link):

    def run(self, **kwargs):

        if ('tabela' and
            'tabelaGrafico' and
            'tabelaBson') in kwargs:
            listaAtletas = list(kwargs['tabela'].find({},
                                                      {'nome': 1,
                                                       'flexibilidade': 1,
                                                       'abdominaisEmUmMin': 1,
                                                       'arremecoDeBolaMed': 1,
                                                       'distEmSaltoHorz': 1
                                                       }
                                                      )
                                )

        if self.next != None:
            return self.next.run(listaAtletas=listaAtletas,
                                 tabelaGrafico=kwargs['tabelaGrafico'],
                                 tabelaBson=kwargs['tabelaBson'])
        else:
            return self.last(listaAtletas=listaAtletas,
                             tabelaGrafico=kwargs['tabelaGrafico'],
                             tabelaBson=kwargs['tabelaBson'])

