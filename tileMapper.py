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
tileSize = 50
tileChar = " " # set to a blank char at the start, read later as a single letter from the map string for image setting

pygame.font.init() #init fonts for later
#prints out loading , gets overwritten once done
font = pygame.font.SysFont("Ariel", 50)
white = 255, 255, 255
text = font.render("loading...", True, white)
screen.blit(text, (600,450))

# Load images beforehand for better blit times
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


mapString = open(os.path.join("data", "tileMap.txt"), "r")
#mapString = mapString.lower() #convert to lowercase, helps make the symbols valid

tileMap = []
for line in mapString:
	tileMap.append(list(line.strip()))#map(string, line.split()))


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
	xCoord = 0
	yCoord = 0
	for line in tileMap:  #read each line in the 2d array
		for tileChar in line:   #then read each char from that sub-array
			tileImage = tileCharRead(tileChar)	#load the matching image
   			tileRect = tileImage.get_rect()		#get the rectangle
			tileRect = tileRect.move(xCoord, yCoord) #move draw location to the right spot, (x,y)
			screen.blit(tileImage, tileRect) #blits, draw pixels into buffer for display

			if (xCoord < (23 * tileSize)): #if not past the right edge of the line/screen
				xCoord += tileSize
			else: 
				xCoord = 0

		if (yCoord < (17 * tileSize)):	
			yCoord += tileSize
	pygame.display.flip() #moves blits onto scene


def searchLogs(tileMap):	
	logX = 0
	logY = 0
	logLocation = []
	for line in tileMap: #checks each line 
		if (("(" in line != False) and (")" in line != False)):
			logLocation.append([line.index('('), logY, (line.index(')')-line.index('(')) ]) # appends x and y coords, and end-start
		logY+=1
	print logLocation

def findLogs(tileMap):
	foundLogs = []
	findX = 0
	findY = 0
	while (findX <= 17):
	    while (findY <= 23):
	        if tileMap[findX][findY] == "(":
	            for i in range(findY, 24):
	                if tileMap[findX][i] == ")":
	                    foundLogs.append([findX, findY, (i - findY + 1)])
	        findY += 1
	    findY = 0
	    findX += 1
	return foundLogs


def objectMove(tileMap, log):
	yCoord = findLogs(tileMap)[0][0]
	xCoord = findLogs(tileMap)[0][1]
	xLength = findLogs(tileMap)[0][2]
	tileMap.pop(0)
	tileMap.pop(0)
	tileMap.pop(0)
	tileMap.pop(0)

	tileMap.insert(0, ")")
	tileMap.insert(0, "=")
	tileMap.insert(0, "(")
	tileMap.insert(0, "w")
	
			
	#tileMap.pop[xCoord, ]
	
	#tileObjectBuffer = ""
	#tileObjectBuffer = tileMap[0] + tileMap[1] + tileMap[2]
	#tileMap.pop(0)
	#tileMap.insert(0, "w")
	
	#tileMap.insert(0, (tileObjectBuffer.split()))

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

				if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q) or (event.key == pygame.K_BACKSPACE) :
					waitToExit()
					getKeys = False
				else:
					getKeys = False
def waitToExit():
	#exitIn = raw_input("\n(press enter to quit)\n")
	pygame.quit()
	
def main(yes):
	while True:
		tileMapPrint()
		getInput()
		tileMapPrint()
		print tileMap
		print yes*10

#main("y")

pygame.font.quit()

