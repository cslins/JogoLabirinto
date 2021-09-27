from menorcaminho import BFS
from cam import *
from caminhoOtimo import *
import imprimir
import pygame


a = 3
l = 3
lab = Labirinto(a, l)

c = Cam(lab, 1)
c.define_caminho()

lab.colocar_macas(4)

lab.imprimir()
print()


ext = imprimir.Base(lab)
ext.print()
print()

otimo = BellmanFord(lab, 10)

otimocaminho = otimo.search()
ext.caminho_vertice(otimocaminho['caminho'])
print(otimocaminho['valor'])
print()
