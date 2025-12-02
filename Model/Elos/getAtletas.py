
from Model.Chain import Link
import pymongo


class EloGetAll(Link):

    def run(self, **kwargs) -> dict | None:

        if 'tabela' in kwargs:
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
            return self.next.run(listaAtletas=listaAtletas)
        else:
            return self.last(listaAtletas=listaAtletas)

