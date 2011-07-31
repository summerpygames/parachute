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

import pygame, sys, os, array, string

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

currentLevel = os.path.join("levels", "desert")

dateFolder = "data"

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
liquidI = pygame.image.load(os.path.join("data", currentLevel, liquid)).convert() #load the image tile and sets it to a variable for later
landI = pygame.image.load(os.path.join("data", currentLevel, land)).convert() #load the image tile and sets it to a variable for later

liquidOverLandI = pygame.image.load(os.path.join("data", currentLevel, liquidOverLand)).convert() #load the image tile and sets it to a variable for later

liquidLandCornerI = pygame.image.load(os.path.join("data", currentLevel, liquidLandCorner)).convert() #load the image tile and sets it to a variable for later
landLiquidCornerI = pygame.image.load(os.path.join("data", currentLevel, landLiquidCorner)).convert() ##load the image tile and sets it to a variable for later

logMiddleI = pygame.image.load(os.path.join("data", currentLevel,  logMiddle)).convert() #load the image tile and sets it to a variable for later
logEndI = pygame.image.load(os.path.join("data",currentLevel,  logEnd)).convert() #load the image tile and sets it to a variable for later
endLogI = pygame.image.load(os.path.join("data", currentLevel, endLog)).convert() #load the image tile and sets it to a variable for later

liquidByLandI = pygame.image.load(os.path.join("data", currentLevel, liquidByLand)).convert() #load the image tile and sets it to a variable for later
landByLiquidI = pygame.image.load(os.path.join("data", currentLevel, landByLiquid)).convert() #load the image tile and sets it to a variable for later


mapString = open(os.path.join("data", currentLevel, "tileMap.txt"), "r")
#mapString = mapString.lower() #convert to lowercase, helps make the symbols valid

selectedLog = 0

tileMap = []
logMap = []
backgroundMap = []
bridgeMap = []
def mapInit():
    #tileMap = []
    #logMap = []
    #backgroundMap = []

    for line in mapString: # the whole map
          tileMap.append(list(line.strip()))#map(string, line.split()))
    
    #create the log-only map
    lineBuffer = []
    for line in tileMap:
        for letter in line:             
            letter = letter.replace('w', '0') # replace all non-log tiles with zeros as spacing, '0' strings are skipped when blitting
            letter = letter.replace('<', '0')
            letter = letter.replace('>', '0')
            letter = letter.replace('o', '0')
            letter = letter.replace('|', '0')
            letter = letter.replace('[', '0')
            letter = letter.replace(']', '0')
            lineBuffer.append(letter)
        logMap.append(lineBuffer)
        lineBuffer = []

    #create the background item only map
    for line in tileMap:    # go through each line
        for letter in line:  # one letter at a time
            letter = letter.replace('(', '0') # and replace all logs with blanks (0 strings) , which are jumped over when blitting :)
            letter = letter.replace(')', '0')
            letter = letter.replace('=', '0')
            lineBuffer.append(letter)
        backgroundMap.append(lineBuffer)
        lineBuffer = []

    print "logMap:\n "
    print tileMap
    print backgroundMap
    print logMap
    #tileMapPrint(logMap)
        
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
            
def tileMapPrint(tileMap):    #prints the tiles from the map    
        xCoord = 0
        yCoord = 0
        for line in tileMap:  #read each line in the 2d array
                for tileChar in line:   #then read each char from that sub-array
			if tileChar != '0':
				tileImage = tileCharRead(tileChar)      #load the matching image
                        	tileRect = tileImage.get_rect()         #get the rectangle
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
                        logLocation.append([line.index('('), logY, (line.index(')')-line.index('(')), line.index(')') ]) # appends x and y coords, and end-start
                logY+=1
        print logLocation

def findLogs(tileMap):
        foundLogs = []
        findX = 0
        findY = 0
        while (findX <= 17):
            while (findY <= 23):
                print findX, findY
                if tileMap[findX][findY] == "(":
                    for i in range(findY, 24):
                        if tileMap[findX][i] == ")":
                                foundLogs.append([findX, findY, i])
                findY += 1
            findY = 0
            findX += 1
        print foundLogs
        return foundLogs

"""
def bridgeCheck(tileMap):
	found = False
	fir line in tileMap:
                if line.join() == ""
"""

def getInput(): 
        getKeys = True
        while getKeys:
                for event in pygame.event.get(): # polls each thing happining
                        if event.type  == pygame.KEYDOWN: # if equal to a keypress
                                #if (event.key == pygame.K_UP) or (event.key == pygame.K_PAGEUP): # and if the key presesed is a certian one
                                #        #objectMove(logMap, "up")
                                #        getKeys = False
                                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_END):
                                        objectMove(logMap, "left", selectedLog)
                                        getKeys = False
                                #if (event.key == pygame.K_DOWN) or (event.key == pygame.K_PAGEDOWN):
                                #        #objectMove(logMap, "down")
                                #        getKeys = False
                            
                                if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_HOME):
                                        objectMove(logMap, "right", selectedLog)
                                        getKeys = False
                                if event.key == pygame.K_RETURN:
                                        objectMove(logMap, "return", selectedLog)
                                        getKeys = False
                                
  

                                if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q) or (event.key == pygame.K_BACKSPACE):
                                        waitToExit()
                                        getKeys = False
                                else:
                                        getKeys = False
def waitToExit():
        #exitIn = raw_input("\n(press enter to quit)\n")
        pygame.quit()
        
def objectMove(tileMap, direction, selectedLog):
        bridgeMap = []
        
        logStart = findLogs(logMap)[selectedLog][0]
        logY = findLogs(logMap)[selectedLog][1]
        logEnd = findLogs(logMap)[selectedLog][2]
        #logStart = searchLogs(logMap)[selectedLog][0]
        #logEnd = searchLogs(logMap)[selectedLog][2]
        print "\nLOGMAP:", logMap, "\n"        
        
        print logStart
        print logEnd
        print range(logStart, logEnd)
        if direction == "return":
                #for line in range(logStart, logEnd):
                logBuffer = logMap[logY][logStart:logEnd].pop()
                print "logBuffer:", logBuffer
                bridgeMap.append(logBuffer)
                logMap[logY][logStart:logEnd+1].append(logBuffer)
                logMap[logY][logStart:logEnd+1].append(["0"] * len(logBuffer))
                print "mappy:", logMap[logY][logStart:logEnd+1]


        #tileMap[9] = 0
        #tileMap[9][2:] = bridgeMap
        #bridgeMap = 
        print "\n\n", list(bridgeMap), "...bridgeMap\n", len(bridgeMap)
        #tileMap.pop(range(findLogs(selectedLog)[i][0], findLogs(selectedLog)[i][1]))
       
        #xCoord = findLogs(tileMap)[0][0]
	#print xCoord
	#yCoord = findLogs(tileMap)[0][1]
	#print yCoord
	#xEnd = findLogs(tileMap)[0][2]
	#print xEnd
	
	if direction == 'right':
                selectedLog+=1
	        #tileMap.insert(xCoord+1, tileMap.pop(xCoord))

	if direction == 'left':
                selectedLog+=1
                #tileMap.insert(yCoord+1, tileMap.pop(yCoord))

def waitToExit():
	#exitIn = raw_input("\n(press enter to quit)\n")
	pygame.quit()
	
def main(yes):
        mapInit()
	while True:
                #mapInit()
		tileMapPrint(backgroundMap)
		tileMapPrint(logMap)
                #tileMapPrint(bridgeMap)

                #logMapPrint()
		
                getInput()
		print tileMap
		print yes*10

#main("y")

pygame.font.quit()

