from olpcgames import activity
from gettext import gettext as _

class Activity(activity.PygameActivity):
    """Your Sugar activity"""
    
    game_name = 'run'
    game_title = _('Hello Pygame')
    game_size = None
