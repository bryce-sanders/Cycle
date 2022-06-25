from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        self._video_service.clear_buffer()
        #call all of the items in the "players" list found in get_actors()
        players = cast.get_actors("players")
        #this loop takes every item returned in the list
        for player in players:
            #updates the trail and gets actors in the "messages" group
            trail = player.get_trail()
            messages = cast.get_actors("messages")
            
            #draw the called items
            self._video_service.draw_actors(trail)
            self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
