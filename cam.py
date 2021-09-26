from types import LambdaType
from grafo_lab import *


class Cam:
    def __init__(self, lab: Labirinto, n) -> None:

        self.lab = lab
        self.n = n

        self.vizit = []

        for i in range(self.lab.i):
            linha_vizit = []
            for j in range(self.lab.j):
                linha_vizit.append(False)

            self.vizit.append(linha_vizit)

        
    def define_caminho(self):

        disponiveis = []
        for i in range(self.lab.i):
            for j in range(self.lab.j):
                disponiveis.append(self.lab.matriz[i][j])

        self.vizit[self.lab.fim.i][self.lab.fim.j] = True

        self.caminho(self.lab.inicio, 0, self.lab.i - 1, 0, self.lab.j - 1)

        for num in range(1, self.n):
            vert = random.choice(disponiveis)
            while self.vizit[vert.i][vert.j]:
                disponiveis.remove(vert)
                if disponiveis != []:
                    vert = random.choice(disponiveis)
                else:
                    return
            print(vert.i, vert.j)

            if vert.i == 0:
                i2 = vert.i
                if vert.j < self.lab.inicio.j:
                    j1 = vert.j + 1
                    j2 = self.lab.j - 1
                else:
                    j1 = 0
                    j2 = vert.j - 1
            else:
                i2 = vert.i - 1
                j1 = 0
                j2 = self.lab.j - 1

            
            self.caminho(vert, 0, i2, j1, j2)

            if vert.i == self.lab.i - 1:
                i1 = vert.i
                if vert.j < self.lab.fim.j:
                    j1 = vert.j + 1
                    j2 = self.lab.j - 1
                else:
                    j1 = 0
                    j2 = vert.j - 1
            else:
                i1 = vert.i + 1
                j1 = 0
                j2 = self.lab.j - 1

            self.caminho(vert, i1, self.lab.i - 1, j1, j2)

        for vrt in disponiveis:
            if not self.vizit[vrt.i][vrt.j]:
                self.caminho(vrt,0, self.lab.i - 1, 0, self.lab.j - 1)
 

    def caminho(self, origem: Vertice, i1, i2, j1, j2):

        acess = []
        for i in range(self.lab.i):
            linha_acess = []
            for j in range(self.lab.j):
                linha_acess.append(False)

            acess.append(linha_acess)

        self.vizit[origem.i][origem.j] = False
        
        pilha = [origem]

        while not self.vizit[pilha[-1].i][pilha[-1].j]:

            acess[pilha[-1].i][pilha[-1].j] = True

            opcoes = []

            i = pilha[-1].i
            j = pilha[-1].j

            if i > i1 and j1<=j<=j2:
                if not acess[i-1][j]:
                    opcoes.append(self.lab.matriz[i-1][j])

            if i < i2 and j1<=j<=j2:
                if not acess[i+1][j]:
                    opcoes.append(self.lab.matriz[i+1][j])

            if j > j1 and i1<=i<=i2:
                if not acess[i][j-1]:
                    opcoes.append(self.lab.matriz[i][j-1])

            if j < j2 and i1<=i<=i2:
                if not acess[i][j+1]:
                    opcoes.append(self.lab.matriz[i][j+1])

            if opcoes == []:
                pilha.pop()
            else:
                pilha.append(random.choice(opcoes))
 
        for n in range(len(pilha) - 1):
            pilha[n].add_vizinho(pilha[n+1])

        for v in pilha:
            self.vizit[v.i][v.j] = True
            #print(v.i, v.j)
