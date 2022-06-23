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
        self._handle_trail_collision(cast)
        self._handle_game_over(cast)
    
    def _handle_trail_collision(self, cast):
        """Sets the game over flag if a player collides with one a trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("players")
        player2 = cast.get_second_actor("players")

        cycle1 = player1.get_trail()[0]
        cycle2 = player2.get_trail()[0]
        trail1 = player1.get_trail()[1:]
        trail2 = player2.get_trail()[1:]
        
        for segment in trail1:
            if cycle2.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for segment in trail2:
            if cycle1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            players = cast.get_actors("players")
            for player in players:
                trail = player.get_trail()

                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)

                message = Actor()
                message.set_text("Game Over!")
                message.set_position(position)
                cast.add_actor("messages", message)

                for segment in trail:
                    segment.set_color(constants.WHITE)
