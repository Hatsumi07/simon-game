from game.scripting.action import Action


class ChangePadColor(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        pads = [cast.get_first_actor("pad1"), cast.get_first_actor("pad2"), cast.get_first_actor("pad3"), cast.get_first_actor("pad4")]
        for pad in pads:
            actor.move_next()
            