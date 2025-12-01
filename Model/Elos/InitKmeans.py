
from Model.Chain import Link
from sklearn.cluster import KMeans

'''
    recebe todos os dados do elo npArrayAtletas,
    inicializa o KMeans,
    treina pela primeira vez com os dados recebidos no data,
    passa os dados treinados para o salvarTrain
'''

class EloInitKmeans(Link):

    def run(self, idsAtleta, npAtletas, escalAtletas):

        kmeans = KMeans(n_clusters=0, random_state=0, n_init='auto')
        kmeans.fit(escalAtletas)
        


        return self.next.run()