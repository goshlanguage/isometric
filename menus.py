import pygame, sys
from pygame.locals import *
from config import display_height, display_width, version

#from ui import button

pygame.init()
display = pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption('Isometric v%s' % version)
start = pygame.image.load('images/obj/start.png').convert()
menubg = pygame.image.load('images/obj/mainmenubg.png').convert()

def mainmenu(main):
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    # menu
    display.fill((225,225,225))

    # bg
    for y in range(0,display_width, 180):
      for x in range(0, display_height, 104):
        display.blit(menubg, (x,y))

    titleFont = pygame.font.Font('fonts/04B_30.ttf',72)
    subFont = pygame.font.Font('fonts/04B_30.ttf',32)
    titleSurf = titleFont.render('Isometric', True, (0,0,0))
    subSurf = subFont.render('by Ryan Hartje', True, (0,0,0))
    titleRect = titleSurf.get_rect() 
    subRect = subSurf.get_rect()
    titleRect.center = ((display_width/2),(display_height/4))
    subRect.center = ((display_width/2),((display_height/4)+100))
    display.blit(titleSurf, titleRect)

    button("Start",display_height-(display_height/3),display_width/2,100,50,(50,50,50),(255,255,255),main)
    pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(display, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(display, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf = smallText.render(msg, True, (0,0,0))
    textRect = textSurf.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    display.blit(textSurf, textRect)
