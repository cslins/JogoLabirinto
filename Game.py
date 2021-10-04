import os
import pygame
from Caminhos import *
from OptimalPath import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

window_width = 1280
window_height = 720

labi_width = window_width * 0.8
labi_height = labi_width * (9/16)


a = 15
l = 15

class Map:
    
    def __init__(self, height:int, width:int, n_paths:int, n_apples:int, apples_score:int):
        
        self.Labirin = Labirinto(height, width)
        self.Path = Cam(self.Labirin, n_paths)
        self.Path.define_caminho()
        self.appleScore = apples_score
        self.Otimo = BFS(self.Labirin)
        self.otimoCaminhoSemMaca = self.Otimo.largura()
        self.OtimoMaca = BFS_mod(self.Labirin, self.appleScore)
        self.otimoCaminhoMaca = self.OtimoMaca.search()
        self.height = height
        self.width = width
        
        
        self.graph_map = self.Labirin.matriz
        self.matrix_map = []
        self.Labirin.colocar_macas(n_apples)
        
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
                

    def drawMap(self):
        
        for i in range(self.height):
        
            for j in range(self.width):
                
                if(self.graph_map[i][j].apple):
                    self.__drawApple(i, j)
            
                if(self.matrix_map[i][j] == 0):
                    
                    borderPixelsX = int(((labi_width)/self.width) * 0.1)
                    borderPixelsY = int(borderPixelsX * 9/16)
                    
                
                    initialPosX = (labi_width * j )/self.width + 0.10*window_width 
                    #Modifica caso a proporção de labi_width mude
                    initialPosY = (labi_height * i)/self.height + 0.10*window_height
                    
                    newPosX = initialPosX + (labi_width/self.width)
                    newPosY = initialPosY + (labi_height/self.height)
                    
                    
                    if not (self.graph_map[i][j].acima()):
                        pygame.draw.line(window,(0,0,255),(initialPosX, initialPosY), (newPosX, initialPosY), borderPixelsY)
                    
                    
                    if not (self.graph_map[i][j].abaixo()):
                        pygame.draw.line(window,(0,0,255),(initialPosX, newPosY), (newPosX, newPosY), borderPixelsY)
                        
                        
                    if not (self.graph_map[i][j].direita()):
                        pygame.draw.line(window,(0,0,255),(newPosX, initialPosY), (newPosX, newPosY), borderPixelsX)
                        
                        
                    if not (self.graph_map[i][j].esquerda()):
                        pygame.draw.line(window,(0,0,255),(initialPosX, initialPosY), (initialPosX, newPosY), borderPixelsX)
                        

    def drawPathApple(self):
        
        for node in (self.otimoCaminhoMaca['caminho']):
        
            pos_x = (labi_width * node.j )/self.width + 0.10*window_width
            pos_y = (labi_height * node.i)/self.height + 0.10*window_height
            width = (labi_width/matrix_map.width)
            height = width*9/16
            
            pygame.draw.rect(window,(211,211,211), pygame.Rect((pos_x, pos_y), (width, height)))
            
    
    def drawPathNoApple(self):
        
        for node in (self.otimoCaminhoSemMaca):
        
            pos_x = (labi_width * node.j )/self.width + 0.10*window_width
            pos_y = (labi_height * node.i)/self.height + 0.10*window_height
            width = (labi_width/matrix_map.width)
            height = width*9/16
            
            pygame.draw.rect(window,(153, 153, 153), pygame.Rect((pos_x, pos_y), (width, height)))
        

    def __drawApple(self, actual_i, actual_j):
        
        
        pos_x = (labi_width * actual_j )/self.width + 0.10*window_width + (labi_width/matrix_map.width * 0.4)
        pos_y = (labi_height * actual_i)/self.height + 0.10*window_height + (labi_height/matrix_map.height * 0.4)
        
        width = (labi_width/self.width) * 0.2
        height = width*9/16
    
        pygame.draw.rect(window,(220,20,60), pygame.Rect((pos_x, pos_y), (width, height)))
                





pygame.init()
window = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()
runningGame = True
runningMenu = True


class Player:
    def __init__(self):
            
        self.actual_i =  matrix_map.Labirin.inicio.i
        self.actual_j  = matrix_map.Labirin.inicio.j
        self.playerX = ((labi_width * self.actual_j)/matrix_map.width) + ((window_width - labi_width) * 0.5) + (labi_width/matrix_map.width * 0.4)
        self.playerY = ((labi_height * self.actual_i) /matrix_map.height) + (window_height - labi_height) * 0.5 + (labi_height/matrix_map.height * 0.4)
        self.playerWidth = ((labi_width)/matrix_map.width) * 0.5
        self.playerHeight = ((labi_height)/matrix_map.height) * 0.5
        self.stepsCounter = 0
        self.score = 100


    def movePlayer(self):
        
        
        if event.key == pygame.K_RIGHT and (matrix_map.graph_map[self.actual_i][self.actual_j].direita()):
            self.playerX += (labi_width/matrix_map.width)
            self.actual_j += 1
            self.stepsCounter += 1
        if event.key == pygame.K_LEFT and (matrix_map.graph_map[self.actual_i][self.actual_j].esquerda()):
            self.playerX -= (labi_width/matrix_map.width)
            self.actual_j -= 1
            self.stepsCounter += 1
        if event.key == pygame.K_DOWN and (matrix_map.graph_map[self.actual_i][self.actual_j].abaixo()):
            self.playerY += (labi_height/matrix_map.height)
            self.actual_i += 1
            self.stepsCounter += 1
        if event.key == pygame.K_UP and (matrix_map.graph_map[self.actual_i][self.actual_j].acima()):
            self.playerY -= (labi_height/matrix_map.height)
            self.actual_i -= 1
            self.stepsCounter += 1
    
           
        self.checkApple()
        self.checkScore()
        
        
        print(self.playerX, self.playerY)
        
    def drawPlayer(self):
        pygame.draw.rect(window,(173,255,47), pygame.Rect((self.playerX, self.playerY), (self.playerWidth, self.playerHeight)))
        
    def checkApple(self):
        if matrix_map.graph_map[self.actual_i][self.actual_j].apple:
            matrix_map.graph_map[self.actual_i][self.actual_j].apple = False
            self.stepsCounter -= matrix_map.appleScore
            
    def checkScore(self):
        if(self.stepsCounter > len(matrix_map.otimoCaminhoSemMaca)):
           self.score = int ( ( len(matrix_map.otimoCaminhoSemMaca)/self.stepsCounter ) * 100 )
            
        

class GUI:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.width  = 'Largura'
        self.height = 'Altura'
        self.paths = 'Nº Caminhos'
        self.chooserApple = 'Mostrar Caminho (Com Maçãs)'
        self.chooserNoApple = 'Mostrar Caminho (Sem Maçãs)'
        self.appleQt = 'Nº Maçãs'
        self.appleScore = 'Pontos Maçãs'

    
    
    def drawButtons(self):
        
        widthButton = self.font.render(self.width, True, (0,0,0), (173,255,47))
        heightButton = self.font.render(self.height, True, (0,0,0), (173,255,47))
        pathsButton = self.font.render(self.paths, True, (0,0,0), (173,255,47))
        appleQtButton = self.font.render(self.appleQt, True, (0,0,0), (173,255,47))
        appleScoreButton = self.font.render(self.appleScore, True, (0,0,0), (173,255,47))
        startButton = self.font.render("Iniciar Jogo", True, (0,0,0), (173,255,47))
        
        widthButtonRect = widthButton.get_rect()
        heightButtonRect = heightButton.get_rect()
        pathsButtonRect = pathsButton.get_rect()
        appleQtButtonRect = appleQtButton.get_rect()
        appleScoreButtonRect = appleScoreButton.get_rect()
        startButtonRect = startButton.get_rect()
        
        widthButtonRect.center = (window_width*0.3, window_height*0.2)
        heightButtonRect.center = (window_width*0.7, window_height*0.2)
        pathsButtonRect.center = (window_width*0.5, window_height*0.4)
        appleQtButtonRect = (window_width*0.25, window_height*0.58)
        appleScoreButtonRect = (window_width*0.62, window_height*0.58)
        startButtonRect.center = (window_width*0.5, window_height*0.8)
        
        pygame.draw.rect(window,(173,255,47), pygame.Rect((window_width*0.2, window_height*0.15), (window_width*0.2, window_height*0.1)))
        pygame.draw.rect(window,(173,255,47), pygame.Rect((window_width*0.6, window_height*0.15), (window_width*0.2, window_height*0.1)))
        pygame.draw.rect(window,(173,255,47), pygame.Rect((window_width*0.4, window_height*0.35), (window_width*0.2, window_height*0.1)))
        pygame.draw.rect(window,(173,255,47), pygame.Rect((window_width*0.2, window_height*0.55), (window_width*0.2, window_height*0.1)))
        pygame.draw.rect(window,(173,255,47), pygame.Rect((window_width*0.6, window_height*0.55), (window_width*0.2, window_height*0.1)))
        pygame.draw.rect(window,(173,255,47), pygame.Rect((window_width*0.4, window_height*0.75), (window_width*0.2, window_height*0.1)))
        
        window.blit(widthButton, widthButtonRect)
        window.blit(heightButton, heightButtonRect)
        window.blit(pathsButton, pathsButtonRect)
        window.blit(appleQtButton, appleQtButtonRect)
        window.blit(appleScoreButton, appleScoreButtonRect)
        window.blit(startButton, startButtonRect)
        
    

    def drawCounter(self):
        
        value = player.stepsCounter
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        
        
        text = font.render('Passos:', True, (0,0,0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (window_width*0.95, window_height*0.1)
        window.blit(text, textRect)
        
        text = self.font.render(str(value), True, (0,0,0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (window_width*0.95, window_height*0.2)
        window.blit(text, textRect)
        
    def drawScore(self):
        value = player.score
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        
        text = font.render('Pontuação:', True, (0,0,0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (window_width*0.95, window_height*0.4)
        window.blit(text, textRect)
        
        text = self.font.render(str(value)+'%', True, (0,0,0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (window_width*0.95, window_height*0.5)
        window.blit(text, textRect)
        
    
    def drawPathAppleChooser(self):
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        
        text = font.render(gui.chooserApple, True, (0,0,0), (80, 80, 80))
        textRect = text.get_rect()
        textRect.center = (window_width*0.25, window_height*0.95)
        
        pygame.draw.rect(window,(80, 80, 80), pygame.Rect((window_width*0.1, window_height*0.925), (window_width*0.3, window_height*0.05)))
        
        window.blit(text, textRect)
        

    def drawPathNoAppleChooser(self):
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        
        text = font.render(gui.chooserNoApple, True, (0,0,0), (96, 96, 96))
        textRect = text.get_rect()
        textRect.center = (window_width*0.65, window_height*0.95)
        
        pygame.draw.rect(window,(96, 96, 96), pygame.Rect((window_width*0.5, window_height*0.925), (window_width*0.3, window_height*0.05)))
        
        window.blit(text, textRect)
        
        
    


gui = GUI()
actual_button = ''
value_text = ''

while runningGame:
    
    
    window.fill((255,255,255))
    
    mouse = pygame.mouse.get_pos()
    
    while runningMenu:
        
        window.fill((255,255,255))
        
        mouse = pygame.mouse.get_pos()
        
        if(actual_button == 'width'):
            gui.width = value_text
        if(actual_button == 'height'):
            gui.height = value_text
        if(actual_button == 'paths'):
            gui.paths = value_text
        if(actual_button == 'appleQt'):
            gui.appleQt = value_text
        if(actual_button == 'appleScore'):
            gui.appleScore = value_text
            
        
        for event in pygame.event.get():    
            
            if event.type == pygame.QUIT:
                runningMenu = False
                runningGame = False
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if window_width*0.4 <= mouse[0] <= window_width*0.6:
                    
                    if window_height*0.35 <= mouse[1] <= window_height*0.45:
                        actual_button = 'paths'
                        value_text = ''
                    
                    if window_height*0.75 <= mouse[1] <= window_height*0.85:
                        runningMenu = False
                        matrix_map = Map(int(gui.height), int(gui.width), int(gui.paths), int(gui.appleQt), int(gui.appleScore))
                        player = Player()
                        break
                    
                
                if window_height*0.15 <= mouse[1] <= window_height*0.25:
                
                    if window_width*0.2 <= mouse[0] <= window_width*0.4:
                        actual_button = 'width'
                        value_text = ''
                    
                    if window_width*0.6 <= mouse[0] <= window_width*0.8:
                        actual_button = 'height'
                        value_text = ''

                if window_height*0.55 <= mouse[1] <= window_height*0.65:
                
                    if window_width*0.2 <= mouse[0] <= window_width*0.4:
                        actual_button = 'appleQt'
                        value_text = ''
                    
                    if window_width*0.6 <= mouse[0] <= window_width*0.8:
                        actual_button = 'appleScore'
                        value_text = ''
                
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    value_text = value_text[0:-1]
                else:    
                    value_text += event.unicode
                print(actual_button)
                print(value_text)
                print(gui.width)
                    
            
            gui.drawButtons()

            pygame.display.update()    

            clock.tick(60)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningGame = False
            break
        elif event.type == pygame.KEYDOWN:
            try:
                player.movePlayer()
            except IndexError:
                runningMenu = True
                gui.width = 'Largura'
                gui.height = 'Altura'
                gui.paths = 'Nº Caminhos'
                gui.appleQt = 'Nº Maçãs'
                gui.appleScore = 'Pontos Maçãs'
                actual_button = ''
                value_text = ''
            if event.key == pygame.K_ESCAPE:
                runningGame = False
                break
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if window_width*0.1 <= mouse[0] <= window_width*0.4 and window_height*0.925 <= mouse[1] <= window_height*0.975\
                and gui.chooserApple == 'Esconder Caminho (Com Maçãs)':
                gui.chooserApple = 'Mostrar Caminho (Com Maçãs)'
                
                
            elif window_width*0.1 <= mouse[0] <= window_width*0.4 and window_height*0.925 <= mouse[1] <= window_height*0.975\
                and gui.chooserApple == 'Mostrar Caminho (Com Maçãs)':
                gui.chooserApple = 'Esconder Caminho (Com Maçãs)'
                
        
            if window_width*0.5 <= mouse[0] <= window_width*0.8 and window_height*0.925 <= mouse[1] <= window_height*0.975\
                and gui.chooserNoApple == 'Esconder Caminho (Sem Maçãs)':
                gui.chooserNoApple = 'Mostrar Caminho (Sem Maçãs)'
                
                
            elif window_width*0.5 <= mouse[0] <= window_width*0.8 and window_height*0.925 <= mouse[1] <= window_height*0.975\
                and gui.chooserNoApple == 'Mostrar Caminho (Sem Maçãs)':
                gui.chooserNoApple = 'Esconder Caminho (Sem Maçãs)'

    
    
    if(gui.chooserApple == 'Esconder Caminho (Com Maçãs)'):
        matrix_map.drawPathApple()

    if(gui.chooserNoApple == 'Esconder Caminho (Sem Maçãs)'):
        matrix_map.drawPathNoApple()
            

    
    
    gui.drawPathAppleChooser()
    
    gui.drawPathNoAppleChooser()
            
    gui.drawCounter()
    
    gui.drawScore()
    
    matrix_map.drawMap()
    
    player.drawPlayer()

    pygame.display.update()    

    clock.tick(60)
                        
    




pygame.quit()


