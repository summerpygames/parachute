#! /usr/bin/env python
"""Skeleton project file mainloop for new OLPCGames users"""
import olpcgames, pygame, logging 
from olpcgames import pausescreen

log = logging.getLogger( 'HelloPygame run' )
log.setLevel( logging.DEBUG )

def main():
    """The mainloop which is specified in the activity.py file
    
    "main" is the assumed function name
    """
    size = (800,600)
    if olpcgames.ACTIVITY:
        size = olpcgames.ACTIVITY.game_size
    screen = pygame.display.set_mode(size)
    
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill( (0,0,128))
        milliseconds = clock.tick(15) # maximum number of frames per second
        
        # Event-management loop with support for pausing after X seconds (20 here)
        events = pausescreen.get_events()
        # Now the main event-processing loop
        if events:
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    log.debug("game keydown: %s", event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    log.debug("game mousedown: %s", event)
            pygame.display.flip()

if __name__ == "__main__":
    logging.basicConfig()
    main()
