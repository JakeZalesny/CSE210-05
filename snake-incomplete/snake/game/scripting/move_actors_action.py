from game.scripting.action import Action
import pyray

class MoveActorsAction(Action) :
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, cast, script):

        actors = cast.get_all_actors()
        for i in actors:
            i.move_next()

        # score = cast.get_first_actor("scores")
        # food = cast.get_first_actor("foods")
        # snake = cast.get_first_actor("snakes")
        # segments = snake.get_segments()
        # messages = cast.get_actors("messages")

        

    
    


# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor