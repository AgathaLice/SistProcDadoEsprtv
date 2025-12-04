
from Model.Chain import Link
import matplotlib.pyplot as plt

class EloGrafico(Link):

    def run(self, **kwargs):

        if ('dadosDecompostos' and
            'ids' and
            'clusters') in kwargs:

            img, grafico = plt.subplots(figsize=(10, 8))
            grafico.scatter(
            [linha[0] for linha in kwargs['dadosDecompostos']],
            [linha[1] for linha in kwargs['dadosDecompostos']],
            c=kwargs['clusters'],
            cmap='viridis',
            label='Dados dos Atletas')

            for i, (x, y) in enumerate(kwargs['dadosDecompostos']): # enumerate pq ele precisa ter um index além dos dados
                grafico.annotate(
                    kwargs['ids'][i], # oq escrever
                    (x, y), # coordenadas
                    textcoords="offset points", # um pouco acima
                    xytext=(0, 10), # qtd de pixels de offset (nesse caso é acima por 10)
                    ha='center' # escrita no centro
                )
            
            grafico.set_title('Classificação dos Atletas')
            grafico.set_xlabel('Principal Component 1')
            grafico.set_ylabel('Principal Component 2')
            grafico.grid(True)

        else:
            print('ERRO NA GRAFICAÇÃO')

        if self.next != None:
            return self.next.run(img=img,
                                 pca=kwargs['pca'],
                                 kmeans=kwargs['kmeansSalvo'],
                                 escalonador=kwargs['escalonador'],
                                 grafico=grafico)
        else:
            return self.last(img=img,
                             pca=kwargs['pca'],
                             kmeans=kwargs['kmeansSalvo'],
                             escalonador=kwargs['escalonador'],
                             grafico=grafico)
