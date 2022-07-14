from asyncio import constants
from game.scripting.action import Action
from constants import *
from game.shared.color import Color
import pyray


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        pads = [cast.get_first_actor("pad1"), cast.get_first_actor("pad2"), cast.get_first_actor("pad3"), cast.get_first_actor("pad4")]

        self._video_service.clear_buffer()
        for pad in pads:
            self._video_service.draw_pad(pad)
        self._video_service.flush_buffer()
        
