import constants
from game.casting.actor import Actor
from game.casting.player import Player
from game.shared.point import Point


class PlayerOne(Player):
    """
    A player on a motorcycle with a long energy trail.
    
    The responsibility of Player is to move itself.

    """
    def __init__(self):
        super().__init__()
    
    def _prepare_trail(self):
        x = int(90)
        y = int(150)

        for i in range(constants.TRAIL_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            color = constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._trail.append(segment)
    
    def grow_tail(self, number_of_segments, color):
        for i in range(number_of_segments):
            tail = self._trail[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._trail.append(segment)
        