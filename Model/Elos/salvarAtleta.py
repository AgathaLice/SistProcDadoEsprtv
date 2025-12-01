
from Model.Chain import Link
import pymongo

class EloSalvar(Link):

    def run(self, data, tabela):

        atleta = data.__dict__
        tabela.insert_one(atleta)

        return self.next.run()
