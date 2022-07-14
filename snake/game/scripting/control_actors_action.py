from tkinter import LEFT
from constants import *
from game.scripting.action import Action
from game.shared.point import Point
from constants import *
import pyray

class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, mouse_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._mouse_service = mouse_service
        


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        pads = [cast.get_first_actor("pad1"), cast.get_first_actor("pad2"), cast.get_first_actor("pad3"), cast.get_first_actor("pad4")]
        for pad in pads:
            mouse_coordinate = self._mouse_service.get_coordinates()
            x = mouse_coordinate.get_x()
            y = mouse_coordinate.get_y()
            pad_x = pad.get_x()
            pad_y = pad.get_y()
            end_x = pad.get_end_x()
            end_y = pad.get_end_y()
            if (pad_x <= x and x <= end_x) and (pad_y <= y and y <= end_y):
                if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT):
                    pad.light_up()
                elif pyray.is_mouse_button_released(pyray.MOUSE_BUTTON_LEFT):
                    pad.return_color()
