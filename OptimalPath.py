from Graph_Lab import *
import sys

class BellmanFord:

    def __init__(self, lab, cost: int):
        self.lab = lab  # para acessar o labrito
        self.M = lab.i * lab.j * 2  # numero de interaçoes do algoritimo
        self.caminho = [[[] for _ in range(lab.j)] for _ in range(lab.i)]  # matriz que guarda o melhor caminho para cada vertice 
        self.cost = cost  # valor da maça
        self.resposta = {'valor': None, 'caminho': []}  

        self.search()

        
    def search(self):

        distance = [[sys.maxsize for _ in range(self.lab.j)] for _ in range(self.lab.i)]

        distance[self.lab.inicio.i][self.lab.inicio.j] = 0

        for _ in range(self.M):
             
            # percorre a matriz
            for i in range(self.lab.i):
                for j in range(self.lab.j):

                    if distance[i][j] != sys.maxsize:
                      
                        for vertice in self.lab.matriz[i][j].list_adj:
                          
                            # define o custo 
                            if vertice.apple and vertice not in self.caminho[vertice.i][vertice.j]:
                                custo = -self.cost
                            else:
                                custo = 1

                            # para cada vertice atualiza o custo e caminho, se for melhor
                            if distance[i][j] + custo < distance[vertice.i][vertice.j] and vertice != self.lab.inicio:

                                distance[vertice.i][vertice.j] = distance[i][j] + custo

                                self.caminho[vertice.i][vertice.j] = self.caminho[i][j] + [self.lab.matriz[i][j]]
                                
                                # salva o caminho se for o final
                                if vertice == self.lab.fim:
                                    self.resposta['valor'] = distance[vertice.i][vertice.j]
                                    self.resposta['caminho'] = self.caminho[vertice.i][vertice.j] + [vertice]

        return self.resposta
    
    



BRANCO = 0
CINZA = 1
PRETO = 2

class BFS:

    def __init__(self, lab: Labirinto):
        self.lab = lab
        self.cor = []
        self.anterior = []
        self.d = []
        self.tempo = 0
        self.ordem_visita = []

        for i in range(self.lab.i):
            linha_cor = []
            linha_ante = []
            linha_dist = []
            for j in range(self.lab.j):
                linha_cor.append(BRANCO)
                linha_ante.append(None)
                linha_dist.append(sys.maxsize)

            self.cor.append(linha_cor)
            self.anterior.append(linha_ante)
            self.d.append(linha_dist)


    def largura(self):

        for i in range(self.lab.i):
            for j in range(self.lab.j):
                self.cor[i][j] = BRANCO
                self.d[i][j] = sys.maxsize
                self.anterior[i][j] = None

        ini = self.lab.inicio

        self.cor[ini.i][ini.j] = CINZA
        self.d[ini.i][ini.j] = 0
        self.anterior[ini.i][ini.j] = None

        fila = [ini]

        while fila != []:
            u = fila.pop(0)
            self.ordem_visita.append(u)
            if u == self.lab.fim:
                return self.menor_caminho(u)
            for v in u.list_adj:
                if self.cor[v.i][v.j] == BRANCO:
                    self.cor[v.i][v.j] = CINZA
                    self.d[v.i][v.j] = self.d[u.i][u.j] + 1
                    self.anterior[v.i][v.j] = u
                    fila.append(v)

            self.cor[u.i][u.j] = PRETO

    def menor_caminho(self, v: Vertice):
        caminho = []
        caminho.append(v)
        anterior = self.anterior[v.i][v.j]

        while anterior is not None:
            caminho.insert(0, anterior)
            anterior = self.anterior[anterior.i][anterior.j]
        
        return caminho