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


	#declare the variables to handle flipping through the menu
	menuCounter = 1
	fontSelect1 = True
	fontSelect2 = False
	fontSelect3 = False
	fontSelect4 = False
	fontSelect5 = False
	fontSelect6 = False

	#Six chucks of code setting up the options for the text options on the menu
	font = pygame.font.Font(None, 64)

	text1 = font.render('Start Adventure!', True, (0, 0, 0), (255, 255, 255))
	textRect1 = text1.get_rect()

	textRect1.centerx = 600
	textRect1.centery = 100

	screen.blit(text1, textRect1)

	text2 = font.render('Options', True, (0, 0, 0))
	textRect2 = text2.get_rect()

	textRect2.centerx = 600
	textRect2.centery = 175

	screen.blit(text2, textRect2)

	text3 = font.render('Credits', True, (0, 0, 0))
	textRect3 = text3.get_rect()

	textRect3.centerx = 600
	textRect3.centery = 250

	screen.blit(text3, textRect3)

	text4 = font.render('About', True, (0, 0, 0))
	textRect4 = text4.get_rect()

	textRect4.centerx = 600
	textRect4.centery = 325

	screen.blit(text4, textRect4)

	text5 = font.render('Help', True, (0, 0, 0))
	textRect5 = text5.get_rect()

	textRect5.centerx = 600
	textRect5.centery = 400

	screen.blit(text5, textRect5)

	text6 = font.render('Exit', True, (0, 0, 0))
	textRect6 = text6.get_rect()

	textRect6.centerx = 600
	textRect6.centery = 475

	screen.blit(text6, textRect6)

	pygame.display.update()

	#Function to handle checking the menuCounter and redrawing the higlighted menu options accordingly
	def moveMenuFocus(menuCounter):
		#init everthing to a False bool

		fontSelect1 = False
		fontSelect2 = False
		fontSelect3 = False
 		fontSelect4 = False
		fontSelect5 = False
		fontSelect6 = False		

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
		if menuCounter == 6:
			fontSelect6 = True

		if fontSelect1 == True:
			text1 = font.render('Start Adventure!', True, (0, 0, 0), (255, 255, 255))
		else:
			text1 = font.render('Start Adventure!', True, (0, 0, 0))
		if fontSelect2 == True:
			text2 = font.render('Options', True, (0, 0, 0), (255, 255, 255))
		else:
			text2 = font.render('Options', True, (0, 0, 0))
		if fontSelect3 == True:
			text3 = font.render('Credits', True, (0, 0, 0), (255, 255, 255))
		else:
			text3 = font.render('Credits', True, (0, 0, 0))
		if fontSelect4 == True:
			text4 = font.render('About', True, (0, 0, 0), (255, 255, 255))
		else:
			text4 = font.render('About', True, (0, 0, 0))
		if fontSelect5 == True:
			text5 = font.render('Help', True, (0, 0, 0), (255, 255, 255))
		else:
			text5 = font.render('Help', True, (0, 0, 0))
		if fontSelect6 == True:
			text6 = font.render('Exit', True, (0, 0, 0), (255, 255, 255))
		else:
			text6 = font.render('Exit', True, (0, 0, 0))

		screen.blit(mainBackground, mainBackgroundRect)
		screen.blit(text1, textRect1)
		screen.blit(text2, textRect2)
		screen.blit(text3, textRect3)
		screen.blit(text4, textRect4)
		screen.blit(text5, textRect5)
		screen.blit(text6, textRect6)

		pygame.display.update()
	#Runs when enter is pressed, checks which menu Item is chosen and responds by running the right code
	def selectMenuItem(menuCounter):
		
		if menuCounter == 1:
			#calls the game 
			#os.system("python tileMapper.py")
			print "map lauch\n"
			tileMapper.main("y")
			
		elif menuCounter == 2:
			print "two"
		elif menuCounter == 3:
			#load the credits page and refresh the screen to display it
			screen.blit(creditsPage, creditsPageRect)
			pygame.display.update()
		elif menuCounter == 4:
			print "nothing"
		elif menuCounter == 5:
			#load the about and refresh the screen to display it
			screen.blit(helpMenu, helpMenuRect)
			pygame.display.update()
		elif menuCounter == 6:
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
							menuCounter = 6
						moveMenuFocus(menuCounter)
					elif event.key == pygame.K_DOWN:
						menuCounter += 1
						if menuCounter >= 7:
							menuCounter = 1
						moveMenuFocus(menuCounter)
					elif event.key == pygame.K_RETURN:
						selectMenuItem(menuCounter)
	#pygame.font.quit()

