import pygame, sys, random
from pygame.locals import *

from mapDraw import drawMap, randomMap
from menus import mainmenu
from config import display_height, display_width, version, save, fps_setting


class playerSprite(pygame.sprite.Sprite):
  frames = [ pygame.image.load('images/obj/player/character_stand_l.png'),
             pygame.image.load('images/obj/player/character_stand_l2.png'),
             pygame.image.load('images/obj/player/character_stand_r.png'),
             pygame.image.load('images/obj/player/character_stand_r2.png')]

  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.rect = pygame.Rect(self.frames[0].get_rect())
    #self.rect.center = (420,320) 
    #372)
    self.anim = 0
    self.image = self.frames[0]

  def update(self, direction):
    if direction == 'u' or direction == 'l':
      if self.anim >= int(len(self.frames)/2):
        self.anim = 0
    else:
      if self.anim >= len(self.frames)-1:
        self.anim = int(len(self.frames)/2)
      
    self.anim += 1
    self.image = self.frames[self.anim]

# Refactor so any sprite/item can be created by passing an array (sprite)
class itemSprite(pygame.sprite.Sprite):
  norm = [ pygame.image.load('images/obj/coin/coin_1.png'),
    pygame.image.load('images/obj/coin/coin_2.png'),
    pygame.image.load('images/obj/coin/coin_3.png'),
    pygame.image.load('images/obj/coin/coin_4.png') ]
  
  def __init__(self, position):
    pygame.sprite.Sprite.__init__(self) 
    self.rect = pygame.Rect(self.norm[0].get_rect())
    self.rect.center = position
    self.anim = 0

  def update(self, hitlist):
    if self in hitlist: self.image = None
    else: 
      self.anim += 1
      if self.anim >= len(self.norm): self.anim = 0
      self.image = self.norm[self.anim]


def gameloop():
  # Load Resources
  pygame.init()
  display = pygame.display.set_mode((display_height,display_width), DOUBLEBUF)
  pygame.display.set_caption("Isometric")
  clock = pygame.time.Clock()
  pygame.mixer.init()
  mapmusic = pygame.mixer.music.load('audio/bg.mp3')
  #mapmusic = pygame.mixer.music.load('audio/sfx/menu_screen.mp3')
  #walk = [pygame.mixer.Sound('audio/sfx/footstep01.ogg'),pygame.mixer.Sound('audio/sfx/footstep01.ogg')]
  font = pygame.font.Font('fonts/Minecraft.ttf', 16)
  
  # Load all frames of animation for the player
  player = [ pygame.image.load('images/obj/player/character_stand_l.png').convert(),
             pygame.image.load('images/obj/player/character_stand_l2.png').convert(),
             pygame.image.load('images/obj/player/character_stand_r.png').convert(),
             pygame.image.load('images/obj/player/character_stand_r2.png').convert()]

  tiles = [pygame.image.load('images/tiles/grass.png').convert(),
           pygame.image.load('images/tiles/water.png').convert(),
           pygame.image.load('images/tiles/brick.png').convert(),
           pygame.image.load('images/tiles/water.jpg').convert()]
  
  #, pygame.image.load('images/tiles/wall.png').convert(),
           #pygame.image.load('images/tiles/water.png').convert(), pygame.image.load('images/tiles/wood.png').convert()]
  blocking_tiles = [1,2]
  bg = pygame.image.load('images/bgs/stardust.png').convert()

  
  
  # Generate our map
  map = randomMap(85,tiles)

  # Setup our sprites
  players = [ playerSprite(), ]

  # This should be moved to the map drawing to handle coordinates for x,y and offset.
  #coins = [  
  #  itemSprite((500,300)),
  #]
 
  # Render our groups to the display
  player_group = pygame.sprite.RenderPlain(*players)
  #coin_group = pygame.sprite.RenderPlain(*coins)
  
  if not save:
    # Setup Variables
    xoffset = 0
    yoffset = 0
    xpos = 18
    ypos = 10
    
    health=60
    stamina=40
    regen=1
    
    inventory = {}

    info_toggle = False
  
  # Event loop
  # pygame.mixer.music.play(0)

  while True:
    for event in pygame.event.get():
      # Mouse Bindings
      if event.type == MOUSEBUTTONDOWN:
        #sound.play()
        mx, my = pygame.mouse.get_pos()
        print("%s,%s" % (mx, my))
      if event.type == KEYDOWN:
          if event.key == K_i:
            if info_toggle:
              info_toggle = False
            else:
              info_toggle = True
          if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit(1)

    # Key Bindings
    keys = pygame.key.get_pressed()

    if not ypos == len(map)-1 and (keys[K_LEFT] or keys[K_a]):
      # BUGGY if you walk off of the map
      #if map[ypos+1][xpos] not in blocking_tiles:
        xoffset += 32
        #yoffset -= 16
        #ypos += 1
        xpos += 1
        #walk[random.randrange(2)].play()
        player_group.update('l')

    if ypos>0 and (keys[K_RIGHT] or keys[K_d]):
      #if map[ypos-1][xpos] not in blocking_tiles:
        #yoffset += 16
        xoffset -= 32
        #ypos -= 1
        xpos -= 1
        #walk[random.randrange(2)].play()
        player_group.update('r')

    if xpos>0 and (keys[K_UP] or keys[K_w]):
      #if map[ypos][xpos-1] not in blocking_tiles:
        yoffset += 32
        #xoffset += 32
        #xpos -= 1
        ypos -= 1
        #walk[random.randrange(2)].play()
        player_group.update('u')

    if not xpos == len(map[0])-1 and (keys[K_DOWN] or keys[K_s]):
      #if map[ypos][xpos+1] not in blocking_tiles:
        yoffset -= 32
        #xoffset -= 32
        #xpos += 1
        ypos += 1
        #walk[random.randrange(2)].play()
        player_group.update('d')


  
  
    if health<100:
      health += regen

    if stamina<100:
      stamina += regen
  
    # Setup frame
    display.fill((0,0,0)) # fill to clear frame
    display.blit(bg,(0,0)) # background
    drawMap(xoffset, yoffset, tiles, display, map) # render the map
    #display.blit(player[0], (385,336)) # draw our character change to sprite later
  
    # health bar horizontal
    pygame.draw.rect(display, (0,0,0), pygame.Rect(22,20,106,12))
    pygame.draw.rect(display, (200,0,0), pygame.Rect(25,22,health,8))

    # Stamina
    pygame.draw.rect(display, (0,0,0), pygame.Rect(22,36,106,12))
    pygame.draw.rect(display, (200,200,200), pygame.Rect(25,38,stamina,8))
  
    # Draw sprites to screen
    #collisions = pygame.sprite.spritecollide(players[0], coin_group, True)
    #coin_group.update(collisions)
    #coin_group.draw(display)

    player_group.draw(display)

    # Info
    if info_toggle:

      # label and version
      label = font.render('isometric v%s' % version, True, (250,250,250))
      label_obj = label.get_rect()
      label_box = label_obj.center = (680,580)
      display.blit(label, label_box)
       
      try:
        info = font.render("(%s,%s): Tile %s" % (ypos,xpos,map[ypos][xpos]), True, (250,250,250))
      except:
        info = font.render("(%s,%s): Tile %s" % (ypos,xpos,"error"), True, (250,250,250))
      
      info_obj = info.get_rect()
      info_box = label_obj.center = (25,580)
      display.blit(info,info_box)
  
      fps = font.render("fps: %s" % (int(clock.get_fps())), True, (250,250,250))
      fps_obj = fps.get_rect()
      fps_box = label_obj.center = (725,25)
      display.blit(fps,fps_box)


  
    clock.tick(fps_setting)
    pygame.display.update()
    pygame.display.flip()


if __name__ == "__main__":
  mainmenu(gameloop)
