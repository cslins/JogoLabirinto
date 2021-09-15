from grafo_lab import *
import sys

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

    