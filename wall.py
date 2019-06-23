import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
 
        self.image = pygame.Surface([width, height],pygame.SRCALPHA,32)
        self.image.convert_alpha()
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def carregarImagem(self,imagem):
        self.image.blit(imagem,(0,0))

    def paint(self,color:tuple):
        self.image.fill(color)