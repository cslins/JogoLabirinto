from menorcaminho import BFS
from caminhos import *
from caminhoOtimo import *
import imprimir
import pygame


a = 3
l = 3
la = Labirinto(a, l)

c = Cam(la, 1)
c.define_caminho()

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
