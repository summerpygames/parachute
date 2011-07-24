import pygame
import sys
import os

import mainMenu


#I'm not too sure what all this crap does, but apparently its important :P
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Mind the Gap')

mainMenu.runMenu(screen)
