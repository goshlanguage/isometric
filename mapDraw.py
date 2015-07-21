# from assets import map
#
import random

def randomMap(tiles):
  size = 64
  rmap = [[]]
  for x in range(0,size-1):
    rmap.append([])
    for y in range(0,size-1):

      # Let's make sure at least 85% of our tiles are walkable
      dice = int(random.randrange(0,100))
      if dice>85:
        # in the 15% of the time we do gen a random tile,
        #  let's try to clump similar types together
        if not y > 0 or random.randint(1,10) < 5:
          randomTile = int(random.randrange(0, len(tiles)))
        else:
          if random.randint(0,1) == 0 or x == 0:
            if rmap[x][y-1] == 1 or rmap[x][y-1] == 2:
              randomTile = rmap[x][y-1]
            else:
              randomTile = 2
          else:
            randomTile = rmap[x-1][y]
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
 
