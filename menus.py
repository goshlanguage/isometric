import pygame, sys
from pygame.locals import *
from config import display_height, display_width, version

#from ui import button

pygame.init()
display = pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption('Isometric v%s' % version)
start = [pygame.image.load('images/obj/button.png').convert(), pygame.image.load('images/obj/button_i.png').convert()]
menubg = pygame.image.load('images/obj/mainmenubg.png').convert()



menu_music = pygame.mixer.music.load('audio/sfx/menu_screen.mp3')
menu_item = pygame.mixer.Sound('audio/sfx/menu_item.ogg')

def quit():
  pygame.quit()
  sys.exit()

def mainmenu(main):
  titleFont = pygame.font.Font('fonts/04B_30.ttf',72)
  #subFont = pygame.font.Font('fonts/04B_30.ttf',32)
  titleSurf = titleFont.render('Isometric', True, (0,0,0))
  #subSurf = subFont.render('by Ryan Hartje', True, (0,0,0))
  titleRect = titleSurf.get_rect()
  #subRect = subSurf.get_rect()
  titleRect.center = ((400,100))
  #subRect.center = ((400,200))

  # MUTED, save me
  #pygame.mixer.music.play(0)
  while True:
    for event in pygame.event.get():
      # This is for when you click X on the game window
      if event.type == pygame.QUIT:
        quit()

      # And this is for when you hit Escape in the Menu screen.
      keys = pygame.key.get_pressed()
      if keys[K_ESCAPE]:
        quit()

    # menu
    display.fill((225,225,225))

    # draw repeating isometric background
    for y in range(0,display_width, 180):
      for x in range(0, display_height, 104):
        display.blit(menubg, (x,y))


    display.blit(titleSurf, titleRect)
    #display.blit(subSurf, subRect)


    button("Start",300,300,200,50,start[0],start[1],main)
    pygame.display.update()

# label, x,y, width, height, inactive_color, active_color, action or subprogram
def button(msg,x,y,w,h,inactive_image, active_image,action=None):
    played=False
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if not played:
          #buggy
          #menu_item.play()
          played=True
        #pygame.draw.rect(display, ac,(x,y,w,h))
        display.blit(active_image, (x,y))

        if click[0] == 1 and action != None:
            action()
    else:
        #pygame.draw.rect(display, inactive_image,(x,y,w,h))
        display.blit(active_image, (x,y))
        played=False
    smallText = pygame.font.Font("fonts/Minecraft.ttf",26)

    textSurf = smallText.render(msg, True, (245,245,245))
    textRect = textSurf.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    display.blit(textSurf, textRect)
