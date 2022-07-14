from constants import *
from game.casting.actor import Actor
from game.casting.rectangle import Rectangle
from game.shared.point import Point
import pyray


class Pad(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, position, size, color):
        self._x = position.get_x()
        self._y = position.get_y()
        self._original_color = color
        super().__init__()
        self.set_color(self._original_color)
        self.set_size(size)
        self.set_position(position)
        self._width = size.get_x()
        self._height = size.get_y()
        self._on_x = False
        self._on_y = False

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_width(self):
        return self._width
    def get_height(self):
        return self._height
    def get_end_x(self):
        return self._x + self._width
    def get_end_y(self):
        return self._y + self._height
    def get_square(self):
        
        rectangle = pyray.Rectangle(self._x, self._y, self._width, self._height)
        pyray.draw_rectangle(self._x, self._y, self._width, self._height, self.get_color().to_tuple())
        pyray.draw_rectangle_lines_ex(rectangle, 8.0, pyray.BLACK)

        
    
    def light_up(self):
        self.set_color(WHITE)
    
    def return_color(self):
        self.set_color(self._original_color)
    
    def _check_mouse_on_pad(self, mouse_x, mouse_y):
        shape_position = self.get_position()
        shape_size = self.get_size()
        end_position = shape_position.add(shape_size)
        end_position_x = end_position.get_x()
        end_position_y = end_position.get_y()
        if ((self._x <= mouse_x) and (mouse_x <= end_position_x)):
            self._on_x = True
        if ((self._y <= mouse_y) and (mouse_y <= end_position_y)):
            self._on_y = True
            
    def mouse_on_pad(self, mouse_x, mouse_y):
        self._check_mouse_on_pad(mouse_x, mouse_y)
        if ((self._on_x == True) and (self._on_y == True)):
            return True
