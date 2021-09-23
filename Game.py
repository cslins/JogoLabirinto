import os
import pygame
from Caminhos import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

window_width = 1080
window_height = 720


a = 3
l = 3


class Map:
    
    def __init__(self, height:int, width:int, n_paths:int):
        
        self.labirin = Labirinto(height, width)
        self.Path = Caminhos(self.labirin, 1)
        self.height = height
        self.width = width
        
        self.graph_map = self.labirin.matriz
        self.matrix_map = []
        self.labirin.imprimir()

        
        for i in range(height):
            self.matrix_map.append([])
            for j in range(width):
                self.matrix_map[i].append(0)
        
        
    
    def print_matrix_map(self) -> None:
        for i in range(self.height):
            print(self.matrix_map[i])
            
    
    def print_graph_map(self) -> None:
        for i in range(self.height):
            print()
            for j in range(self.width):
                print(self.graph_map[i][j].id, end='   ')


matrix_map = Map(a, l, 1)


pygame.init()
window = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()

x = 120
y = 120
running = True



def drawStroke(actual_i, actual_j):
    
    borderPixels = 20
    
    initialPosX = (window_width * actual_j)/matrix_map.width
    initialPosY = (window_height * actual_i)/matrix_map.height
    
    newPosX = initialPosX + (window_width/matrix_map.width)
    newPosY = initialPosY + (window_height/matrix_map.height)
    
    
    if not (matrix_map.graph_map[i][j].acima()):
        pygame.draw.line(window,(0,0,255),(initialPosX, initialPosY), (newPosX, initialPosY), borderPixels)
    
    
    if not (matrix_map.graph_map[i][j].abaixo()):
        pygame.draw.line(window,(0,0,255),(initialPosX, newPosY), (newPosX, newPosY), borderPixels)
        
        
    if not (matrix_map.graph_map[i][j].direita()):
        pygame.draw.line(window,(0,0,255),(newPosX, initialPosY), (newPosX, newPosY), borderPixels)
        
        
    if not (matrix_map.graph_map[i][j].esquerda()):
        pygame.draw.line(window,(0,0,255),(initialPosX, initialPosY), (initialPosX, newPosY), borderPixels)
        
        


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            elif event.key == pygame.K_RIGHT:
                x += 8
            elif event.key == pygame.K_LEFT:
                x -= 8
            elif event.key == pygame.K_DOWN:
                y += 8
            elif event.key == pygame.K_UP:
                y -= 8


    window.fill((255,255,255))
    

    for i in range(matrix_map.height):
        
        for j in range(matrix_map.width):
            if(matrix_map.matrix_map[i][j] == 0):
                drawStroke(i, j)
                
            
            
    
    pygame.display.update()    

    clock.tick(60)

pygame.quit()