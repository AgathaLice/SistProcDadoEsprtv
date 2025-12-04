
from Model.Chain import Link
import numpy as np


class EloNpArray(Link):

    def run(self, **kwargs):

        if ('listaAtletas' and
            'tabelaGrafico' and
            'tabelaBson') in kwargs:
            idAtletas = [atleta['nome'] for atleta in kwargs['listaAtletas']]
            dadosAtleta = [[
                atleta['flexibilidade'],
                atleta['abdominaisEmUmMin'],
                atleta['arremecoDeBolaMed'],
                atleta['distEmSaltoHorz']]
                for atleta in kwargs['listaAtletas']]

            npAtletas = np.array(dadosAtleta)

        if self.next != None:
            return self.next.run(idAtletas=idAtletas,
                                 npAtletas=npAtletas,
                                 tabelaGrafico=kwargs['tabelaGrafico'],
                                 tabelaBson=kwargs['tabelaBson'])
        else:
            return self.last(idAtletas=idAtletas,
                             npAtletas=npAtletas,
                             tabelaGrafico=kwargs['tabelaGrafico'],
                             tabelaBson=kwargs['tabelaBson'])
