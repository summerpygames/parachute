# tileMapper.py
# For "Mind The Gap"
# maps out the image tiles for the background of the game
# git: http://www.github.com/summerpygames/parachute
# 
# TODO:
# probaly needs to be in a function, with image sets as inputs, for each different world
# 
#-josh
#

import pygame, sys

screenSize = width, height = 1200, 900 # screen res of the XO laptops
screen = pygame.display.set_mode(screenSize) #sets the virtual screen size to the res specified

mapString = "" #sets the map to an empty string first, incase the file cannot be opened
mapStringFile = file("tileMap.txt", "r") #prepares the file for reading
mapString = mapStringFile.read() #read the chars one by one, all of them into the variable
mapString = mapString.lower() #convert to lowercase, helps make the symbols valid

tileMap = [' ']
j=0
#convert the map into and array after reading, for better speed (maybe)
tileMap = list(mapString)
mapString = mapString + "alkjsfinm"
print mapString
# tile file names for refering later 
land = "land.bmp"
liquid = "liquid.bmp"

liquidByLand = "liquidByLand.bmp"
landByLiquid = "landByLiquid.bmp"

liquidOverLand  = "liquidOverLand.bmp"

liquidLandCorner = "liquidLandCorner.bmp"
landLiquidCorner = "landLiquidCorner.bmp"

logEnd = "logEnd.bmp"
logMiddle = "logMiddle.bmp"
endLog = "endLog.bmp"

mapSize = [24, 18] #number of tiles for the screen
tileLocation = [0, 0] #starting x and y location for tile printing
mapArea = mapSize[0] * mapSize[1] #area of tile map, set with the number of tiles
fileLocation = "data\\" #dir for all files, data and images, setting as a filename allows easier access
tileSize = [50, 50]
tileChar = " " # set to a blank char at the start, read later as a single letter from the map string for image setting

pygame.font.init() #init fonts for later

#trying to make a loading screen, NEED to do in parralel while the image buffering is actually running (at the blit comomand in the while?)
font = pygame.font.SysFont("Times New Roman", 30)
white = 255, 255, 255
font.render("loading", True, white)
font.render("loading..", True, white)
font.render("loading..", True, white)
font.render("loading...", True, white)

font.render(tileChar, True, white) #print the tile letter

#### Load images beforehand for better blit times, etc
liquidI = pygame.image.load(fileLocation + liquid).convert() #load the image tile and sets it to a variable for later
landI = pygame.image.load(fileLocation + land).convert() #load the image tile and sets it to a variable for later

liquidOverLandI = pygame.image.load(fileLocation + liquidOverLand).convert() #load the image tile and sets it to a variable for later

liquidLandCornerI = pygame.image.load(fileLocation + liquidLandCorner).convert() #load the image tile and sets it to a variable for later
landLiquidCornerI = pygame.image.load(fileLocation + landLiquidCorner).convert() ##load the image tile and sets it to a variable for later

logMiddleI = pygame.image.load(fileLocation + logMiddle).convert() #load the image tile and sets it to a variable for later
logEndI = pygame.image.load(fileLocation + logEnd).convert() #load the image tile and sets it to a variable for later
endLogI = pygame.image.load(fileLocation + endLog).convert() #load the image tile and sets it to a variable for later


liquidByLandI = pygame.image.load(fileLocation + liquidByLand).convert() #load the image tile and sets it to a variable for later
landByLiquidI = pygame.image.load(fileLocation + landByLiquid).convert() #load the image tile and sets it to a variable for later

        
for tileChar in tileMap:
    #old, while loop ver:
    #tileChar = tileMap[(i)] #% mapSize[0])] #sets the tileChar to the letter standing for the images by reading the string of tiles like an array
    
    tileImage = pygame.image.load(fileLocation + liquid).convert()

    if tileChar == "w" : #if the char stands for the water tile
        #tileImage = pygame.image.load(fileLocation + liquid).convert() #sets to the image for the tile
        tileImage = liquidI

    elif tileChar == "o" :
        #tileImage = pygame.image.load(fileLocation + liquid).convert() #sets to the image for the tile
        tileImage = landI

    #detects the matching char from the string and matches it with the right image
    elif tileChar == "<":
        tileImage = liquidLandCornerI #sets the tileImage to the picture loaded for the tile, so we can always refer to the current tile with the same name during each loop
    elif tileChar == ">":
        tileImage = landLiquidCornerI #''

    elif tileChar == "=":
        tileImage = logMiddleI
    elif tileChar == "(":
        tileImage = endLogI
    elif tileChar == ")":
        tileImage = logEndI

    elif tileChar == "]":
        tileImage = landByLiquidI
    elif tileChar == "[":
        tileImage = liquidByLandI

    elif tileChar == "_":
        tileImage = liquidOverLandI

    else: #if the char does not match any of the valid symbols, default the image to water
        tileImage = liquidI

    tileRect = tileImage.get_rect()

    tileRect = tileRect.move(tileLocation[0], tileLocation[1]) #move draw location to the right spot, (x,y)
    screen.blit(tileImage, tileRect) #"blits", draw pixels into buffer for display

    if (tileLocation[0] >= width): #if x co-ord is at the right edge, bigger than the map size
        tileLocation[0] = 0 #set the draw location back to the left edge
        tileLocation[1] = tileLocation[1] + tileSize[1] #and move the y co-ord down by the height of one tile
        
    else: # (tileLocation[0] < mapSize[0]): #if not past the edge
        tileLocation[0] = tileLocation[0] + tileSize[1] #move the tile drawing to the right by the width of one tile

pygame.display.flip() #moves blits onto sceen

pygame.font.quit()

#don't do this yet
#sys.exit()


#I think there is a function in python that can show where the program was called from, example: the menu, and then we couldreopen that program after
#this is finished (or on exit code or error) instead of keeping it running in the background and not blitting, either could theoretically work though. (-josh)

