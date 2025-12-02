
from Model.Chain import Link
from sklearn.preprocessing import StandardScaler

class EloEscala(Link):

    def run(self, **kwargs):

        if ('idAtletas' and 'npAtletas') in kwargs:
            escalonador = StandardScaler()
            escalAtletas = escalonador.fit_transform(kwargs['npAtletas'])
        else:
            print("ERRO, FALTA KWARGS PARA ESCALONAR")

        if self.next != None:
            return self.next.run(idAtletas=kwargs['idAtletas'],
                                 npAtletas=kwargs['npAtletas'],
                                 escalAtletas=escalAtletas,
                                 escalonador=escalonador)
        else:
            return self.last(idAtletas=kwargs['idAtletas'],
                             npAtletas=kwargs['npAtletas'],
                             escalAtletas=escalAtletas,
                             escalonador=escalonador)
