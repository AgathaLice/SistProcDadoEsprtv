
from Model.Chain import Link
from sklearn.decomposition import PCA

class EloDecomposicao(Link):

    def run(self, **kwargs):

        if ('dadosAtletas' and
            'kmeansSalvo' and
            'escalonador') in kwargs:
            dadosParaDec = []
            for dado in kwargs['dadosAtletas']:
                for atleta in dado['dadosLista']:
                    dadosParaDec.append(atleta)
            pca = PCA(n_components=2) # número de eixos (x e y) do gráfico
            dadosDecompostos = pca.fit_transform(dadosParaDec).tolist()
            ids = []
            for dado in kwargs['dadosAtletas']:
                for idNome in dado['idsLista']:
                    ids.append(idNome)
            clusters = []
            for dado in kwargs['dadosAtletas']:
                for cluster in dado['clusters']:
                    clusters.append(cluster)
        else:
            print('ERRO NA DECOMPOSIÇÃO DOS DADOS PARA GRÁFICO')

        if self.next != None:
            return self.next.run(dadosDecompostos=dadosDecompostos,
                                 ids=ids,
                                 clusters=clusters,
                                 pca=pca,
                                 kmeansSalvo=kwargs['kmeansSalvo'],
                                 escalonador=kwargs['escalonador'])
        else:
            return self.last(dadosDecompostos=dadosDecompostos,
                             ids=ids,
                             clusters=clusters,
                             pca=pca,
                             kmeansSalvo=kwargs['kmeansSalvo'],
                             escalonador=kwargs['escalonador'])
