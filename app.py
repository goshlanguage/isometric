import pygame, sys
from pygame.locals import *
from mapDraw import drawMap
from assets import map

pygame.init()
display = pygame.display.set_mode((800,600), DOUBLEBUF)
pygame.display.set_caption("Iso")
clock = pygame.time.Clock()


#wall = pygame.image.load('wall.png').convert()
#grass = pygame.image.load('grass.png').convert()
tiles = [pygame.image.load('grass.png').convert(), pygame.image.load('wall.png').convert(),
         pygame.image.load('water.png').convert()]

tileWidth = 64
tileHeight = 64

xoffset = 0
yoffset = 0

xpos = 6
ypos = 11

# Event loop
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYUP:
      if event.key == K_LEFT or event.key == K_a:
        xoffset += 64 
        xpos -= 1
      if event.key == K_RIGHT or event.key == K_d:
        xoffset -= 64
        xpos += 1
      if event.key == K_UP or event.key == K_w:
        yoffset += 32
        ypos -= 1
      if event.key == K_DOWN or event.key == K_s:
        yoffset -= 32
        ypos += 1 
      elif event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()

    print("(%s,%s)" % (xpos, ypos))
    print(map[xpos][ypos])

    drawMap(xoffset, yoffset, tiles, display)  
    player = pygame.image.load('player.png').convert() 
    player.set_colorkey((0,0,0))
    display.blit(player, (384,320))

    pygame.display.update()
    clock.tick(30)
