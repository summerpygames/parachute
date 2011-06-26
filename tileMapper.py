# tileMapper.py
# for "Mind The Gap"
# maps out the image tiles for the background of the game
#
# 
# git: http://www.github.com/summerpygames/parachute
# 
# 
# TODO:
# print out aall of the tiles in the right spot
# probaly needs to be in a function, with image sets as inputs, for each different world
# 
# 
# 
 
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

#good tile map codewise, no newlines, etc, but harder on the users/devs eyes, could strip all whitespace from the old style one and output to a new var instead ("string are immutable"...)
tileMap = """wwwwwwwwwwwwwwwwwwwwwwwwwwww(=)w(=====)www(==)ww>wwwwwwwwwwwwwwwwwwwwww<o>wwwww(===)wwwwwwwwww<ooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oooo|wwwwwwwwwwwwwwwwww|oo"""

# tile file names for ease 
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





mapSize = [24, 18] #number of tiles for the screen
tileLocation = [0, 0] #starting x and y location for tile printing
mapArea = mapSize[0] * mapSize[1] #area of tile map, set with the number of tiles
fileLocation = "data\\" #dir for all files, data and images, setting as a filename allows easier access

tileChar = " " # set to a blank char at the start, read later as a single letter from the map string for image setting


screen = pygame.display.set_mode(screenSize) #sets the virtual screen size to the res specified
print "\npost init"

pygame.font.init() #init fonts for later

#trying to make a loading screen, NEED to do in parralel while the image buffering is actually running (at the blit comomand in the while?)
font = pygame.font.SysFont("Times New Roman", 30)
white = 255, 255, 255
font.render("loading", True, white)
font.render("loading..", True, white)
font.render("loading..", True, white)
font.render("loading...", True, white)

font.render(tileChar, True, white) #print the tile letter

#i = 0 # location counting device

#while (i < mapArea):
#for i in tileMap:
for tileChar in tileMap:
    print "\nPRE letter assignment"
    #tileChar = tileMap[(i)] #% mapSize[0])] #sets the tileChar to the letter standing for the images by reading the string of tiles like an array
    
    tileImage = pygame.image.load(fileLocation + liquid).convert()

    print "tileChar: (" + tileChar + ")\n"

    if tileChar == "w" : #water tile
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

    tileRect = tileRect.move(tileLocation[0], tileLocation[1]) #move draw location to the right spot, (x,y)
    screen.blit(tileImage, tileRect) #"blits", draw pixels into buffer for display

    pygame.display.flip() #moves blits onto sceen

    if (tileLocation[0] >= mapSize[0]): #if x co-ord is at the right edge, bigger than the map size
        tileLocation[0] = 0 #set the draw location back to the left edge
        tileLocation[1] = tileLocation[1] + tileSize[1] #and move the y co-ord down by the height of one tile
        #tileLocation[1] = tileLocation[0] + tileSize[1] #?
        
    else: # (tileLocation[0] < mapSize[0]): #if not past the edge
        tileLocation[0] = tileLocation[0] + tileSize[1] #move the tile drawing to the right by the width of one tile

    print "\nBefore i++, i =="
    #print i

    #i=i+1

print "exited while loop"
#pygame.display.flip() #moves blits onto sceen

pygame.font.quit()

#don't do this yet
#sys.exit()


#I think there is a function in python that can show where the program was called from, example: the menu, and then we couldreopen that program after
#this is finished (or on exit code or error) instead of keeping it running in the background and not blitting, either could theoretically work though. (-josh)

