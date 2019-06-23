import pygame
pygame.init()

def inserttext(screen,fonte,text,color,posx,posy,keyset):
    if keyset[0]:
        text += 'q'
    if keyset[1]:
        text += 'w'
    if keyset[2]:
        text += 'e'
    if keyset[3]:
        text+='r'
    if keyset[4]:
        text+='t'
    if keyset[5]:
        text += 'y'
    if keyset[6]:
        text+='u' 
    if keyset[7]:
        text+='i'
    if keyset[8]:
        text += 'o'
    if keyset[9]:
        text+='p'
    if keyset[10]:
        text+='a'
    if keyset[0]:
        text+='s'
    if keyset[12]:
        text +='d'
    if keyset[13]:
        text+='f'
    if keyset[14]:
        text+='g'
    if keyset[15]:
        text +='h'
    if keyset[16]:
        text+='j'
    if keyset[17]:
        text+='k'
    if keyset[18]:
        text+='l'
    if keyset[19]:
        text+='z'
    if keyset[20]:
        text+='x'
    if keyset[21]:
        text+='c'
    if keyset[22]:
        text += 'v'
    if keyset[23]:
        text+='b'
    if keyset[24]:
        text+='n'
    if keyset[25]:
        text+='m'
    if keyset[26]:     
        text= text[:len(text)-1]
    if keyset[1]:
        text+= ' '
    screen.blit(fonte.render(text,True,color),(posx,posy))

def write_fixed(screen,fonte,text,color,posx,posy):
    screen.blit(fonte.render(text,True,color),(posx,posy))