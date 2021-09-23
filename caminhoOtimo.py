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
