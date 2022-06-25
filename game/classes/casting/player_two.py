import constants
from classes.casting.actor import Actor
from classes.casting.player import Player
from classes.shared.point import Point


class PlayerTwo(Player):
    """
    A player on a motorcycle with a long energy trail.
    
    The responsibility of Player is to move itself.

    """
    def __init__(self):
        super().__init__()
    
    def _prepare_trail(self):
        """
        Prepares the initial trail of the player in that players color.
        """
        x = int(90)
        y = int(450)

        for i in range(constants.TRAIL_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            color = constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._trail.append(segment)
    
    def grow_trail(self, number_of_segments, color):
        """
        Extend the players trail each time that they move.
        """
        for i in range(number_of_segments):
            trail = self._trail[-1]
            velocity = trail.get_velocity()
            offset = velocity.reverse()
            position = trail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._trail.append(segment)