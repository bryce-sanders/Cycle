from game.scripting.action import Action
import constants

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
        # actors = cast.get_all_actors()
        # for actor in actors:
        #     actor.move_next()
        #     actor.grow_tail(1)
        
        actor1 = cast.get_first_actor("players")
        actor1.move_next()
        actor1.grow_tail(1, constants.RED)


        actor2 =cast.get_second_actor("players")
        actor2.move_next()
        actor2.grow_tail(1, constants.GREEN)
