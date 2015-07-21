# from assets import map
#
import random

def randomMap(tiles):
  size = 128
  rmap = [[]]
  for x in range(0,size-1):
    rmap.append([])
    for y in range(0,size-1):

      # Let's make sure at least 75% of our tiles are walkable
      dice = int(random.randrange(0,100))
      if dice>75:
        randomTile = int(random.randrange(0, len(tiles)))
        rmap[x].append(randomTile)
      else:
        rmap[x].append(0)
  return rmap

def drawMap(xoffset,yoffset,tiles,display,map):
  currentRow = 0 # y
  currentTile = 0 # x
  for row in map:
    for tile in row:
      tileImage = tiles[map[currentRow][currentTile]]
      tileImage.set_colorkey((0,0,0))
  
      cartx = currentTile*64
      carty = currentRow*64

      x = xoffset + 0 + ((cartx - carty) / 2)
      y = yoffset + 0 + ((cartx+carty) / 4)
  
      currentTile+=1
      display.blit(tileImage, (x,y))
    
    currentTile = 0 # Reset for new row
    currentRow += 1
 
