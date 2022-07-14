import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        players = [cast.get_first_actor("player1"), cast.get_first_actor("player2")]
        heads = []
        segments_list = []
        for player in players:
            head = player.get_segments()[0]
            segments = player.get_segments()[1:]
            heads.append(head)
            segments_list.append(segments)
        for segment in segments_list[1]:
            if heads[0].get_position().equals(segment.get_position()):
                self._is_game_over = True
        for segment in segments_list[0]:
            if heads[1].get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            players = [cast.get_first_actor("player1"), cast.get_first_actor("player2")]
            for player in players:
                segments = player.get_segments()

                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)

                message = Actor()
                message.set_text("Game Over!")
                message.set_position(position)
                cast.add_actor("messages", message)

                for segment in segments:
                    segment.set_color(constants.WHITE)