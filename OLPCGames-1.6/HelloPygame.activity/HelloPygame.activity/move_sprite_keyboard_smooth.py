# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import olpcgames, pygame, logging 
from olpcgames import pausescreen, textsprite
from gettext import gettext as _

log = logging.getLogger( 'HelloPygame run' )
log.setLevel( logging.DEBUG )


# -- Attributes
# Set speed vector
class Player(textsprite.TextSprite):
    """docstring for somehting"""
    def __init__(self, text=None, family=None, size=None, bold=False,
                 italic=False, color=None, background=None):

        super(Player, self).__init__(text=None, family=None, size=None,
                                        bold=False, italic=False, color=None,
                                        background=None)
        self.change_y = 0
        self.change_x = 0


            
    # Change the speed of the player
    def changespeed(self, x, y):
        self.change_x+=x
        self.change_y+=y
        
    # Find a new position for the player
    def update(self):
        self.rect.top += self.change_y
        self.rect.left += self.change_x

def main():
    """The mainlook which is specified in the activity.py file
    
    "main" is the assumed function name"""

    
    size = (800,600)
    if olpcgames.ACTIVITY:
        size = olpcgames.ACTIVITY.game_size
    screen = pygame.display.set_mode(size)
    # Create an 800x600 sized screen
    
    text = Player(
        text = _( "Hello Children of the World" ),
        color = (255,255,255),
        size = 20,
    )
    group = pygame.sprite.RenderUpdates()
    group.add( text )
    
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill( (0,0,128))
        milliseconds = clock.tick(25) # maximum number of frames per second
        
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
                    if event.key == pygame.K_LEFT:
                        text.changespeed(-3,0)
                    if event.key == pygame.K_RIGHT:
                        text.changespeed(3,0)
                    if event.key == pygame.K_UP:
                        text.changespeed(0,-3)
                    if event.key == pygame.K_DOWN:
                        text.changespeed(0,3)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        text.changespeed(3,0)
                    if event.key == pygame.K_RIGHT:
                        text.changespeed(-3,0)
                    if event.key == pygame.K_UP:
                        text.changespeed(0,3)
                    if event.key == pygame.K_DOWN:
                        text.changespeed(0,-3)
        text.update()
        group.draw( screen )
        pygame.display.flip()
        clock.tick(140)

    pygame.quit()

if __name__ == '__main__':
    main()
