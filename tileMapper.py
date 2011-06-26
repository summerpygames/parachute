import pygame, sys

print "init"

tileSize = [50, 50]
screenSize = width, height = 1200, 900 # screen res of the XO laptops

"""
symbol list:

game tile mapper names
1 liquid w
2 land (ground) o
3 liquid by land |
4 liquid/ land corner /
5 liquid over land 
6 log end -
7 log middle =
"""

#ascii tile map for custom levels
oldTileMap = """wwwwwwwwwwwwwwwwwwwwwwww
wwww(=)w(=====)www(==)ww
>wwwwwwwwwwwwwwwwwwwwww<
o>wwwww(===)wwwwwwwwww<o
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
oo|wwwwwwwwwwwwwwwwww|oo
"""

tileMap = """wwwwwwwwwwwwwwwwwwwwwwwwwwww(=)w(=====)www(==)ww>wwwwwwwwwwwwwwwwwwwwww<o>wwwww(===)wwwwwwwwww<ooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oo"""

# tile file names
land = "land.bmp"
liquid = "liquid.bmp"
liquidByLand = "liquidByLand.bmp"
liquidOverLand  = "liquidOverLand.bmp"
liquidLandCorner = "liquidLandCorner.bmp"
liquidLandCornerLeft = "liquidLandCorner.bmp"
liquidLandCornerRight = "liquidLandCorner.bmp"

logEnd = "logEnd.bmp"
logMiddle = "logMiddle.bmp"
logEndLeft = "logEndLeft.bmp"
logEndRight = "logEndRight.bmp"



#do not:
#sys.exit()

i = 0 # location counting device
mapSize = [24, 18] #number of tiles for the screen
tileLocation = [0, 0] #starting x and y location for tile printing
mapArea = mapSize[0] * mapSize[1] #area of tile map, set with the number of tiles
fileLocation = "data\\" #dir for all files, data and images, setting as a filename allows easier access

tileChar = " " # set to a blank char at the start, read later as a single letter from the map string for image setting


screen = pygame.display.set_mode(screenSize)
print "\npost init"

pygame.font.init()

font = pygame.font.SysFont("Times New Roman", 30)
white = 255, 255, 255
font.render(tileChar, True, white)

while (i < mapArea):
    print "\nPRE letter assignment"
    tileChar = tileMap[i] #% mapSize[0])] #sets the tileChar to the letter standing for the images by reading the string of tiles like an array
    
    tileImage = pygame.image.load(fileLocation + liquid).convert()

    print "tileChar: (" + tileChar + ")\n"

    if tileChar == "w": #water tile
        tileImage = pygame.image.load(fileLocation + liquid).convert() #sets to the image for the land tile
        
    elif tileChar == "<":
        tileImage = pygame.image.load(fileLocation + liquidLandCorner).convert() #sets to the image for the land tile
        
    elif tileChar == ">":
        tileImage = pygame.image.load(fileLocation + liquidLandCorner).convert() #sets to the image for the land tile
        
    elif tileChar == "(":
        tileImage = pygame.image.load(fileLocation + logEnd).convert() #sets to the image for the land tile
        
    elif tileChar == ")":
        tileImage = pygame.image.load(fileLocation + logEnd).convert() #sets to the image for the land tile
        
    elif tileChar == "|":
        tileImage = pygame.image.load(fileLocation + liquidByLand).convert() #sets to the image for the land tile
        
    elif tileChar == "=":
        tileImage = pygame.image.load(fileLocation + logMiddle).convert() #sets to the image for the land tile
        

    ###tileImage = pygame.image.load(fileLocation + ground).convert()    
    tileRect = tileImage.get_rect()

    tileRect = tileRect.move(tileLocation[0], tileLocation[1])
    screen.blit(tileImage, tileRect) #"blits", draw pixels into buffer for display

    pygame.display.flip() #moves blits onto sceen

    if (tileLocation[0] >= mapSize[0]):
        tileLocation[0] = 0
        tileLocation[1] = tileLocation[1] + tileSize[1]
        #tileLocation[1] = tileLocation[0] + tileSize[1]
        
    else: # (tileLocation[0] < mapSize[0]):
        tileLocation[0] = tileLocation[0] + tileSize[1] 

    print "\nBefore i++, i =="
    print i

    i=i+1

print "exited while loop"
#pygame.display.flip() #moves blits onto sceen

pygame.font.quit()
