def creditsFunction(screen):
    #load tha background
    mainBackground = pygame.image.load(os.path.join("data", "mainMenu.png")).convert()
    mainBackgroundRect = mainBackground.get_rect()
    screen.blit(mainBackground, mainBackgroundRect)

    text1 = font.render('Coders:', True, (0, 0, 0), (255, 255, 255))
    text2 = font.render('William Conroy', True, (0, 0, 0), (255, 255, 255))
    text3 = font.render('Joshua Satterfield', True, (0, 0, 0), (255, 255, 255))
    text4 = font.render('Ryan Becwar', True, (0, 0, 0), (255, 255, 255))
    text5 = font.render('Artists:', True, (0, 0, 0), (255, 255, 255))
    text6 = font.render('Lawton Mizell', True, (0, 0, 0), (255, 255, 255))
    text7 = font.render('Michael Mizell', True, (0, 0, 0), (255, 255, 255))
    text8 = font.render('William Archie', True, (0, 0, 0), (255, 255, 255))
    text9 = font.render('Musician:', True, (0, 0, 0), (255, 255, 255))
    text10 = font.render('Lawton Mizell', True, (0, 0, 0), (255, 255, 255))
    text11 = font.render('Adam Walker', True, (0, 0, 0), (255, 255, 255))
    text12 = font.render('Mentors:', True, (0, 0, 0), (255, 255, 255))
    text13 = font.render('Elizabeth Barndollar', True, (0, 0, 0), (255, 255, 255))
    text14 = font.render('Fred Krenson', True, (0, 0, 0), (255, 255, 255))
    text15 = font.render('Adam Brightwell', True, (0, 0, 0), (255, 255, 255))
    text16 = font.render('Zenko Klapko', True, (0, 0, 0), (255, 255, 255))


    screen.blit(text1, (100, 200))

    screen.blit(text2, textRect2)
