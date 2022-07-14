from constants import *

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.pad import Pad
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.mouse_service import MouseService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("pad1", Pad(RED_PAD_POSITION, PAD_SIZE, RED))
    cast.add_actor("pad2", Pad(BLUE_PAD_POSITION, PAD_SIZE, BLUE))
    cast.add_actor("pad3", Pad(GREEN_PAD_POSITION, PAD_SIZE, GREEN))
    cast.add_actor("pad4", Pad(YELLOW_PAD_POSITION, PAD_SIZE, YELLOW))

    # start the game

    mouse_service = MouseService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(mouse_service))
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()