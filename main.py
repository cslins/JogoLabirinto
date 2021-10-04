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

alt_otimo = BFS_mod(lab, 10)
otimo_caminho = alt_otimo.search()
ext.caminho_vertice(otimo_caminho['caminho'])
print(otimo_caminho['valor'])
#for i in otimo_caminho['caminho']:
#    print(i.i, i.j)
print()
