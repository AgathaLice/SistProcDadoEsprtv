
from Model.Chain import Link


class EloPeso(Link):

    def run(self, **kwargs):

        if ('idAtletas' and
            'npAtletas' and
            'escalAtletas' and
            'escalonador') in kwargs:
            for atleta in kwargs['escalAtletas']:
                atleta[2] *= 1.6 # Aplica peso de 60% ao arremeço
                atleta[3] *= 1.3 # Aplica peso de 30% ao salto
        else:
            print("ERRO, FALTA KWARGS PARA PESAR")

        if self.next != None:
            return self.next.run(idAtletas=kwargs['idAtletas'],
                                 npAtletas=kwargs['npAtletas'],
                                 escalAtletas=kwargs['escalAtletas'],
                                 escalonador=kwargs['escalonador'])
        else:
            return self.last(idAtletas=kwargs['idAtletas'],
                             npAtletas=kwargs['npAtletas'],
                             escalAtletas=kwargs['escalAtletas'],
                             escalonador=kwargs['escalonador'])
