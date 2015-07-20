import pygame, sys, random
from pygame.locals import *

from mapDraw import drawMap
from assets import map


# Load Resources
pygame.init()
display = pygame.display.set_mode((800,600), DOUBLEBUF)
pygame.display.set_caption("Iso")
clock = pygame.time.Clock()
pygame.mixer.init()
mapmusic = pygame.mixer.music.load('audio/music/BoxCat_Games_-_12_-_Passing_Time.mp3')
walk = [pygame.mixer.Sound('audio/sfx/footstep01.ogg'),pygame.mixer.Sound('audio/sfx/footstep01.ogg')]


# Load all frames of animation for the player
player = [pygame.image.load('images/obj/player_walk_0.png').convert(),pygame.image.load('images/obj/player_walk_1.png').convert()]

tiles = [pygame.image.load('images/tiles/grass.png').convert(), pygame.image.load('images/tiles/wall.png').convert(),
         pygame.image.load('images/tiles/water.png').convert()]
clouds = pygame.image.load('images/bgs/clouds.jpg').convert()

# Setup Variables
xoffset = 0
yoffset = 0

xpos = 6
ypos = 6

# We want our character animation to be on the first frame
ani = 0
# set alpha for all character animations
for i in player:
  player[ani].set_colorkey((255,0,255))
  ani += 1
ani = 0

# Event loop
# pygame.mixer.music.play(0)
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    # Mouse Bindings
    if event.type == MOUSEBUTTONDOWN:
        #sound.play()
        mx, my = pygame.mouse.get_pos()
        print("%s,%s" % (mx, my))

    # Key Bindings
    if event.type == KEYDOWN:
      if event.key == K_LEFT or event.key == K_a:
        xoffset += 64 
        xpos -= 1
        walk[random.randrange(2)].play()
      if event.key == K_RIGHT or event.key == K_d:
        xoffset -= 64
        xpos += 1
        walk[random.randrange(2)].play()
      if event.key == K_UP or event.key == K_w:
        yoffset += 32
        ypos -= 1
        walk[random.randrange(2)].play()
      if event.key == K_DOWN or event.key == K_s:
        yoffset -= 32
        ypos += 1
        walk[random.randrange(2)].play()
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()
      # animate the character
      if ani == 1:
        ani = 0
      else:
        ani += 1

    print("(%s,%s)" % (xpos, ypos))
    print(map[xpos][ypos])


  display.fill((0,0,0))
  display.blit(clouds,(0,0))
  drawMap(xoffset, yoffset, tiles, display)
  display.blit(player[ani], (384,320))

  clock.tick(30)
  pygame.display.update()
