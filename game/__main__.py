# Import necessary classes.
from classes.casting.cast import Cast
from classes.casting.player_one import PlayerOne
from classes.casting.player_two import PlayerTwo
from classes.scripting.script import Script
from classes.scripting.control_actor_one import ControlActorOne
from classes.scripting.control_actor_two import ControlActorTwo
from classes.scripting.move_actors_action import MoveActorsAction
from classes.scripting.handle_collisions_action import HandleCollisionsAction
from classes.scripting.draw_actors_action import DrawActorsAction
from classes.directing.director import Director
from classes.services.keyboard_service import KeyboardService
from classes.services.video_service import VideoService


def main():
    """
    Creates the Cast and Script and passes them to the Director.
    """
    
    # Create the Cast and add both players to it.
    cast = Cast()
    cast.add_actor("players", PlayerOne())
    cast.add_actor("players", PlayerTwo())
   
    # Create the Script.
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorOne(keyboard_service))
    script.add_action("input", ControlActorTwo(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    # Creat the Director and give them the Cast and Script.
    director = Director(video_service)
    director.start_game(cast, script)


# Run the Main() function.
if __name__ == "__main__":
    main()
