
from Model.Chain import Link
import pymongo


class EloGetAll(Link):

    def run(self, tabela) -> list | None:

        listaAtletas = list(tabela.find({}, {'nome': 1,
                                             'idade': 1,
                                             'flexibilidade': 1,
                                             'abdominais': 1,
                                             'arremeco': 1,
                                             'saltoHorizontal': 1
                                             }
                                       )
                           )

        return self.next.run(listaAtletas)
