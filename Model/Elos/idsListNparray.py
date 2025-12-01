
from Model.Chain import Link
import numpy as np


class EloNpArray(Link):

    def run(self, listaAtletas):

        idsAtleta = [atleta['_id'] for atleta in listaAtletas]
        dadosAtleta = [[
            atleta['flexibilidade'],
            atleta['abdominais'],
            atleta['arremeco'],
            atleta['saltoHorizontal']]
            for atleta in listaAtletas]

        npAtletas = np.array(dadosAtleta)

        return self.next.run(idsAtleta, npAtletas)
