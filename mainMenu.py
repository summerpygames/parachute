def runMenu(screen):
	import os
	import pygame
	import sys
	
	import tileMapper #our map printing function. tileMapper.py in .
	pygame.init()

	#Declare a variable to determine what part of the application is running and set it to the main menu value: 1
	runningLoop = 1

	#load the backgrounds
	mainBackground = pygame.image.load(os.path.join("data", "background.png")).convert()#"mainMenu.png")).convert()
	mainBackgroundRect = mainBackground.get_rect()
	screen.blit(mainBackground, mainBackgroundRect)
	
	creditsPage = pygame.image.load(os.path.join("data", "creditsPage.png")).convert()
	creditsPageRect = creditsPage.get_rect()

	helpMenu = pygame.image.load(os.path.join("data", "helpMenu.png")).convert()
	helpMenuRect = helpMenu.get_rect()
	
        levelsMap = pygame.image.load(os.path.join("data", "levelsMap.png")).convert()
	levelsMapRect = helpMenu.get_rect()

	hightlightColor = 0x0cc9ff

	#declare the variables to handle flipping through the menu
	menuCounter = 1
	fontSelect1 = True
	fontSelect2 = False
	fontSelect3 = False
	fontSelect4 = False
	fontSelect5 = False

        #array with all the xy coords for menu items, the higlighting locations of all the things
       	location = [[136, 738], [170, 667], [250, 708], [332, 662], [460, 660], [710, 732], [797, 696], [902, 716], [936, 622], [873, 539], [486, 535], [400, 529], [296, 544], [134, 524], [182, 454], [718, 432], [802, 444], [895, 447], [898, 384], [817, 351], [422, 262], [372, 182], [291, 234], [207, 186], [113, 114]]
        levelSelected = 0


	#set up the  text on the menu using objects, blitted by coords
	font = pygame.font.Font(None, 64)

	text1 = font.render('Start Adventure!', True, (0, 0, 0), (255, 255, 255))
	textRect1 = text1.get_rect()

	textRect1.centerx = 600
	textRect1.centery = 100

	screen.blit(text1, textRect1)

	text2 = font.render('Credits', True, (0, 0, 0))
	textRect2 = text2.get_rect()

	textRect2.centerx = 600
	textRect2.centery = 175

	screen.blit(text2, textRect2)

	text3 = font.render('About', True, (0, 0, 0))
	textRect3 = text3.get_rect()

	textRect3.centerx = 600
	textRect3.centery = 250

	screen.blit(text3, textRect3)

	text4 = font.render('Help', True, (0, 0, 0))
	textRect4 = text4.get_rect()

	textRect4.centerx = 600
	textRect4.centery = 325

	screen.blit(text4, textRect4)

	text5 = font.render('Exit', True, (0, 0, 0))
	textRect5 = text5.get_rect()

	textRect5.centerx = 600
	textRect5.centery = 400

	screen.blit(text5, textRect5)

	pygame.display.update()

	#Function to handle checking the menuCounter and redrawing the higlighted menu options accordingly
	def moveMenuFocus(menuCounter):
		#init all the vars to a False bool

		fontSelect1 = False
		fontSelect2 = False
		fontSelect3 = False
		fontSelect4 = False
		fontSelect5 = False		

		if menuCounter == 1:
			fontSelect1 = True
		if menuCounter == 2:
			fontSelect2 = True
		if menuCounter == 3:
			fontSelect3 = True
		if menuCounter == 4:
			fontSelect4 = True
		if menuCounter == 5:
			fontSelect5 = True

		if fontSelect1 == True:
			text1 = font.render('Start Adventure!', True, (0, 0, 0), (255, 255, 255))
		else:
			text1 = font.render('Start Adventure!', True, (0, 0, 0))
		if fontSelect2 == True:
			text2 = font.render('Credits', True, (0, 0, 0), (255, 255, 255))
		else:
			text2 = font.render('Credits', True, (0, 0, 0))
		if fontSelect3 == True:
			text3 = font.render('About', True, (0, 0, 0), (255, 255, 255))
		else:
			text3 = font.render('About', True, (0, 0, 0))
		if fontSelect4 == True:
			text4 = font.render('Help', True, (0, 0, 0), (255, 255, 255))
		else:
			text4 = font.render('Help', True, (0, 0, 0))
		if fontSelect5 == True:
			text5 = font.render('Exit', True, (0, 0, 0), (255, 255, 255))
		else:
			text5 = font.render('Exit', True, (0, 0, 0))
			
		screen.blit(mainBackground, mainBackgroundRect)
		screen.blit(text1, textRect1)
		screen.blit(text2, textRect2)
		screen.blit(text3, textRect3)
		screen.blit(text4, textRect4)
		screen.blit(text5, textRect5)

		pygame.display.update()

	#Highlights all the levels, one at a time.
	def outlineDot(levelSelected, location):
                screen.blit(levelsMap, levelsMapRect)
                pygame.draw.ellipse(screen, hightlightColor, (((location[levelSelected][0])-30), ((location[levelSelected][1])-30), 60, 60))
                pygame.display.flip()
                #Runs when enter is pressed, checks which menu Item is chosen and responds by running the right code
	def selectMenuItem(menuCounter):
		if menuCounter == 1:
                        screen.blit(levelsMap, levelsMapRect)
                        pygame.draw.ellipse(screen, hightlightColor, (106, 708, 60, 60))
                        pygame.display.flip()
                        ##tileMapper.main("y")
		elif menuCounter == 2:
			#load the credits page and refresh the screen to display it
			screen.blit(creditsPage, creditsPageRect)
			pygame.display.update()
		elif menuCounter == 3:
			print "item 3"
		elif menuCounter == 4:
			#load the about and refresh the screen to display it
			screen.blit(helpMenu, helpMenuRect)
			pygame.display.update()
		elif menuCounter == 5:
			pygame.quit()
	while runningLoop == 1:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                runningLoop = 0
                                sys.exit()
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                        menuCounter -= 1
                                        if menuCounter <= 0:
                                                menuCounter = 5
                                        moveMenuFocus(menuCounter)
                                elif event.key == pygame.K_DOWN:
                                        menuCounter += 1
                                        if menuCounter >= 6:
                                                menuCounter = 1
                                        moveMenuFocus(menuCounter)
                                elif event.key == pygame.K_RETURN:
                                        print "selected menu item"
                                        selectMenuItem(menuCounter)
                                        if menuCounter == 1:
                                                runningLoop = 2
                                        print runningLoop
	while runningLoop == 2:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                runningLoop = 0
                                sys.exit()
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    #calls the game 
                                    #os.system("python tileMapper.py")
                                    print "map lauch\n"
                                    if levelSelected % 5 == 0:
                                            tileMapper.main("desert")
	    			    if levelSelected % 5 == 1:
                                           tileMapper.main("jungle")
        			    if levelSelected % 5 == 2:
				            tileMapper.main("lava")
                                    if levelSelected % 5 == 3:
				            tileMapper.main("tundra")
				    if levelSelected % 5 == 4:
				            tileMapper.main("space")
								
								
                                    print "ran"
                                if event.key == pygame.K_LEFT:
                                    levelSelected -= 1
                                if event.key == pygame.K_RIGHT:
                                    levelSelected += 1
                                if levelSelected < 0:
                                    levelSelected = 24
                                elif levelSelected > 24:
                                    levelSelected = 0
                                else:
                                    pass
                                print levelSelected
                                outlineDot(levelSelected, location)
                                                
	#pygame.font.quit()

