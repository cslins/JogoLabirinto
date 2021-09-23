from Graph_Lab import *
import random


class Caminhos:

    def __init__(self, lab: Labirinto, n: int = 1) -> None:
        self.lab = lab
        self.cam = []
        self.vizit = []

        for i in range(self.lab.i):
            linha_cam = []
            for j in range(self.lab.j):
                linha_cam.append([])

            self.cam.append(linha_cam)

        for w in range(1, n+1):
            self.caminho_ini(w)

        
    def caminho_ini(self, num):
        self.vizit = []
        for i in range(self.lab.i):
            linha_vizit = []
            for j in range(self.lab.j):
                linha_vizit.append(False)

            self.vizit.append(linha_vizit)
        

        pilha = [self.lab.inicio]

        while pilha[-1] != self.lab.fim:
            self.vizit[pilha[-1].i][pilha[-1].j] = True
            opc = self.vizinhos_validos(pilha[-1])

            if opc == []:
                pilha.pop()
            else:
                pilha.append(random.choice(opc))
        
        print()
        desvio = -1
        for n in range(len(pilha) - 1):
            i = pilha[n].i
            j = pilha[n].j

            if desvio == -1:
                if self.cam[i][j] == []:
                    desvio = n

            else:
                if self.cam[i][j] != []:
                    pilha = pilha[desvio-1:n+1]
                    break


        for n in range(len(pilha) - 1):
            pilha[n].add_vizinho(pilha[n+1])
            i = pilha[n].i
            j = pilha[n].j

            self.cam[i][j].append(num)

        self.cam[pilha[-1].i][pilha[-1].j].append(num)

        for it in pilha:
            print(it.i, it.j)



    def vizinhos_validos(self, v: Vertice) -> list:
        opcoes = []

        i = v.i
        j = v.j

        if i > 0:
            if not self.vizit[i-1][j]:
                opcoes.append(self.lab.matriz[i-1][j])

        if i < self.lab.i - 1:
            if not self.vizit[i+1][j]:
                opcoes.append(self.lab.matriz[i+1][j])

        if j > 0:
            if not self.vizit[i][j-1]:
                opcoes.append(self.lab.matriz[i][j-1])

        if j < self.lab.j - 1:
            if not self.vizit[i][j+1]:
                opcoes.append(self.lab.matriz[i][j+1])


        return opcoes

    def semsaida(self):
        for i in range(self.lab.i):
            for j in range(self.lab.j):
                if self.cam[i][j] != []:
                    self.acessar(self.lab.matriz[i][j])
    
    def acessar(self, v: Vertice):

        i = v.i
        j = v.j

        pilha = [v]

        while pilha != []:
            opcoes = []

            i = pilha[-1].i
            j = pilha[-1].j

            
            self.cam[i][j] = [0]

            if i > 0:
                if self.cam[i-1][j] == []:
                    opcoes.append(self.lab.matriz[i-1][j])

            if i < self.lab.i - 1:
                if self.cam[i+1][j] == []:
                    opcoes.append(self.lab.matriz[i+1][j])

            if j > 0:
                if self.cam[i][j-1] == []:
                    opcoes.append(self.lab.matriz[i][j-1])

            if j < self.lab.j - 1:
                if self.cam[i][j+1] == []:
                    opcoes.append(self.lab.matriz[i][j+1])

            if opcoes != []:
                escolha = random.choice(opcoes)

                pilha[-1].add_vizinho(escolha)

                pilha.append(escolha)
            else:
                pilha.pop()
                



