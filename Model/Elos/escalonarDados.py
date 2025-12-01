
from Model.Chain import Link
from sklearn.preprocessing import StandardScaler


class EloEscala(Link):

    def run(self, idsAtleta, npAtletas):

        escalonador = StandardScaler()
        escalAtletas = escalonador.fit_transform(npAtletas)

        return self.next.run(idsAtleta, npAtletas, escalAtletas)