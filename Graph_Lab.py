import random
import sys

class Vertice:

    def __init__(self, i, j):
        self.i = i
        self.j = j

        self.list_adj = []
        
        self.inicio = False
        self.fim = False

        self.apple = False

    def add_vizinho(self, v):
        if v not in self.list_adj:
            self.list_adj.append(v)
        if self not in v.list_adj:
            v.list_adj.append(self)

    def acima(self) -> bool:
        for v in self.list_adj:
            if v.i == self.i - 1 and v.j == self.j or self.inicio == True:
                return True
        
        return False


    def abaixo(self) -> bool:
        for v in self.list_adj:
            if v.i == self.i + 1 and v.j == self.j or self.fim == True:
                return True
        
        return False

    def esquerda(self) -> bool:
        for v in self.list_adj:
            if v.i == self.i and v.j == self.j - 1:
                return True
        
        return False

    def direita(self) -> bool:
        for v in self.list_adj:
            if v.i == self.i and v.j == self.j + 1:
                return True
        
        return False
    
    def set_apple(self):
        self.apple = True


class Labirinto:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.matriz = []
        self.inicio = [0, 0]
        self.fim = [self.i - 1, self.j - 1]

        self.construir_lab()
        self.inicio_fim()
        
        self.listmacas = []



    def construir_lab(self):
        
        for i in range(self.i):
            linha = []
            for j in range(self.j):
                
                vert = Vertice(i, j)
                linha.append(vert)

            self.matriz.append(linha)



    def inicio_fim(self):
        self.inicio = self.matriz[0][random.randint(0, self.j - 1)]
        self.fim = self.matriz[self.i - 1][random.randint(0, self.j - 1)]
        
        for i in self.matriz:
            for j in i:
                if(self.inicio == j):
                    j.inicio = True
                if(self.fim == j):
                    j.fim = True
                    

    def colocar_macas(self, n: int):
        aux = []
        while True:
            posi = (random.randrange(self.i), random.randrange(self.j))
            if posi not in aux:
                aux.append(posi)
            if len(aux) == n:
                break
    
        self.listmacas.append(aux)
        for i, j in aux:
            self.matriz[i][j].set_apple()
            

        