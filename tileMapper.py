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

import pygame, sys, os

screenSize = width, height = 1200, 900 # screen res of the XO laptops
screen = pygame.display.set_mode(screenSize) #sets the virtual screen size to the res specified

pygame.display.set_caption('Mind The Gap (Team Parachute 2011)')

#mapString = "" #sets the map to an empty string first, incase the file cannot be opened
#mapStringFile = file(os.path.join("data", "tileMap.txt" ), "r") #prepares the file for reading

mapString = open(os.path.join("data", "tileMap.txt"), "r")

tileMap = []
for line in mapString:
	tileMap.append(list(line.strip()))#map(string, line.split()))
	
for i in tileMap:
	print i

print tileMap
#mapString = mapStringFile.read() #read the chars one by one, all of them into the variable
#mapString = mapString.lower() #convert to lowercase, helps make the symbols valid

#tileMap = list(mapString)

# tile file names for refering later 
land = "land.png"
liquid = "liquid.png"

liquidByLand = "liquidByLand.png"
landByLiquid = "landByLiquid.png"

liquidOverLand  = "liquidOverLand.png"

liquidLandCorner = "liquidLandCorner.png"
landLiquidCorner = "landLiquidCorner.png"

logEnd = "logEnd.png"
logMiddle = "logMiddle.png"
endLog = "endLog.png"

mapSize = [24, 18] #number of tiles for the screen
tileLocation = [0, 0] #starting x and y location for tile printing
mapArea = mapSize[0] * mapSize[1] #area of tile map, set with the number of tiles
fileLocation = "data" #dir for all files, data and images, setting as a filename allows easier access
tileSize = [50, 50]
tileChar = " " # set to a blank char at the start, read later as a single letter from the map string for image setting


pygame.font.init() #init fonts for later
#trying to make a loading screen, NEED to do in parralel while the image buffering is actually running (at the blit comomand in the while?)
font = pygame.font.SysFont("Ariel", 50)
white = 255, 255, 255
text = font.render("loading...", True, white)
screen.blit(text, (600,450))



#### Load images beforehand for better blit times
liquidI = pygame.image.load(os.path.join("data", liquid)).convert() #load the image tile and sets it to a variable for later
landI = pygame.image.load(os.path.join("data", land)).convert() #load the image tile and sets it to a variable for later

liquidOverLandI = pygame.image.load(os.path.join("data", liquidOverLand)).convert() #load the image tile and sets it to a variable for later

liquidLandCornerI = pygame.image.load(os.path.join("data", liquidLandCorner)).convert() #load the image tile and sets it to a variable for later
landLiquidCornerI = pygame.image.load(os.path.join("data", landLiquidCorner)).convert() ##load the image tile and sets it to a variable for later

logMiddleI = pygame.image.load(os.path.join("data", logMiddle)).convert() #load the image tile and sets it to a variable for later
logEndI = pygame.image.load(os.path.join("data", logEnd)).convert() #load the image tile and sets it to a variable for later
endLogI = pygame.image.load(os.path.join("data", endLog)).convert() #load the image tile and sets it to a variable for later


liquidByLandI = pygame.image.load(os.path.join("data", liquidByLand)).convert() #load the image tile and sets it to a variable for later
landByLiquidI = pygame.image.load(os.path.join("data", landByLiquid)).convert() #load the image tile and sets it to a variable for later


def tileCharRead(tileChar): #picks the correct image for each ascii stand-in
    
    #sets the tileImage to the picture loaded for the tile, so we can always refer to the current tile with the same name during each loop
    #detects the matching char from the string and matches it with the right image
    if tileChar == "w" : #if the char stands for the water tile 
        tileImage = liquidI

    elif tileChar == "o" :
        tileImage = landI

    elif tileChar == "<":
        tileImage = liquidLandCornerI 
    elif tileChar == ">":
        tileImage = landLiquidCornerI 

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

    return tileImage

            
def tileMapPrint():    #prints the tiles from the map    
    for tileChar in tileMap:

        tileImage = tileCharRead(tileChar)
        
        tileRect = tileImage.get_rect()

        tileRect = tileRect.move(tileLocation[0], tileLocation[1]) #move draw location to the right spot, (x,y)
        screen.blit(tileImage, tileRect) #"blits", draw pixels into buffer for display

        if (tileLocation[0] >= width): #if x co-ord is at the right edge, bigger than the map size
            tileLocation[0] = 0 #set the draw location back to the left edge
            tileLocation[1] = tileLocation[1] + tileSize[1] #and move the y co-ord down by the height of one tile
            
        elif (tileLocation[0] < width): #if not past the edge
            tileLocation[0] = tileLocation[0] + tileSize[1] #move the tile drawing to the right by the width of one tile

        elif (tileLocation[0] == width and tileLocation[1] == height): #if at the end of the ENTIRE array,
			tileLocation[0] = 0 # reset to the start					
			tileLocation[1] = 0
	
        else:
			tileLocation[0] = 0 # reset to the start                                        
			tileLocation[1] = 0
			print "error"
			return 1
    pygame.display.flip() #moves blits onto scene


def objectMove(tileMap, tileObjectBuffer):
	#tileObjectBuffer = ""
	#tileObjectBuffer = tileMap[0] + tileMap[1] + tileMap[2]
	tileMap.pop(0)
	tileMap.pop(0)
	tileMap.pop(0)
	tileMap.pop(0)
	#tileMap.insert(0, ")") 
	#tileMap.pop(4)
	#tileMap.insert(1, tileObjectBuffer) 
	
	tileMap.insert(0, ")")
	tileMap.insert(0, "=")
	tileMap.insert(0, "(")
	
	tileMap.insert(0, "w")

def getInput():	
	getKeys = True
	while getKeys:
		for event in pygame.event.get():
			if event.type  == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					objectMove(tileMap, "(=)")
					getKeys = False
				if event.key == pygame.K_LEFT:
					objectMove(tileMap, "(=)")
					getKeys = False
				if event.key == pygame.K_DOWN:
					objectMove(tileMap, "(=)")
					getKeys = False
				if event.key == pygame.K_RIGHT:
					objectMove(tileMap, "(=)")
					getKeys = False
				if event.key == pygame.K_RETURN:
					objectMove(tileMap, "(=)")
					getKeys = False

				if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
					waitToExit()
					getKeys = False
				else:
					getKeys = False
def waitToExit():
	#exitIn = raw_input("\n(press enter to quit)\n")
	pygame.quit()
	
while True:
	tileMapPrint()
	getInput()
	tileMapPrint()
	#waitToExit()
	print tileMap
	print "/n/nPOSTPRINT"

#def main()


pygame.font.quit()

