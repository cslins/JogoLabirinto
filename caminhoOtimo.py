from grafo_lab import *
import sys
import imprimir
from collections import deque


class BellmanFord:

    def __init__(self, lab: Labirinto, cost: int):
        self.lab = lab  # para acessar o labrito
        self.M = lab.i * lab.j  # numero de interaçoes do algoritimo
        self.caminho = [[[] for _ in range(lab.j)] for _ in
                        range(lab.i)]  # matriz que guarda o melhor caminho para cada vertice
        self.cost = cost  # valor da maça
        self.resposta = {'valor': sys.maxsize, 'caminho': []}

        #self.search()

    def search(self):
        e = imprimir.Base(self.lab)

        distance = [[sys.maxsize for _ in range(self.lab.j)] for _ in range(self.lab.i)]

        distance[self.lab.inicio.i][self.lab.inicio.j] = 0
        if self.lab.inicio.apple:
            distance[self.lab.inicio.i][self.lab.inicio.j] -= self.cost
        self.caminho[self.lab.inicio.i][self.lab.inicio.j] += [self.lab.inicio]

        for _ in range(self.M):

            # percorre a matriz
            for i in range(self.lab.i):
                for j in range(self.lab.j):

                    # print('(', i, ',', j, ') - ', distance[i][j], ':')  ############

                    if distance[i][j] != sys.maxsize:

                        for vertice in self.lab.matriz[i][j].list_adj:

                            # define o custo 
                            if vertice.apple and not (vertice in self.caminho[vertice.i][vertice.j]):
                                custo = 0 - self.cost
                            else:
                                custo = 1

                            # para cada vertice atualiza o custo e caminho, se for melhor
                            if distance[i][j] + custo < distance[vertice.i][
                                vertice.j]:  # and vertice != self.lab.inicio:

                                # e.caminho_vertice(self.caminho[vertice.i][vertice.j])
                                # print('  [', vertice.i, ',', vertice.j, ']',
                                #      distance[i][j] + custo, distance[vertice.i][vertice.j])

                                distance[vertice.i][vertice.j] = distance[i][j] + custo

                                self.caminho[vertice.i][vertice.j] = self.caminho[i][j] + [vertice]

                                # salva o caminho se for o final
                                if vertice == self.lab.fim and distance[vertice.i][vertice.j] < self.resposta['valor']:
                                    self.resposta['valor'] = distance[vertice.i][vertice.j]+1
                                    self.resposta['caminho'] = self.caminho[vertice.i][vertice.j]

                                # print()
                                # e.caminho_vertice(self.caminho[vertice.i][vertice.j])
                                # print('  -', vertice.i, ',', vertice.j, '-: ', distance[vertice.i][vertice.j])
                                # for a in self.caminho[vertice.i][vertice.j]:
                                #    print(a.i, a.j, end='  ')
                                # print('\n')

        return self.resposta


class BFS_mod:

    def __init__(self, lab: Labirinto, cost: int):
        self.lab = lab  # para acessar o labrito
        self.caminho = [[[] for _ in range(lab.j)] for _ in
                        range(lab.i)]  # matriz que guarda o melhor caminho para cada vertice
        self.distance = [[sys.maxsize for _ in range(self.lab.j)] for _ in range(self.lab.i)]
        self.cost = cost  # valor da maça
        self.resposta = {'valor': sys.maxsize, 'caminho': []}

        #self.search()

    def search(self):

        e = imprimir.Base(self.lab)

        fila = deque()
        self.distance[self.lab.inicio.i][self.lab.inicio.j] = 0
        self.caminho[self.lab.inicio.i][self.lab.inicio.j] += [self.lab.inicio]

        fila.append(self.lab.inicio)
        while fila:
            vertice = fila.popleft()
            for vertice_adj in vertice.list_adj:

                # define o custo
                if vertice_adj.apple and vertice_adj not in self.caminho[vertice.i][vertice.j]:
                    custo = -self.cost
                else:
                    custo = 1

                # para cada vertice atualiza o custo e caminho, se for melhor
                if self.distance[vertice.i][vertice.j] + custo <=\
                        self.distance[vertice_adj.i][vertice_adj.j]:  # and vertice != self.lab.inicio:

                    self.distance[vertice_adj.i][vertice_adj.j] = self.distance[vertice.i][vertice.j] + custo
                    self.caminho[vertice_adj.i][vertice_adj.j] = self.caminho[vertice.i][vertice.j] + \
                                                                 [vertice_adj]

                    # salva o caminho se for o final
                    if vertice_adj == self.lab.fim and \
                            self.distance[vertice_adj.i][vertice_adj.j] < self.resposta['valor']:
                        self.resposta['valor'] = self.distance[vertice.i][vertice.j]
                        self.resposta['caminho'] = self.caminho[vertice.i][vertice.j] + [vertice_adj]

                    fila.append(vertice_adj)

                    #print()
                    #e.caminho_vertice(self.caminho[vertice_adj.i][vertice_adj.j])
                    #print('  -', vertice_adj.i, ',', vertice_adj.j, '-: ', self.distance[vertice_adj.i][vertice_adj.j])
                    #for a in self.caminho[vertice_adj.i][vertice_adj.j]:
                    #    print(a.i, a.j, end='  ')
                    #print('\n')

        return self.resposta
