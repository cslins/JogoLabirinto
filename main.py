from grafo_lab import *
import random


i = 4 # tamanho do labirinto
j = 4

lab = Labirinto(i, j)


listacam = []

for ob in range(2):
    cam = Caminho(lab)
    if ob == 0:
        listacam.append(cam.construir_caminho())
    else:
         listacam.append(cam.construir_caminho(False))


for itn in listacam:
    print()
    for v in itn:
        print(v.i, v.j, end='  ')

    print()

lab.imprimir()
#lab.imprimir_lab()
print()

busca = BFS(lab)

mc = busca.largura()

for v in mc:
    print(v.i, v.j, end='  ')


