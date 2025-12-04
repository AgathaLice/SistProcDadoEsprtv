
from Model.Chain import Link
import numpy as np

class EloUpdateKmeans(Link):

    def run(self, **kwargs):

        if ('kmeans' and 'escal' and 'pca' and 'atleta') in kwargs:
            kmeans = kwargs['kmeans']
            escal = kwargs['escal']
            pca = kwargs['pca']
            dadosAtleta = [
                kwargs['atleta']['flexibilidade'],
                kwargs['atleta']['abdominaisEmUmMin'],
                kwargs['atleta']['arremecoDeBolaMed'],
                kwargs['atleta']['distEmSaltoHorz']
                ]
            npAtletas = np.array(dadosAtleta)
            escalAtletas = escal.transform(npAtletas)
            escalAtletas[2] *= 1.6
            escalAtletas[3] *= 1.3
            cluster = kmeans.predict(escalAtletas)
            cluster = cluster[0]
            dadosPca = pca.transform(escalAtletas)
            nome = kwargs['atleta']['nome']
            x = dadosPca[0, 0]
            y = dadosPca[0, 1]
            kwargs['grafico'].scatter(
                x,
                y,
                c=[cluster],
                cmap='viridis'
            )
            kwargs['grafico'].annotate(
                nome,
                (x, y),
                textcoords="offset points",
                xytext=(0, 10),
                ha='center'
            )
            kwargs['grafImg'].draw()

        if self.next != None:
            return self.next.run(grafico=kwargs['grafico'])
        else:
            return self.last(grafico=kwargs['grafico'])

