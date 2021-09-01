import random
import sys

BRANCO = 0
CINZA = 1
PRETO = 2

class Vertice:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.list_adj = []
        
        apple = False

    def add_vizinho(self, v):
        if v not in self.list_adj:
            self.list_adj.append(v)



class Labirinto:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.matriz = []
        self.inicio = [0, 0]
        self.fim = [self.i - 1, self.j - 1]

        self.construir_lab()
        self.inicio_fim()



    def construir_lab(self):

        for i in range(self.i):
            linha = []
            for j in range(self.j):
                vert = Vertice(i, j)
                linha.append(vert)

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



class Caminho:

    def __init__(self, lab: Labirinto):

        self.lab = lab
        self.vizitados = []
        self.pilha = []
        self.cont = 0
        self.lista_caminhos = []
        self.anterior = []

    def inicializar(self):
        for i in range(self.lab.i):
            linha_vizit = []
            linha_ante = []
            for j in range(self.lab.j):
                linha_vizit.append(False)
                linha_ante.append(None)

            self.vizitados.append(linha_vizit)
            self.anterior.append(linha_ante)
        self.pilha = []


    def construir_caminho(self, t=True):

        self.inicializar()

        self.pilha = [self.lab.inicio]
        tam = self.lab.i * self.lab.j

        while self.pilha != []:

            local_atual = self.pilha[-1]

            i = local_atual.i
            j = local_atual.j

            self.vizitados[i][j] = True

            opcoes = []

            if i > 0:
                if not self.vizitados[i-1][j]:
                    opcoes.append(self.lab.matriz[i-1][j])

            if i < self.lab.i - 1:
                if not self.vizitados[i+1][j]:
                    opcoes.append(self.lab.matriz[i+1][j])

            if j > 0:
                if not self.vizitados[i][j-1]:
                    opcoes.append(self.lab.matriz[i][j-1])

            if j < self.lab.j - 1:
                if not self.vizitados[i][j+1]:
                    opcoes.append(self.lab.matriz[i][j+1])

            if opcoes == []:
                self.pilha.pop()
            else:
                self.pilha.append(random.choice(opcoes))
                prox = self.pilha[-1]
                if t:
                    self.conectar(prox, local_atual)
                self.anterior[prox.i][prox.j] = local_atual

        caminho = []
        caminho.append(self.lab.fim)
        anterior = self.anterior[self.lab.fim.i][self.lab.fim.j]

        while anterior is not None:
            if not t:
                self.conectar(anterior, caminho[0])
            caminho.insert(0, anterior)
            anterior = self.anterior[anterior.i][anterior.j]
        
        return caminho


    def conectar(self, v1:Vertice, v2:Vertice):

        self.cont += 1

        if v2 not in v1.list_adj:
            v1.add_vizinho(v2)

        if v1 not in v2.list_adj:
            v2.add_vizinho(v1)


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

    