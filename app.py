import pygame, sys, random
from pygame.locals import *

from mapDraw import drawMap, randomMap
from menus import mainmenu
from config import display_height, display_width, version, save

class playerSprite(pygame.sprite.Sprite):
  frames = [ pygame.image.load('images/obj/player/character_stand_l.png'),
          pygame.image.load('images/obj/player/character_stand_r.png') ]

  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.rect = pygame.Rect(self.frames[0].get_rect())
    self.rect.center = (385,336)
    self.anim = 0

  def update(self, direction):
    if direction == 'u' or direction == 'l':
      self.anim = 0
    else:
      self.anim = 1
    self.image = self.frames[self.anim]


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
  #mapmusic = pygame.mixer.music.load('audio/music/.mp3')
  mapmusic = pygame.mixer.music.load('audio/music/BoxCat_Games_-_12_-_Passing_Time.mp3')
  walk = [pygame.mixer.Sound('audio/sfx/footstep01.ogg'),pygame.mixer.Sound('audio/sfx/footstep01.ogg')]
  font = pygame.font.Font('fonts/Minecraft.ttf', 16)
  
  # Load all frames of animation for the player
  #player = [pygame.image.load('images/obj/player/character_stand_l.png').convert(),pygame.image.load('images/obj/player/character_stand_r.png').convert()]
  player = playerSprite()
  
  tiles = [pygame.image.load('images/tiles/grass.png').convert(), pygame.image.load('images/tiles/wall.png').convert(),
           pygame.image.load('images/tiles/water.png').convert(), pygame.image.load('images/tiles/wood.png').convert()]
  blocking_tiles = [1,2]
  bg = pygame.image.load('images/bgs/stardust.png').convert()

  objs = [ { 'name': 'Coin',
             'value': 1,
             'weight': 0.01,
             'meta' : { 'max_quantity': 100000000000 },
           } ]
                        
  
  
  # Generate our map
  map = randomMap(tiles)

  coins = [  
    itemSprite((32,32)),
    itemSprite((720,480)),
    itemSprite((500,300)),
  ]
  coin_group = pygame.sprite.RenderPlain(*coins)
  player_group = pygame.sprite.RenderPlain(*[player])
  
  if not save:
    # Setup Variables
    xoffset = 0
    yoffset = 0
    xpos = 18
    ypos = 6
    
    health=60
    regen=0.1
    
    inventory = {}

    info_toggle = False
  
  # Event loop
  # pygame.mixer.music.play(0)
  while True:

    # Key Bindings
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ypos>0:
      if map[ypos][xpos-1] not in blocking_tiles:
        yoffset += 16
        xoffset += 32
        xpos -= 1
        #walk[random.randrange(2)].play()
        player.update('u')

    for event in pygame.event.get():
      # Mouse Bindings
      if event.type == MOUSEBUTTONDOWN:
        #sound.play()
        mx, my = pygame.mouse.get_pos()
        print("%s,%s" % (mx, my))

    if keys[K_LEFT] or keys[K_a] and ypos<len(map):
      # BUGGY if you walk off of the map
      if map[ypos+1][xpos] not in blocking_tiles:
        xoffset += 32
        yoffset -= 16
        ypos += 1
        #walk[random.randrange(2)].play()
        player.update('l')
    if keys[K_RIGHT] or keys[K_d] and ypos>0:
      if map[ypos-1][xpos] not in blocking_tiles:
        yoffset += 16
        xoffset -= 32
        ypos -= 1
        #walk[random.randrange(2)].play()
        player.update('r')
    if keys[K_UP] or keys[K_w] and xpos>0:
      if map[ypos][xpos-1] not in blocking_tiles:
        yoffset += 16
        xoffset += 32
        xpos -= 1
        #walk[random.randrange(2)].play()
        player.update('u')
    if keys[K_DOWN] or keys[K_s] and xpos<len(map[0]):
      if map[ypos][xpos+1] not in blocking_tiles:
        yoffset -= 16
        xoffset -= 32
        xpos += 1
        #walk[random.randrange(2)].play()
        player.update('d')
    # This info screen toggle will soon become inventory
    if keys[K_i]:
      if info_toggle:
        info_toggle = False
      else:
        info_toggle = True
    if keys[K_ESCAPE]:
      pygame.quit()
      sys.exit()
  
  
    if health<100:
      health += regen
  
    # Setup frame
    display.fill((0,0,0)) # fill to clear frame
    display.blit(bg,(0,0)) # background
    drawMap(xoffset, yoffset, tiles, display, map) # render the map
    #display.blit(player, (385,336)) # draw our character change to sprite later
    #[player].draw(display)
  
    # health bar horizontal
    pygame.draw.rect(display, (0,0,0), pygame.Rect(22,22,106,26))
    pygame.draw.rect(display, (200,0,0), pygame.Rect(25,25,health,20))
  
    # label and version
    label = font.render('isometric v%s' % version, True, (250,250,250))
    label_obj = label.get_rect()
    label_box = label_obj.center = (680,580)
    display.blit(label, label_box)
  
    # Draw sprites to screen
    pygame.sprite.RenderPlain(player)
    collisions = pygame.sprite.spritecollide(player, coin_group, True)
    coin_group.update(collisions)
    coin_group.draw(display)

    # Info
    if info_toggle:
      info = font.render("(%s,%s): Tile %s" % (xpos,ypos,map[ypos][xpos]), True, (250,250,250))
      info_obj = info.get_rect()
      info_box = label_obj.center = (25,580)
      display.blit(info,info_box)
  
      fps = font.render("fps: %s" % (int(clock.get_fps())), True, (250,250,250))
      fps_obj = fps.get_rect()
      fps_box = label_obj.center = (725,25)
      display.blit(fps,fps_box)
  
    clock.tick(30)
    pygame.display.update()


if __name__ == "__main__":
  mainmenu(gameloop)
