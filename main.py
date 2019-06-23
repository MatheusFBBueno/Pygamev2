import pygame
from player import Player
from wall import Wall
from interagivel import Interagivel
from texto import inserttext
from texto import write_fixed


#Constantes globais
guyF = pygame.image.load('images/dood_frontal.png')
guyL = pygame.image.load('images/dood_left.png')
guyR = pygame.image.load('images/dood_right.png')
guyB = pygame.image.load('images/dood_back.png')
guyF = pygame.transform.scale(guyF,(80,80))
guyL = pygame.transform.scale(guyL,(80,80))
guyR = pygame.transform.scale(guyR,(80,80))
guyB = pygame.transform.scale(guyB,(80,80))

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
BROWN= (188,100,28)
GRAY= (89,82,78)
# tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


pygame.init()
fonte= pygame.font.Font('pokemon_fire_red.ttf',24)
 
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
pygame.display.set_caption('QuestMan')

# lista de sprites
all_sprite_list = pygame.sprite.Group()
 
# paredes (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)


wall = Wall(10, 0, 790, 10)
wall_list.add(wall)

wall = Wall(790, 10, 10, 590)
wall_list.add(wall)

wall = Wall(10, 590, 790, 10)
wall_list.add(wall)

textbox = Wall(10,500,780,90)
textbox.image.fill(BLUE) 
wall_list.add(textbox)
all_sprite_list.add(textbox)

# Jogador
player = Player(160, 400,80,80)
player.definirImagem(guyF,guyB,guyL,guyR)
player.walls = wall_list
all_sprite_list.add(player)

clock = pygame.time.Clock()

#variáveis de locais visitados
visited_basement = False
visited_garden = False
secret_path= False #--ativa quando chega na última fase,leva para o lago
#variáveis de inventário
inv_peixe=False
inv_comida= False
inv_machado= False
chave_final=False
inv_dinheiro=False
def quarto(visited_basement,visited_garden):
    done = False
    keyS = False
    space= False

    wall1 = Wall(0, 437, 177, 63)
    wall_list.add(wall1)
    wall2 = Wall(557, 291, 146, 4)
    wall_list.add(wall2)
    wall3 = Wall(683, 308, 20, 151)
    wall_list.add(wall3)
    wall4 = Wall(566, 390, 138, 69)
    wall_list.add(wall4)
    wall5 = Wall(269, 437, 476, 62)
    wall_list.add(wall5)
    wall6 = Wall(177, 481, 92, 19)
    wall_list.add(wall6)
    wall7 = Wall(703, 285, 97, 215)
    wall_list.add(wall7)
    wall8 = Wall(768, 218, 22, 67)
    wall_list.add(wall8)
    wall9 = Wall(0, 0, 800, 145)
    wall_list.add(wall9)
    wall10 = Wall(319, 138, 128, 83)
    wall_list.add(wall10)
    wall11 = Wall(63, 122, 124, 64)
    wall_list.add(wall11)
    wall12 = Wall(0, 124, 63, 385)
    wall_list.add(wall12)
    wall13 = Wall(177, 481, 92, 19)
    wall_list.add(wall13)
    wall14 = Wall(703, 285, 97, 215)
    wall_list.add(wall14)
    wall15 = Wall(768, 218, 22, 67)
    wall_list.add(wall15)
    wall16 = Wall(0, 0, 800, 145)
    wall_list.add(wall16)
    wall17 = Wall(319, 138, 128, 83)
    wall_list.add(wall17)
    wall18 = Wall(63, 122, 124, 64)
    wall_list.add(wall18)
    wall19 = Wall(703, 138, 97, 62)
    wall_list.add(wall19)
    wall20 = Wall(63, 412, 60, 24)
    wall_list.add(wall20)

    bg_quarto= pygame.image.load("images/quarto.png")
    bg_quarto= pygame.transform.scale(bg_quarto,(800,500))
    leaf=  pygame.image.load("images/galho_quarto.png")
    leaf = pygame.transform.scale(leaf,(60,46))
    galho= Wall(63,373,60,46)
    galho.carregarImagem(leaf)
    all_sprite_list.add(galho)
    porta_porao = Interagivel(564,358,139,145,["Uma escada leva a um estranho porao.Descer?","S/N"])
    screen.fill(BLACK)
    porta_jardim = Interagivel(770,250,20,100,["A saida leva para um lago,sair?","S/N"])
    if visited_basement:
        player.rect.x=464
        player.rect.y =260
    if visited_garden:
        player.rect.x= 464
        player.rect.y= 260
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    keyS = True
        
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    keyS = False
        
        keyset =[keyS,space]
        #transição para porão
        if porta_porao.sayhi(player,textbox,fonte) and keyset[0]:
            wall_list.remove(wall1)
            wall_list.remove(wall2)
            wall_list.remove(wall3)
            wall_list.remove(wall4)
            wall_list.remove(wall5)
            wall_list.remove(wall6)
            wall_list.remove(wall7)
            wall_list.remove(wall8)
            wall_list.remove(wall9)
            wall_list.remove(wall10)
            wall_list.remove(wall11)
            wall_list.remove(wall12)
            wall_list.remove(wall13)
            wall_list.remove(wall14)
            wall_list.remove(wall15)
            wall_list.remove(wall16)
            wall_list.remove(wall17)
            wall_list.remove(wall18)
            wall_list.remove(wall19)
            wall_list.remove(wall20)
            all_sprite_list.remove(galho)
            porao(visited_basement,chave_final)
             
        #transição para jardim
        if porta_jardim.sayhi(player,textbox,fonte) and keyset[0]:
            wall_list.remove(wall1)
            wall_list.remove(wall2)
            wall_list.remove(wall3)
            wall_list.remove(wall4)
            wall_list.remove(wall5)
            wall_list.remove(wall6)
            wall_list.remove(wall7)
            wall_list.remove(wall8)
            wall_list.remove(wall9)
            wall_list.remove(wall10)
            wall_list.remove(wall11)
            wall_list.remove(wall12)
            wall_list.remove(wall13)
            wall_list.remove(wall14)
            wall_list.remove(wall15)
            wall_list.remove(wall16)
            wall_list.remove(wall17)
            wall_list.remove(wall18)
            wall_list.remove(wall19)
            wall_list.remove(wall20)
            all_sprite_list.remove(galho)
            jardim(visited_garden,inv_machado,inv_peixe,inv_dinheiro,inv_comida,secret_path)
        screen.blit(bg_quarto,(0,0))
        all_sprite_list.update()
        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        pygame.display.flip()
    
        clock.tick(60)

def porao(visited_basement,chave_final):
    done = False
    keyS = False
    space = False
    player.rect.x= 100
    player.rect.y=30
    escada_quarto = Interagivel(135,60,665,100,["Subir para o quarto?","S/N"])

    bg_basement = pygame.image.load("images/FasePorao.png")
    wall1 = Wall(180, 170, 10, 10)
    wall_list.add(wall1)

    wall2 = Wall(450, 100, 790, 10)
    wall_list.add(wall2)

    wall3 = Wall(380, 0, 10, 110)
    wall_list.add(wall3)

    wall4 = Wall(230, 150, 10, 10)
    wall_list.add(wall4)

    wall5 = Wall(280, 130, 10, 10)
    wall_list.add(wall5)

    wall6 = Wall(320, 110, 10, 10)
    wall_list.add(wall6)

    box = pygame.image.load("images/box.png")
    box = pygame.transform.scale(box,(100,100))
    
    box1=Wall(0,400,100,100)
    box1.carregarImagem(box)
    wall_list.add(box1)
    all_sprite_list.add(box1)
    
    box2=Wall(0,300,100,100)
    box2.carregarImagem(box)
    wall_list.add(box2)
    all_sprite_list.add(box2)
    
    box3=Wall(200,400,100,100)
    box3.carregarImagem(box)
    wall_list.add(box3)
    all_sprite_list.add(box3)
    
    box4=Wall(200,300,100,100)
    box4.carregarImagem(box)
    wall_list.add(box4)
    all_sprite_list.add(box4)
    
    
    realbox=Interagivel(100,400,100,100,["Todas as caixas estao empoeiradas,mas um estranho brilho vem do fundo","Tentar pegar o objeto?","S/N"])
    realbox.carregarImagem(box)
    wall_list.add(realbox)
    all_sprite_list.add(realbox)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    keyS = True
                if event.key == pygame.K_n:
                    keyn = True
        
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    keyS = False
        
        keyset =[keyS,space]
        all_sprite_list.update()
        if escada_quarto.sayhi(player,textbox,fonte) and keyset[0]:
            visited_basement = True
            wall_list.remove(wall1)
            wall_list.remove(wall2)
            wall_list.remove(wall3)
            wall_list.remove(wall4)
            wall_list.remove(wall5)
            wall_list.remove(wall6)
            wall_list.remove(box1)
            wall_list.remove(box2)
            wall_list.remove(box3)
            wall_list.remove(box4)
            wall_list.remove(realbox)

            all_sprite_list.remove(box1)
            all_sprite_list.remove(box2)
            all_sprite_list.remove(box3)
            all_sprite_list.remove(box4)
            all_sprite_list.remove(realbox)

            quarto(visited_basement,visited_garden)
        
        if realbox.sayhi(player,textbox,fonte) and keyset[0]:
            chave_final=  True
            player.key= True
        
        if chave_final:
            key= pygame.image.load("images/da_key.png")
            key = pygame.transform.scale(key,(40,30))
            keyfinal= Wall(700,560,40,30)
            keyfinal.carregarImagem(key)
            all_sprite_list.add(keyfinal)
        
        screen.blit(bg_basement,(0,0))
        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        pygame.display.flip()
    
        clock.tick(60)

def jardim(visited_garden,inv_machado,inv_peixe,inv_dinheiro,inv_comida,secret_path):
    done = False
    keyS = False
    space = False
    if player.secret== True:
        secret_path= True
    player.rect.x = 25
    player.rect.y = 300
    rock = Wall(0, 0, 800, 90)
    wall_list.add(rock)

    water = Wall(415, 0, 270, 250)
    wall_list.add(water)

    tree = Wall(75, 0, 50, 250)
    wall_list.add(tree)

    dog_house = Wall(295, 185, 100, 20)
    wall_list.add(dog_house)

    water2 = Wall(415, 400, 270, 250)
    wall_list.add(water2)
    img_fish= pygame.image.load("images/fish.png")
    img_fish= pygame.transform.scale(img_fish,(50,50))
    fish= Wall(700,500,50,50)
    fish.carregarImagem(img_fish)
    bg_lake = pygame.image.load("images/FaseLago.png")
    porta_quarto = Interagivel(10,440,20,60,["Entrar no quarto?","S/N"])

    path_mirror = Interagivel(770,400,20,100,["Uma porta para uma sala estranha.","continuar?","S/N"])
    
    img_axe= pygame.image.load("images/axe.png")
    img_axe=pygame.transform.scale(img_axe,(50,50))
    axe= Interagivel(80,250,50,50,["Um machado velho esta preso na arvore. Pegar?","S/N"])
    axe.carregarImagem(img_axe)
    
    fishing_rod= Interagivel(685,200,60,60,["Uma vara de pescar, talvez consiga um bom peixe se pescar.","pescar?","S/N"])
    img_rod= pygame.image.load("images/fishingrod.png")
    img_rod= pygame.transform.scale(img_rod,(60,60))
    fishing_rod.carregarImagem(img_rod)
    all_sprite_list.add(fishing_rod)
    
    secret_tunnel = Interagivel(135,90,100,50,["Esse tunel te trouxe da floresta,e pode te levar de volta","avancar para a floresta?","S/N"])
    if secret_path:
        player.rect.x = 135
        player.rect.y = 190
    img_chain = pygame.image.load("images/chain.png")
    img_chain= pygame.transform.scale(img_chain,(32,100))
    chain = Interagivel(415,300,32,150,["Um cadeado bloqueia seu caminho, talvez consiga quebra-lo com o machado","quebrar o cadeado?(isso quebra o machado)","S/N"])
    chain.carregarImagem(img_chain)
    all_sprite_list.add(chain)
    broke = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    keyS = True
        
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    keyS = False
        
        keyset =[keyS,space]
        all_sprite_list.update()
        

        
        if fishing_rod.sayhi(player,textbox,fonte) and keyset[0]:
            inv_peixe= True
        if inv_peixe:
            all_sprite_list.add(fish)
        else:
            all_sprite_list.remove(fish)
        
        #transição para quarto
        if porta_quarto.sayhi(player,textbox,fonte) and keyset[0]:
            all_sprite_list.remove(porta_quarto)
            all_sprite_list.remove(path_mirror)
            wall_list.remove(water)
            wall_list.remove(water2)
            wall_list.remove(rock)
            wall_list.remove(dog_house)
            wall_list.remove(tree)
            wall_list.remove(chain)
            if not inv_machado:
                all_sprite_list.remove(axe)
            all_sprite_list.remove(fishing_rod)
            all_sprite_list.remove(chain)
            visited_garden = True
            
            quarto(visited_basement,visited_garden)
        #transição para labirinto 
        screen.blit(bg_lake,(0,0))
        if path_mirror.sayhi(player,textbox,fonte) and keyset[0]:
            wall_list.remove(water)
            wall_list.remove(water2)
            wall_list.remove(rock)
            wall_list.remove(dog_house)
            wall_list.remove(tree)
            all_sprite_list.empty()
            transition_in(inv_peixe,inv_dinheiro,inv_comida,chave_final)
        #tunel *super* secreto
        if secret_path:
            if secret_tunnel.sayhi(player,textbox,fonte) and keyset[0]:
                all_sprite_list.remove(porta_quarto)
                all_sprite_list.remove(path_mirror)
                wall_list.remove(water)
                wall_list.remove(water2)
                wall_list.remove(rock)
                wall_list.remove(dog_house)
                wall_list.remove(tree)
                all_sprite_list.remove(fishing_rod)
                all_sprite_list.remove(fish)
                all_sprite_list.remove(chain)
                final_room(inv_peixe,inv_dinheiro,inv_comida,chave_final,secret_path)
        else:
            if not broke:
                all_sprite_list.add(axe)
                wall_list.add(chain)
                all_sprite_list.add(chain)
            
                if chain.sayhi(player,textbox,fonte) and keyset[0]:
                    if inv_machado:
                        broke = True
                        all_sprite_list.remove(chain)
                        all_sprite_list.remove(axe)
                        wall_list.remove(chain)
            if inv_machado:
                axe.rect.x=650
                axe.rect.y=500
            else:
                axe.rect.x=80
                axe.rect.y=250
                if axe.sayhi(player,textbox,fonte) and keyset[0]:
                    inv_machado= True
        all_sprite_list.draw(screen)

        textbox.image.fill(BLUE)
        pygame.display.flip()
    
        clock.tick(60)

def transition_in(inv_peixe,inv_dinheiro,inv_comida,chave_final):
    done = False
    keyS = False
    space = False
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        space= True
                elif event.type== pygame.KEYUP:
                    if event.key== pygame.K_SPACE:
                        space= False
        keyset =[keyS,space]
        if keyset[1]:
            maze(inv_peixe,inv_dinheiro,inv_comida,chave_final)
        screen.fill(BLACK)
        write_fixed(screen,fonte,"Depois de passar pela passagem,o caminho se fechou. Parece que nao tem como voltar.",WHITE,100,200)
        write_fixed(screen,fonte,"Pressione espaco para continuar.",WHITE,100,220)
        pygame.display.flip()
        clock.tick(60)
def transition_out(inv_peixe,inv_dinheiro,inv_comida,chave_final):
    done = False
    keyS = False
    space = False
    all_sprite_list.remove(player)
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        space= True
                elif event.type== pygame.KEYUP:
                    if event.key== pygame.K_SPACE:
                        space= False
        keyset =[keyS,space]
        if keyset[1]:
            final_room(inv_peixe,inv_dinheiro,inv_comida,chave_final,secret_path)                    
        screen.fill(BLACK)
        write_fixed(screen,fonte,"Voce conseguiu sair do labirinto.",WHITE,100,200)
        write_fixed(screen,fonte,"Pressione espaco para continuar.",WHITE,100,220)
        pygame.display.flip()
        clock.tick(60)


def maze(inv_peixe,inv_dinheiro,inv_comida,chave_final):
    maze_list=  pygame.sprite.Group()
    wall = Wall(0, 0, 0, 600)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(0, 670, 800, 0)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(0, 0, 800, 0)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(870, 0, 0, 670)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)



    #---

    wall = Wall(10, 8, 2, 584)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(11, 589, 735, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(785, 11, 2, 576)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(9, 3, 780, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(144, 362, 2, 165)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(229, 203, 2, 131)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(187, 395, 2, 99)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(101, 299, 2, 94)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(144, 75, 2, 124)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(59, 203, 2, 93)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(101, 139, 2, 96)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(144, 558, 2, 31)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(102, 461, 2, 27)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(58, 491, 2, 68)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(13, 459, 92, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(13, 331, 219, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(59, 363, 2, 68)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(59, 427, 86, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(63, 266, 167, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(146, 297, 44, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(144, 266, 2, 34)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(60, 556, 46, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(103, 523, 88, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(102, 527, 2, 32)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(187, 526, 2, 33)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(187, 557, 92, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(188, 491, 45, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(229, 493, 2, 34)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(13, 169, 42, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(13, 105, 93, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(60, 138, 129, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(870, 0, 2, 670)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(187, 74, 2, 67)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(59, 75, 85, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(59, 42, 2, 33)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(103, 40, 174, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(272, 42, 2, 61)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(229, 41, 2, 100)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(189, 169, 87, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(187, 173, 2, 65)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(103, 233, 86, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(147, 362, 172, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(231, 298, 216, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(400, 169, 2, 130)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(358, 138, 2, 131)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(315, 9, 2, 222)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(273, 169, 2, 101)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(275, 266, 86, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(233, 139, 81, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(315, 300, 2, 29)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(272, 333, 2, 30)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(193, 395, 82, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(229, 427, 2, 34)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(315, 363, 2, 60)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(319, 395, 43, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(231, 461, 131, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(273, 491, 173, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(401, 462, 2, 59)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(315, 559, 2, 30)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(358, 526, 2, 30)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(230, 524, 132, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(316, 105, 46, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(357, 10, 2, 67)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(401, 10, 2, 28)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(400, 74, 2, 66)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(361, 138, 42, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(443, 106, 2, 94)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(405, 170, 40, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(405, 234, 85, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(487, 138, 2, 98)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(445, 105, 87, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(528, 41, 2, 35)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(443, 40, 88, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(444, 300, 2, 30)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(360, 331, 45, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(401, 332, 2, 31)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(359, 362, 131, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(358, 364, 2, 34)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(402, 398, 2, 32)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(359, 429, 2, 31)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(359, 428, 44, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(400, 559, 2, 31)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(401, 557, 45, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(443, 526, 2, 33)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(445, 523, 45, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(487, 491, 2, 36)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(529, 524, 2, 66)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(487, 557, 42, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(573, 557, 44, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(488, 491, 172, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(572, 495, 2, 63)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(613, 461, 2, 36)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(657, 524, 2, 68)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(743, 525, 43, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(742, 527, 2, 34)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(699, 558, 46, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(613, 523, 91, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(699, 493, 2, 32)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(701, 492, 44, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(742, 462, 2, 33)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(657, 461, 88, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(657, 396, 2, 65)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(661, 395, 42, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(699, 298, 2, 99)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(703, 362, 42, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(744, 396, 42, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(743, 397, 2, 34)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(698, 427, 45, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(445, 459, 131, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(443, 430, 2, 62)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(528, 429, 2, 33)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(572, 429, 2, 32)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(573, 428, 44, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(615, 364, 2, 67)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(574, 361, 85, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(657, 138, 2, 227)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(401, 395, 176, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(487, 397, 2, 29)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(529, 300, 2, 96)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(487, 267, 2, 98)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(443, 266, 90, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(532, 331, 85, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(614, 233, 2, 102)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(745, 331, 39, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(743, 267, 2, 68)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(659, 266, 87, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(573, 203, 174, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(572, 106, 2, 193)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(698, 233, 48, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(742, 205, 2, 28)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(529, 298, 48, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(528, 106, 2, 164)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(701, 169, 84, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(742, 40, 2, 101)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(660, 137, 87, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(615, 105, 2, 62)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(699, 41, 2, 66)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(575, 105, 127, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(657, 9, 2, 62)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(573, 9, 2, 29)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(613, 40, 2, 37)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)

    wall = Wall(359, 73, 258, 2)
    maze_list.add(wall)
    all_sprite_list.add(wall)
    wall.paint(BLACK)
    guyF = pygame.image.load('images/dood_frontal.png')
    guyL = pygame.image.load('images/dood_left.png')
    guyR = pygame.image.load('images/dood_right.png')
    guyB = pygame.image.load('images/dood_back.png')
    guyF = pygame.transform.scale(guyF,(10,10))
    guyL = pygame.transform.scale(guyL,(10,10))
    guyR = pygame.transform.scale(guyR,(10,10))
    guyB = pygame.transform.scale(guyB,(10,10))

    player2 = Player(20, 20,10,10)
    player2.definirImagem(guyF,guyB,guyL,guyR)
    player2.walls = maze_list
    all_sprite_list.add(player2)


    done=False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player2.changespeed(-2, 0)
                elif event.key == pygame.K_RIGHT:
                    player2.changespeed(2, 0)
                elif event.key == pygame.K_UP:
                    player2.changespeed(0, -2)
                elif event.key == pygame.K_DOWN:
                    player2.changespeed(0, 2)


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player2.changespeed(2, 0)
                elif event.key == pygame.K_RIGHT:
                    player2.changespeed(-2, 0)
                elif event.key == pygame.K_UP:
                    player2.changespeed(0, 2)
                elif event.key == pygame.K_DOWN:
                    player2.changespeed(0, -2)

        all_sprite_list.update()
        screen.fill(WHITE)
        all_sprite_list.draw(screen)
        if player2.rect.x in range(746,786) and player2.rect.y >580:
            all_sprite_list.empty()
            maze_list.empty()
            transition_out(inv_peixe,inv_dinheiro,inv_comida,chave_final)
        pygame.display.flip()

        clock.tick(60)




def final_room(inv_peixe,inv_dinheiro,inv_comida,chave_final,secret_path):
    done = False
    keyS = False
    space = False
    player.rect.x=200
    player.rect.y=32
    gateopen= False  
    all_sprite_list.add(player)
    all_sprite_list.add(textbox)  
    
    bg_finalC = pygame.image.load("images/background_closed_final.png")
    bg_finalC= pygame.transform.scale(bg_finalC,(800,600))
    bg_finalO = pygame.image.load("images/background_open_final.png")
    bg_finalO=pygame.transform.scale(bg_finalO,(800,600))
    img_background = pygame.image.load("images/galho_arvore1_final.png")
    img_background = pygame.transform.scale(img_background,(105, 104))
    background = Interagivel(60,329,105,104,[""])
    background.carregarImagem(img_background)
    all_sprite_list.add(background)

    tun_img= pygame.image.load('images/door_open.png')
    tun_img= pygame.transform.scale(tun_img,(100,100))
    secret_tunnel = Interagivel(0,243,100,100,["Esse tunel segue na direcao da casa","se voce passar pelo tunel o cachorro voltara ao seu posto,prosseguir?","S/N"])
    secret_tunnel.carregarImagem(tun_img)
    all_sprite_list.add(secret_tunnel)
    wall_list.add(secret_tunnel)



    img_npc1=pygame.image.load("images/fishyboi.png")
    img_npc1=pygame.transform.scale(img_npc1,(100,100))
    fish_npc = Interagivel(100,0,100,100,["Se me der um bom peixe eu te pagarei bem.","vender o peixe?","S/N"])
    fish_npc.carregarImagem(img_npc1)
    all_sprite_list.add(fish_npc)
    wall_list.add(fish_npc)

    img_npc2=pygame.image.load("images/oldman.png")
    img_npc2=pygame.transform.scale(img_npc2,(100,100))
    food_npc= Interagivel(340,30,100,100,["Um vendedor de racao.","Se tiver dinheiro,talvez possa alimentar o cachorro feroz. Comprar?","S/N"])
    food_npc.carregarImagem(img_npc2)
    wall_list.add(food_npc)
    all_sprite_list.add(food_npc)

    

    img_doge= pygame.image.load("images/dog_btw.png")
    img_doge=pygame.transform.scale(img_doge,(80,80))
    dog= Interagivel(300,220,80,80,["Um cachorro feroz bloqueia seu caminho.Se tivesse comida,poderia disrtai-lo","Dar comida ao cachorro?","S/N"])
    dog.carregarImagem(img_doge)
    all_sprite_list.add(dog)
    wall_list.add(dog)
    
    gate = Interagivel(397, 193, 15, 151,["Um portao que necessita de uma chave, talvez voce tenha que procura-la","Abrir o portao?(chave necessaria)","S/N"])
    wall_list.add(gate)
    all_sprite_list.add(gate)

    wall = Wall(426, 10, 22, 169)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(192, 207, 27, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(65, 108, 94, 73)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(397, 207, 53, 45)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(10, 180, 184, 15)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(10, 343, 787, 54)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(349, 179, 442, 15)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(393, 393, 53, 101)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    fish= Wall(700,500,50,50)
    img_fish= pygame.image.load("images/fish.png")
    img_fish= pygame.transform.scale(img_fish,(50,50))
    fish.carregarImagem(img_fish)
    
    img_food= pygame.image.load("images/dog_food.png")
    img_food= pygame.transform.scale(img_food,(40,40))
    food_icon=Wall(740,550,40,40)
    food_icon.carregarImagem(img_food)
    
    moni = pygame.image.load("images/moni.png")
    moni= pygame.transform.scale(moni,(40,40))
    money_icon=Wall(740,550,40,40)
    money_icon.carregarImagem(moni)
    
    key= pygame.image.load("images/da_key.png")
    key = pygame.transform.scale(key,(40,30))
    keyfinal= Wall(690,550,40,30)
    keyfinal.carregarImagem(key)
    doggo = True
    if player.key== True:
        chave_final= True
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    keyS = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    keyS = False
        

        keyset =[keyS,space]
        if chave_final:
            all_sprite_list.add(keyfinal)
        if inv_peixe== True:
            all_sprite_list.add(fish)
        else:
            all_sprite_list.remove(fish)
        
        if inv_comida:
            all_sprite_list.add(food_icon)
        else:
            all_sprite_list.remove(food_icon)
        
        if inv_dinheiro:
            all_sprite_list.add(money_icon)
        else:
            all_sprite_list.remove(money_icon)
        
        if gate.sayhi(player,textbox,fonte) and keyset[0]:
            if chave_final:
                wall_list.remove(gate)
                bg_finalC= bg_finalO
                gate.text= [""]
                all_sprite_list.remove(gate)        
        if inv_peixe:
            if fish_npc.sayhi(player,textbox,fonte) and keyset[0]:
                inv_dinheiro = True
                inv_peixe= False
        if inv_dinheiro:
            if food_npc.sayhi(player,textbox,fonte) and keyset[0]:
                inv_comida= True
                inv_dinheiro= False
                
        if inv_comida:
            if dog.sayhi(player,textbox,fonte) and keyset[0]:
                all_sprite_list.remove(dog)
                wall_list.remove(dog)
                dog.text= [""]
                inv_comida= False
                player.passe= True
        if secret_tunnel.sayhi(player,textbox,fonte) and keyset[0]:
            wall_list.empty()
            wall_list.add(textbox)
            all_sprite_list.remove(dog)
            all_sprite_list.remove(fish_npc)
            all_sprite_list.remove(food_npc)
            all_sprite_list.remove(secret_tunnel)
            all_sprite_list.remove(background)
            jardim(visited_garden,inv_machado,inv_peixe,inv_dinheiro,inv_comida,secret_path)
        finish = Interagivel(700,0,100,600,[''])

        all_sprite_list.update()
        screen.blit(bg_finalC,(0,0))
        secret_path= True
        player.secret= True
        all_sprite_list.draw(screen)
        textbox.image.fill(BLUE)
        pygame.display.flip()

        if finish.sayhi(player,textbox,fonte): 
            all_sprite_list.empty()
            wall_list.empty()
            end_screen()
        clock.tick(60)
def end_screen():
    done = False
    all_sprite_list.empty()
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    quit()
        screen.fill(BLACK)
        write_fixed(screen,fonte,"Voce terminou o jogo! Obrigado por jogar.",WHITE,100,200)
        pygame.display.flip()
        clock.tick(60)
def loop_principal():
    done = False
    while not done:
        quarto(visited_basement,visited_garden)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            
loop_principal()
pygame.quit()