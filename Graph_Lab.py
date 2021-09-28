import random
import sys

class Vertice:

    def __init__(self, i, j, ID):
        self.i = i
        self.j = j
        self.id = ID
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
        
        ID = ""

        for i in range(self.i):
            linha = []
            ID = str(i)
            for j in range(self.j):
                
                ID += " "+str(j)
                vert = Vertice(i, j, ID)
                linha.append(vert)

                ID = str(i)

            self.matriz.append(linha)


    def imprimir(self):
        print(' ', end='')
        for j in range(self.j):
            if self.matriz[0][j] == self.inicio:
                print('  ', end='')
            else:
                print('_ ', end='')

        for i in range(self.i):
            print()
            for j in range(self.j):
                if j == 0:
                    print('|', end='')

                if i < self.i - 1:
                    if self.matriz[i + 1][j] in self.matriz[i][j].list_adj:
                        print(' ', end='')
                    else:
                        print('_', end='')
                else:
                    if self.matriz[i][j] == self.fim:
                        print(' ', end='')
                    else:
                        print('_', end='')

                if j < self.j - 1:
                    if self.matriz[i][j + 1] in self.matriz[i][j].list_adj:
                        print(' ', end='')
                    else:
                        print('|', end='')
                else:
                    print('|', end='')

        print()

    def imprimir_lab(self):

        for i in range(self.i):
            print()
            for j in range(self.j):

                aux = []
                for n in self.matriz[i][j].list_adj:
                    aux.append(n.id)

                print(f'{str(self.matriz[i][j].id): <6}:{str(aux)}')


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
            

        