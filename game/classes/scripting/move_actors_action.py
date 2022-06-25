# Import necessary classes and variables.
import constants
from classes.scripting.action import Action


class MoveActorsAction(Action):
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
        # Move player 1 and grow their trail.
        actor1 = cast.get_first_actor("players")
        actor1.move_next()
        actor1.grow_trail(1, constants.RED)

        # Move player 2 and grow their trail.
        actor2 =cast.get_second_actor("players")
        actor2.move_next()
        actor2.grow_trail(1, constants.GREEN)
