
from Model.Chain import Link
import pymongo

class EloSalvar(Link):

    def run(self, **kwargs):

        if ('atleta' and 'tabela') in kwargs:
            atleta = kwargs['atleta'].__dict__
            kwargs['tabela'].insert_one(atleta)
            print(atleta)
        else:
            print("ERRO, FALTA KWARGS PARA SALVAR")

        if self.next != None:
            return self.next.run(atleta=kwargs['atleta'],
                                 tabela=kwargs['tabela'])
        else:
            return self.last(atleta=kwargs['atleta'],
                             tabela=kwargs['tabela'])