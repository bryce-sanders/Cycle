import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Player(Actor):
    """
    A player on a motorcycle with a long energy trail.
    
    The responsibility of Player is to move itself.

    Attributes:
        _trail : A list that holds each section of the player's energy trail.
        _prepar_trail() : Prepares the Player's cycle and each segment of their trail. 
    """
    def __init__(self):
        super().__init__()
        self._trail = []
        self.trail_extension = 0
        self._prepare_trail()

    def get_trail(self):
        return self._trail

    def move_next(self):
        # move all segments
        for segment in self._trail:
            segment.move_next()
        # update velocities
        for i in range(len(self._trail) - 1, 0, -1):
            trailing = self._trail[i]
            previous = self._trail[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._trail[0]

    def turn_head(self, velocity):
        self._trail[0].set_velocity(velocity)
    
    def _prepare_trail(self):
        pass