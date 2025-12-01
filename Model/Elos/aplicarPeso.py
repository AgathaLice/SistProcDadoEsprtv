
from Model.Chain import Link


class EloPeso(Link):

    def run(self, idsAtleta, npAtletas, escalAtletas):
        
        for atleta in escalAtletas:
            atleta[2] *= 1.6
            atleta[3] *= 1.3

        return self.next.run(idsAtleta, npAtletas, escalAtletas)