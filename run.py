#! /usr/bin/env python
"""Skeleton project file mainloop for new OLPCGames users"""
import os, sys
import pygame, logging
#import olpcgames, pygame, logging 
#from olpcgames import pausescreen

import mainMenu

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




log = logging.getLogger( 'Parachute run' )
log.setLevel( logging.DEBUG )

def main():
    """The mainloop which is specified in the activity.py file
    
    "main" is the assumed function name
    """
    #size = (800,600)
    size = (1200,900)
    #if olpcgames.ACTIVITY:
    #    size = olpcgames.ACTIVITY.game_size
    screen = pygame.display.set_mode(size)
    
    clock = pygame.time.Clock()
    
    pygame.display.set_caption('Mind the Gap')

    running = True
    while running:
        screen.fill( (0,0,128))
        milliseconds = clock.tick(25) # maximum number of frames per second
        
        #calls the main menu function
        mainMenu.runMenu(screen)

        # Event-management loop with support for pausing after X seconds (20 here)
        events = pausescreen.get_events()
        # Now the main event-processing loop
        if events:
            for event in events:
                log.debug( "Event: %s", event )
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.flip()

if __name__ == "__main__":
    logging.basicConfig()
    main()
