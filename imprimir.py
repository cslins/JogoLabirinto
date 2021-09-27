from grafo_lab import *
import copy

preto = '\033[40m'
vermelho = '\033[41m'
verde = '\033[42m'
amarelo = '\033[43m'
azul = '\033[44m'
magenta = '\033[45m'
ciano = '\033[46m'
branco = '\033[47m'
original = '\033[0;0m'


class Base:
    def __init__(self, lab: Labirinto):
        self.lab = lab
        self.atl = lab.i
        self.lar = lab.j
        self.inicio = lab.inicio
        self.fim = lab.fim
        self.matriz = []
        self.const_matriz()

    def const_matriz(self):
        for _ in range(self.atl*2+1):
            linha = []
            for _ in range(self.lar*2+1):
                linha.append(preto)
            self.matriz.append(linha)

        self.matriz[0][self.inicio.j * 2 + 1] = ciano
        self.matriz[-1][self.fim.j * 2 + 1] = verde

        for x in range(self.atl):
            for y in range(self.lar):
                self.matriz[x*2+1][y*2+1] = branco

                if x < self.atl - 1:
                    if self.lab.matriz[x+1][y] in self.lab.matriz[x][y].list_adj:
                        self.matriz[x * 2 + 2][y * 2 + 1] = branco

                if y < self.lar - 1:
                    if self.lab.matriz[x][y+1] in self.lab.matriz[x][y].list_adj:
                        self.matriz[x * 2 + 1][y * 2 + 2] = branco

                if self.lab.matriz[x][y].apple:
                    self.matriz[x * 2 + 1][y * 2 + 1] = vermelho

    def print(self):
        for lin in self.matriz:
            for tex in lin:
                print(tex, ' ', original, end='')
            print()

    def caminho(self, lista):
        # print(lista)
        newMatriz = copy.deepcopy(self.matriz)
        old = (self.inicio.i, self.inicio.j)
        for x, y in lista:
            newMatriz[x*2+1][y*2+1] = amarelo

            if old[0] > x:
                newMatriz[old[0] * 2][old[1] * 2 + 1] = amarelo
            elif old[0] < x:
                newMatriz[old[0] * 2 + 2][old[1] * 2 + 1] = amarelo

            if old[1] > y:
                newMatriz[old[0] * 2 + 1][old[1] * 2] = amarelo
            elif old[1] < y:
                newMatriz[old[0] * 2 + 1][old[1] * 2 + 2] = amarelo

            old = (x, y)

            if self.lab.matriz[x][y].apple:
                newMatriz[x * 2 + 1][y * 2 + 1] = magenta

        for lin in newMatriz:
            for tex in lin:
                print(tex, ' ', original, end='')
            print()

    def caminho_vertice(self, lista):
        # print(lista)
        newMatriz = copy.deepcopy(self.matriz)

        old = (self.inicio.i, self.inicio.j)
        for vetice in lista:
            x = vetice.i
            y = vetice.j

            newMatriz[x*2+1][y*2+1] = amarelo

            if old[0] > x:
                newMatriz[old[0] * 2][old[1] * 2 + 1] = amarelo
            elif old[0] < x:
                newMatriz[old[0] * 2 + 2][old[1] * 2 + 1] = amarelo

            if old[1] > y:
                newMatriz[old[0] * 2 + 1][old[1] * 2] = amarelo
            elif old[1] < y:
                newMatriz[old[0] * 2 + 1][old[1] * 2 + 2] = amarelo

            old = (x, y)

            if self.lab.matriz[x][y].apple:
                newMatriz[x * 2 + 1][y * 2 + 1] = magenta

        for lin in newMatriz:
            for tex in lin:
                print(tex, ' ', original, end='')
            print()

