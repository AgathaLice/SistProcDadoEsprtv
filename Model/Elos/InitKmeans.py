
from Model.Chain import Link
from sklearn.cluster import KMeans

class EloInitKmeans(Link):

    def run(self, **kwargs):

        if ('idAtletas' and
            'npAtletas' and
            'escalAtletas' and
            'escalonador' and
            'tabelaGrafico' and
            'tabelaBson') in kwargs:
            kmeans = KMeans(n_clusters=2, random_state=42, n_init='auto')
            kmeansSalvo = kmeans.fit(kwargs['escalAtletas'])
            grupos = kmeans.labels_
        else:
            print('ERRO NA INICIALIZAÇÃO DO KMEANS')

        if self.next != None:
            return self.next.run(idAtletas=kwargs['idAtletas'],
                                 npAtletas=kwargs['npAtletas'],
                                 escalonador=kwargs['escalonador'],
                                 tabelaGrafico=kwargs['tabelaGrafico'],
                                 tabelaBson=kwargs['tabelaBson'],
                                 escalAtletas=kwargs['escalAtletas'],
                                 grupos=grupos,
                                 kmeansSalvo=kmeansSalvo)
        else:
            return self.last(idAtletas=kwargs['idAtletas'],
                             npAtletas=kwargs['npAtletas'],
                             escalonador=kwargs['escalonador'],
                             tabelaGrafico=kwargs['tabelaGrafico'],
                             tabelaBson=kwargs['tabelaBson'],
                             escalAtletas=kwargs['escalAtletas'],
                             grupos=grupos,
                             kmeansSalvo=kmeansSalvo)
