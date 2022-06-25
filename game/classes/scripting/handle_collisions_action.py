# Import necessary classes.
import constants
from classes.casting.actor import Actor
from classes.scripting.action import Action
from classes.shared.point import Point

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
        """Sets the game over flag if a player collides with opponent's trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # Get players.
        player1 = cast.get_first_actor("players")
        player2 = cast.get_second_actor("players")

        # Establish variables to track each players cycle and trail.
        cycle_1 = player1.get_trail()[0]
        cycle_2 = player2.get_trail()[0]
        trail_1 = player1.get_trail()[1:]
        trail_2 = player2.get_trail()[1:]
        
        # Check if player 2 collided with player 1's trail.
        for segment in trail_1:
            if cycle_2.get_position().equals(segment.get_position()):
                self._is_game_over = True

        # Check if player 1 collided with player 2's trail.
        for segment in trail_2:
            if cycle_1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the players white if the game is over.
        
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

                # Create "Game Over" message.
                message = Actor()
                message.set_text("Game Over!")
                message.set_position(position)
                cast.add_actor("messages", message)

                # Turn players white.
                for segment in trail:
                    segment.set_color(constants.WHITE)
