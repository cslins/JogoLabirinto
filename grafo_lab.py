import random
import math



class Vertice:

    def __init__(self, id, list_adj: list):
        self.id = id
        self.list_adj = list_adj



class Labirinto:

    def __init__(self, tam):
        self.tam = tam
        self.matriz = []
        self.inicio = [0, 0]
        self.fim = [self.tam - 1, self.tam - 1]

        self.construir_lab()
        self.inicio_fim()



    def construir_lab(self):

        for i in range(self.tam):
            linha = []
            for j in range(self.tam):
                id = str(i) + ' ' + str(j)
                vert = Vertice(id, [])
                linha.append(vert)

            self.matriz.append(linha)



    def imprimir(self):


        inicial = self.matriz[self.inicio[0]][self.inicio[1]]
        final = self.matriz[self.fim[0]][self.fim[1]]

        print(' ', end='')
        for j in range(self.tam):
            if self.matriz[0][j] == inicial:
                print('  ', end='')
            else:
                print('_ ', end='')

        for i in range(self.tam):
            print()
            for j in range(self.tam):
                if j == 0:
                    print('|', end='')

                if i < self.tam - 1:
                    if self.matriz[i + 1][j] in self.matriz[i][j].list_adj:
                        print(' ', end='')
                    else:
                        print('_', end='')
                else:
                    if self.matriz[i][j] == final:
                        print(' ', end='')
                    else:
                        print('_', end='')

                if j < self.tam - 1:
                    if self.matriz[i][j + 1] in self.matriz[i][j].list_adj:
                        print(' ', end='')
                    else:
                        print('|', end='')
                else:
                    print('|', end='')

        print()

    def imprimir_lab(self):

        for i in range(self.tam):
            print()
            for j in range(self.tam):

                aux = []
                for n in self.matriz[i][j].list_adj:
                    aux.append(n.id)

                print(f'{str(self.matriz[i][j].id): <6}:{str(aux)}')


    def inicio_fim(self):
        self.inicio = [0, random.randint(0, self.tam - 1)]
        self.fim = [self.tam - 1, random.randint(0, self.tam - 1)]



class Caminho:

    def __init__(self, lab: Labirinto):

        self.lab = lab
        self.vizitados = []
        self.beira = []
        self.cont = 0

    def construir_caminho(self):

        self.cont = 0

        self.beira = [self.lab.inicio]
        tam = self.lab.tam

        local_atual = random.choice(self.beira)
        self.vizitados.append(local_atual)

        while len(self.vizitados) < tam ** 2:

            self.beira.remove(local_atual)

            i = local_atual[0]
            j = local_atual[1]

            if i > 0:
                self.add_beira(i - 1, j)

            if i < tam - 1:
                self.add_beira(i + 1, j)

            if j > 0:
                self.add_beira(i, j - 1)

            if j < tam - 1:
                self.add_beira(i, j + 1)

            local_prox = random.choice(self.beira)

            self.vizitados.append(local_atual)

            for local in reversed(self.vizitados):
                boolean = self.conectar(local[0], local[1], local_prox[0], local_prox[1])
                if boolean:
                    break


            local_atual = local_prox.copy()



        #print(self.vizitados)


    def add_beira(self, i, j):

        if [i, j] not in self.beira and [i, j] not in self.vizitados:
            self.beira.append([i, j])



    def conectar(self, i1, j1, i2, j2):

        if abs(i1 - i2) > 1 or abs(j1 - j2) > 1:
            return False
        if i1 != i2 and j1 != j2:
            return False

        self.cont += 1

        v1 = self.lab.matriz[i1][j1]
        v2 = self.lab.matriz[i2][j2]

        if v2 not in v1.list_adj:
            v1.list_adj.append(v2)

        if v1 not in v2.list_adj:
            v2.list_adj.append(v1)

        return True





t = 10 # tamanho do labirinto


lab = Labirinto(t)
cam = Caminho(lab)
print('local do inicio:', lab.inicio)
print('local do fim:', lab.fim)

cam.construir_caminho()

lab.imprimir()
#lab.imprimir_lab()
print()

quant_paredes_inicio = 2*t*(t-1)
quant_paredes_final = quant_paredes_inicio - cam.cont

print('Quantidade de paredes no labirinto =', quant_paredes_final)

