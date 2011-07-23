def runMenu(screen):
    import os
    import pygame
    import sys
    pygame.init()

    #Declare a variable to determine what part of the application is running and set it to the main menu value: 1
    runningLoop = 1

    #load tha backgrounds
    mainBackground = pygame.image.load(os.path.join("data", "mainMenu.png")).convert()
    mainBackgroundRect = mainBackground.get_rect()
    screen.blit(mainBackground, mainBackgroundRect)

    #declare the variables to handle flipping through the menu
    menuCounter = 1
    fontSelect1 = 255, 255, 255
    fontSelect2 = 255, 100, 225
    fontSelect3 = 255, 100, 225
    fontSelect4 = 255, 100, 255
    fontSelect5 = 255, 100, 255
    fontSelect6 = 255, 100, 255

    #Four chucks of code setting up the options for the text options on the menu
    font = pygame.font.Font(None, 64)

    text1 = font.render('Start Adventure!', True, (0, 0, 0), (fontSelect1))

    textRect1 = text1.get_rect()

    textRect1.centerx = 600
    textRect1.centery = 100

    screen.blit(text1, textRect1)

    text2 = font.render('Options', True, (0, 0, 0), (fontSelect2))

    textRect2 = text2.get_rect()

    textRect2.centerx = 600
    textRect2.centery = 175

    screen.blit(text2, textRect2)

    text3 = font.render('Credits', True, (0, 0, 0), (fontSelect3))

    textRect3 = text3.get_rect()

    textRect3.centerx = 600
    textRect3.centery = 250

    screen.blit(text3, textRect3)

    text4 = font.render('About', True, (0, 0, 0), (fontSelect4))

    textRect4 = text4.get_rect()

    textRect4.centerx = 600
    textRect4.centery = 325

    screen.blit(text4, textRect4)

    text5 = font.render('Help', True, (0, 0, 0), (fontSelect5))

    textRect5 = text5.get_rect()

    textRect5.centerx = 600
    textRect5.centery = 400

    screen.blit(text5, textRect5)

    text6 = font.render('Exit', True, (0, 0, 0), (fontSelect6))

    textRect6 = text6.get_rect()

    textRect6.centerx = 600
    textRect6.centery = 475

    screen.blit(text6, textRect6)

    pygame.display.update()

    #Function to handle checking the menuCounter and redrawing the higlighted menu options accordingly
    def moveMenuFocus(menuCounter):
        if menuCounter == 1:
            fontSelect1 = 255, 255, 255
            fontSelect2 = 255, 100, 255
            fontSelect3 = 255, 100, 255
            fontSelect4 = 255, 100, 255
            fontSelect5 = 255, 100, 255
            fontSelect6 = 255, 100, 255
        if menuCounter == 2:
            fontSelect1 = 255, 100, 255
            fontSelect2 = 255, 255, 255
            fontSelect3 = 255, 100, 255
            fontSelect4 = 255, 100, 255
            fontSelect5 = 255, 100, 255
            fontSelect6 = 255, 100, 255
        if menuCounter == 3:
            fontSelect1 = 255, 100, 255
            fontSelect2 = 255, 100, 255
            fontSelect3 = 255, 255, 255
            fontSelect4 = 255, 100, 255
            fontSelect5 = 255, 100, 255
            fontSelect6 = 255, 100, 255
        if menuCounter == 4:
            fontSelect1 = 255, 100, 255
            fontSelect2 = 255, 100, 255
            fontSelect3 = 255, 100, 255
            fontSelect4 = 255, 255, 255
            fontSelect5 = 255, 100, 255
            fontSelect6 = 255, 100, 255
        if menuCounter == 5:
            fontSelect1 = 255, 100, 255
            fontSelect2 = 255, 100, 255
            fontSelect3 = 255, 100, 255
            fontSelect4 = 255, 100, 255
            fontSelect5 = 255, 255, 255
            fontSelect6 = 255, 100, 255
        if menuCounter == 6:
            fontSelect1 = 255, 100, 255
            fontSelect2 = 255, 100, 255
            fontSelect3 = 255, 100, 255
            fontSelect4 = 255, 100, 255
            fontSelect5 = 255, 100, 255
            fontSelect6 = 255, 255, 255
            
        text1 = font.render('Start Adventure!', True, (0, 0, 0), (fontSelect1))
        text2 = font.render('Options', True, (0, 0, 0), (fontSelect2))
        text3 = font.render('Credits', True, (0, 0, 0), (fontSelect3))
        text4 = font.render('About', True, (0, 0, 0), (fontSelect4))
        text5 = font.render('Help', True, (0, 0, 0), (fontSelect5))
        text6 = font.render('Exit', True, (0, 0, 0), (fontSelect6))

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
            print "play"
        elif menuCounter == 2:
            print "two"
        elif menuCounter == 3:
            print "three"
        elif menuCounter == 4:
            print "four"
        elif menuCounter == 5:
            print "five"
        elif menuCounter == 6:
            pygame.QUIT
            
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
