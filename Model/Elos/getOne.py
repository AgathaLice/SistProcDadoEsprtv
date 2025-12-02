
from Model.Chain import Link
import pymongo


class EloGetOne(Link):

    def run(self, **kwargs):

        if ('tabela' and 'id') in kwargs:
            atleta = kwargs['tabela'].find_one({'_id': id},
                                                          {'nome': 1,
                                                           'flexibilidade': 1,
                                                           'abdominaisEmUmMin': 1,
                                                           'arremecoDeBolaMed': 1,
                                                           'distEmSaltoHorz': 1
                                                       }
                                                      )

        if self.next != None:
            return self.next.run(atleta=atleta)
        else:
            return self.last(atleta=atleta)

