import os
import pygame
from Caminhos import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

window_width = 1280
window_height = 720

labi_width = window_width * 0.8
labi_height = labi_width * (9/16)


a = 30
l = 30


class Map:
    
    def __init__(self, height:int, width:int, n_paths:int):
        
        self.Labirin = Labirinto(height, width)
        self.Path = Cam(self.Labirin, 1)
        self.Path.define_caminho()
        self.height = height
        self.width = width
        
        self.graph_map = self.Labirin.matriz
        self.matrix_map = []
        self.Labirin.imprimir()

        
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
running = True





def drawStroke(actual_i, actual_j):
    
    borderPixels = int(((labi_width)/matrix_map.width) * 0.2)
    

    initialPosX = (labi_width * actual_j )/matrix_map.width + 0.10*window_width
    initialPosY = (labi_height * actual_i)/matrix_map.height + 0.10*window_height
    
    newPosX = initialPosX + (labi_width/matrix_map.width)
    newPosY = initialPosY + (labi_height/matrix_map.height)
    
    
    if not (matrix_map.graph_map[actual_i][actual_j].acima()):
        pygame.draw.line(window,(0,0,255),(initialPosX, initialPosY), (newPosX, initialPosY), borderPixels)
    
    
    if not (matrix_map.graph_map[actual_i][actual_j].abaixo()):
        pygame.draw.line(window,(0,0,255),(initialPosX, newPosY), (newPosX, newPosY), borderPixels)
        
        
    if not (matrix_map.graph_map[actual_i][actual_j].direita()):
        pygame.draw.line(window,(0,0,255),(newPosX, initialPosY), (newPosX, newPosY), borderPixels)
        
        
    if not (matrix_map.graph_map[actual_i][actual_j].esquerda()):
        pygame.draw.line(window,(0,0,255),(initialPosX, initialPosY), (initialPosX, newPosY), borderPixels)


def movePlayer(actual_i, actual_j, playerX, playerY, stepsCounter):
    
    
    if event.key == pygame.K_RIGHT and (matrix_map.graph_map[actual_i][actual_j].direita()):
        playerX += (labi_width/matrix_map.width)
        actual_j += 1
        stepsCounter += 1
    if event.key == pygame.K_LEFT and (matrix_map.graph_map[actual_i][actual_j].esquerda()):
        playerX -= (labi_width/matrix_map.width)
        actual_j -= 1
        stepsCounter += 1
    if event.key == pygame.K_DOWN and (matrix_map.graph_map[actual_i][actual_j].abaixo()):
        playerY += (labi_height/matrix_map.height)
        actual_i += 1
        stepsCounter += 1
    if event.key == pygame.K_UP and (matrix_map.graph_map[actual_i][actual_j].acima()):
        playerY -= (labi_height/matrix_map.height)
        actual_i -= 1
        stepsCounter += 1
    
    print(playerX, playerY)
    
    return actual_i, actual_j, playerX, playerY, stepsCounter


def drawCounter(value):
    text = font.render(str(value), True, (0,0,0), (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (window_width*0.95, window_height*0.1)
    window.blit(text, textRect)
    

actual_i= matrix_map.Labirin.inicio.i
actual_j  = matrix_map.Labirin.inicio.j
playerX = ((labi_width * actual_j)/matrix_map.width) + (window_width - labi_width) * 0.55
playerY = ((labi_height * actual_i) /matrix_map.height) + (window_height - labi_height) * 0.55
playerWidth = ((labi_width)/matrix_map.width) * 0.4
playerHeight = ((labi_height)/matrix_map.height) *0.4
stepsCounter = 0


font = pygame.font.Font('freesansbold.ttf', 32)

print(actual_i, actual_j)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            actual_i, actual_j, playerX, playerY, stepsCounter = movePlayer(actual_i, actual_j, playerX, playerY, stepsCounter)
            if event.key == pygame.K_ESCAPE:
                running = False
                break



    window.fill((255,255,255))
    
    pygame.draw.rect(window,(173,255,47), pygame.Rect((playerX, playerY), (playerWidth, playerHeight)))
    drawCounter(stepsCounter)
    

    for i in range(matrix_map.height):
        
        for j in range(matrix_map.width):
            if(matrix_map.matrix_map[i][j] == 0):
                drawStroke(i, j)
                
            
            
    
    pygame.display.update()    

    clock.tick(60)


pygame.quit()


