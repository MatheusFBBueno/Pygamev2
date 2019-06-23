import pygame
#classe base de interagiveis
class Interagivel(pygame.sprite.Sprite):
    posx = 0
    posy = 0
    def __init__(self, x, y, width, height ,text:list):
        super().__init__()
        self.text = text
        self.image = pygame.Surface([width,height],pygame.SRCALPHA,32)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.len_x = width
        self.len_y = height

    def carregarImagem(self,imagem):
        self.image.blit(imagem,(0,0))
    
    def sayhi(self,player,textbox,fonte):
        if player.rect.x in range(self.rect.x -100,self.rect.x+int(self.len_x*1.25)) and player.rect.y in range(self.rect.y -100,self.rect.y+int(self.len_y*1.25)):
            for i in range(len(self.text)):
                textbox.image.blit(fonte.render(self.text[i],True,(0,0,0)),(self.posx,self.posy))
                self.posy += 20
            self.posy = 0
            return True



