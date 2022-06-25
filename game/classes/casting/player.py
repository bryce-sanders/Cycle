# Import the necessary classes.
from classes.casting.actor import Actor


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
        """
        Progress each segment of the trail.
        """
        # Move all segments.
        for segment in self._trail:
            segment.move_next()
        # Update velocities.
        for i in range(len(self._trail) - 1, 0, -1):
            trailing = self._trail[i]
            previous = self._trail[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def grow_trail(self, number_of_segments):
        pass

    def get_cycle(self):
        return self._trail[0]

    def turn_cycle(self, velocity):
        """
        Change the velocity of the Player.
        """
        self._trail[0].set_velocity(velocity)
    
    def _prepare_trail(self):
        pass