from assets import map
# 

def drawMap(xoffset,yoffset,tiles,display):
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
 
