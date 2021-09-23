from menorcaminho import BFS
from caminhos import *
from caminhoOtimo import *
import imprimir
import pygame


a = 30
l = 40
la = Labirinto(a, l)

c = Caminhos(la, 5)
c.semsaida()

la.imprimir()
print()

ext = imprimir.Base(lab)
ext.print()
print()

otimo = BellmanFord(lab, 10)

otimocaminho = otimo.search()
ext.caminho_vertice(otimocaminho['caminho'])
print(otimocaminho['valor'])
print()
