import os
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'

window_width = 1080
window_height = 720

class MatrixMap:
    
    def __init__(self, matrix_map):
        self.matrix = matrix_map
        self.width = len(matrix_map[0])
        self.height = len(matrix_map)


matrix_map = MatrixMap([[1, 1, 0, 1],
                        [0, 0, 0, 1],
                        [1, 0, 0, 1],
                        [1, 1, 0, 0]])


pygame.init()
window = pygame.display.set_mode((window_width,window_height))
# pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()

x = 120
y = 120
running = True



def drawStroke(actual_i, actual_j, initialPosX, initialPosY):
    
    borderPixels = 20
    
    newPosX = initialPosX + (window_width/matrix_map.width)
    newPosY = initialPosY + (window_height/matrix_map.height)
    
    

    if actual_j-1 >= 0 and matrix_map.matrix[actual_i][actual_j-1] == 0:
        pygame.draw.line(window,(0,0,255),(initialPosX, initialPosY), (initialPosX, newPosY), borderPixels)
        
    elif actual_j-1 < 0:
        pygame.draw.line(window,(0,0,255),(initialPosX, initialPosY), (initialPosX, newPosY), borderPixels)


    if actual_j+1 < matrix_map.width and matrix_map.matrix[actual_i][actual_j+1] == 0:
        pygame.draw.line(window,(0,0,255),(newPosX, initialPosY), (newPosX, newPosY), borderPixels)
        
    elif actual_j+1 == matrix_map.width:
        pygame.draw.line(window,(0,0,255),(newPosX, initialPosY), (newPosX, newPosY), borderPixels)
        

    if actual_i - 1 >= 0 and matrix_map.matrix[actual_i-1][actual_j] == 0:
        pygame.draw.line(window,(0,0,255),(initialPosX, initialPosY), (newPosX, initialPosY), borderPixels)
        
    elif actual_i-1 < 0:
        pygame.draw.line(window,(0,0,255),(initialPosX, initialPosY), (newPosX, initialPosY), borderPixels)
        

    if actual_i+1 < matrix_map.width and matrix_map.matrix[actual_i+1][actual_j] == 0:
        pygame.draw.line(window,(0,0,255),(initialPosX, newPosY), (newPosX, newPosY), borderPixels)
        
    elif actual_i+1 == matrix_map.height:
        pygame.draw.line(window,(0,0,255),(initialPosX, newPosY), (newPosX, newPosY), borderPixels)
        
        

            

            




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
    

    for i in range (len(matrix_map.matrix)):
        position_y = (window_height * i)/matrix_map.height
        for j in range (len(matrix_map.matrix[i])):
            position_x = (window_width * j)/matrix_map.width
            if(matrix_map.matrix[i][j] == 1):
                drawStroke(i, j, position_x, position_y)
            
            
    
    pygame.display.update()    

    clock.tick(60)

pygame.quit()