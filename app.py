import pygame, sys, random
from pygame.locals import *

from mapDraw import drawMap, randomMap
from menus import mainmenu
from config import display_height, display_width, save


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
  font = pygame.font.Font('fonts/minecraft.ttf', 16)
  
  # Load all frames of animation for the player
  player = [pygame.image.load('images/obj/player/character_stand_l.png').convert(),pygame.image.load('images/obj/player/character_stand_r.png').convert()]
  
  tiles = [pygame.image.load('images/tiles/grass.png').convert(), pygame.image.load('images/tiles/wall.png').convert(),
           pygame.image.load('images/tiles/water.png').convert(), pygame.image.load('images/tiles/wood.png').convert()]
  blocking_tiles = [1,2]
  bg = pygame.image.load('images/bgs/stardust.png').convert()

  objs = [ { 'name': 'Coin',
             'value': 1,
             'weight': 0.01,
             'meta' : { 'max_quantity': 100000000000 },
             'blit' : [ pygame.image.load('images/obj/coin/coin_1.png'), 
                        pygame.image.load('images/obj/coin/coin_2.png'), 
                        pygame.image.load('images/obj/coin/coin_3.png'), 
                        pygame.image.load('images/obj/coin/coin_4.png') ]
           } ]
                        
  
  
  # Generate our map
  map = randomMap(tiles)
  
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
        if event.key == K_LEFT or event.key == K_a and ypos<len(map):
          # BUGGY if you walk off of the map
          if map[ypos+1][xpos] not in blocking_tiles:
            xoffset += 32
            yoffset -= 16
            ypos += 1
            #walk[random.randrange(2)].play()
            ani = 0
        if event.key == K_RIGHT or event.key == K_d and ypos>0:
          if map[ypos-1][xpos] not in blocking_tiles:
            yoffset += 16
            xoffset -= 32
            ypos -= 1
            #walk[random.randrange(2)].play()
            ani = 1
        if event.key == K_UP or event.key == K_w and xpos>0:
          if map[ypos][xpos-1] not in blocking_tiles:
            yoffset += 16
            xoffset += 32
            xpos -= 1
            ani = 0
            #walk[random.randrange(2)].play()
        if event.key == K_DOWN or event.key == K_s and xpos<len(map[0]):
          if map[ypos][xpos+1] not in blocking_tiles:
            yoffset -= 16
            xoffset -= 32
            xpos += 1
            ani = 1
            #walk[random.randrange(2)].play()
        if event.key == K_i:
          if info_toggle:
            info_toggle = False
          else:
            info_toggle = True
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
  
  
    if health<100:
      health += regen
  
    # Setup frame
    display.fill((0,0,0)) # fill to clear frame
    display.blit(bg,(0,0)) # background
    drawMap(xoffset, yoffset, tiles, display, map) # render the map
    display.blit(player[ani], (385,336)) # draw our character
  
    # health bar
    pygame.draw.rect(display, (0,0,0), pygame.Rect(22,22,106,26))
    pygame.draw.rect(display, (200,0,0), pygame.Rect(25,25,health,20))
  
    # label and version
    label = font.render('isometric v0.1', True, (250,250,250))
    label_obj = label.get_rect()
    label_box = label_obj.center = (680,580)
    display.blit(label, label_box)
  
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
  
      debug = font.render("xpos: %s" % (xpos),True, (250,250,250))
      debug_obj = debug.get_rect()
      debug_box = debug_obj.center = (725,50)
      display.blit(debug,debug_box)
  
      debug1 = font.render("ypos: %s" % (ypos),True, (250,250,250))
      debug1_obj = debug1.get_rect()
      debug1_box = debug1_obj.center = (725,75)
      display.blit(debug1,debug1_box)
  
      debug2 = font.render("nextu:%s" % (map[ypos][xpos-1]),True, (250,250,250))
      debug2_obj = debug2.get_rect()
      debug2_box = debug2_obj.center = (725,100)
      display.blit(debug2,debug2_box)
  
      debug3 = font.render("nextd:%s" % (map[ypos][xpos+1]),True, (250,250,250))
      debug3_obj = debug3.get_rect()
      debug3_box = debug3_obj.center = (725,125)
      display.blit(debug3,debug3_box)
  
    clock.tick(30)
    pygame.display.update()


if __name__ == "__main__":
  mainmenu(gameloop)
