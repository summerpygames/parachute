"""
	This file is part of Mind The Gap
	
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import pygame
import sys
import os

import mainMenu


#init the screen at the right size
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Mind the Gap')
#calls the menu function
mainMenu.runMenu(screen)
