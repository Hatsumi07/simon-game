from game.shared.color import Color
from game.shared.point import Point
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
PAD_WIDTH = 200
PAD_HEIGHT = 200
PAD_MARGEN = 5
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 15
FONT_SIZE = 15
CAPTION = "Snake"
SNAKE_LENGTH = 4
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

PAD_SIZE = Point(PAD_WIDTH, PAD_HEIGHT)

RED_PAD_POSITION = Point(int(MAX_X / 2 - PAD_MARGEN - PAD_WIDTH), int(MAX_Y / 2 - PAD_MARGEN - PAD_HEIGHT))

BLUE_PAD_POSITION = Point(int(MAX_X / 2 - PAD_MARGEN - PAD_WIDTH), int(MAX_Y / 2 + PAD_MARGEN))

GREEN_PAD_POSITION = Point(int(MAX_X / 2 + PAD_MARGEN), int(MAX_Y / 2 + PAD_MARGEN))

YELLOW_PAD_POSITION = Point(int(MAX_X / 2 + PAD_MARGEN), int(MAX_Y / 2 - PAD_MARGEN - PAD_HEIGHT))