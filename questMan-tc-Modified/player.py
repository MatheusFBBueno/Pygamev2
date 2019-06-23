import pygame

class Player(pygame.sprite.Sprite):

    # Constructor function
    def __init__(self, x, y,lenX,lenY):
        super().__init__()
 
        # altura, largura
        self.image = pygame.Surface([lenX, lenY],pygame.SRCALPHA,32)
        self.image.convert_alpha()

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.key=False
        self.secret= False
        # vetor de velocidade
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def definirImagem(self,IMF,IMB,IML,IMR):
        self.image.blit(IMF,(0,0))
        self.imf = IMF
        self.imb = IMB
        self.iml = IML
        self.imr = IMR
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def update(self):
        #atualizar imagem
        transparent = (0,0,0,0)
        if self.change_y > 0:
            self.image.fill(transparent)
            self.image.blit(self.imf,(0,0))
        elif self.change_y <0:
            self.image.fill(transparent)
            self.image.blit(self.imb,(0,0))
        else:
            if self.change_x >0:
                self.image.fill(transparent)
                self.image.blit(self.imr,(0,0))
            elif self.change_x <0:
                self.image.fill(transparent)
                self.image.blit(self.iml,(0,0))


        # mover
        self.rect.x += self.change_x
 
        # conferir se há uma parede
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
        # mesma coisa p/ vertical
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom