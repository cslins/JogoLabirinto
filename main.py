from menorcaminho import BFS

from cam import *
import pygame


a = 3
l = 3
la = Labirinto(a, l)

c = Cam(la, 1)
c.define_caminho()

la.imprimir()
print()

'''
busca = BFS(la)

mc = busca.largura()

for v in mc:
    print(v.i, v.j)

'''