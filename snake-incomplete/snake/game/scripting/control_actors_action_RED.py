import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService


class ControlActorsActionRed(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service: KeyboardService):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = constants.RIGHT


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('j') and self._direction != constants.RIGHT :
            self._direction = constants.LEFT
        
        # right
        if self._keyboard_service.is_key_down('l') and self._direction != constants.LEFT  :
            self._direction = constants.RIGHT
        
        # up
        if self._keyboard_service.is_key_down('i') and self._direction != constants.DOWN:
            self._direction = constants.UP
        
        # down
        if self._keyboard_service.is_key_down('k') and self._direction != constants.UP:
            self._direction = constants.DOWN
        
        red_snake = cast.get_first_actor("snake_red")
        red_snake.turn_head(self._direction)