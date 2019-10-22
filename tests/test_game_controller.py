import unittest
from unittest.mock import Mock
from pacman.engine.game_controller import GameController
from pacman.model.pacman import Direction


class TestGameController(unittest.TestCase):
    def setUp(self):
        self.board = Mock()
        self.fps = 30
        self.tick = Mock()
        self.utils = Mock()
        self.controller = GameController(self.board, self.tick, self.utils, self.fps)

    def test_tick_function_is_called_thrice_per_second(self):
        self.run_one_second_of_updates()
        self.assertEqual(self.tick.call_count, 3)

    def test_no_direction_is_passed_to_tick_by_default(self):
        self.run_one_second_of_updates()
        self.assertIsNone(self.tick.call_args[0][1])

    def test_last_passed_direction_is_used_for_tick(self):
        self.controller.direction = Direction.LEFT
        self.controller.direction = Direction.RIGHT
        self.controller.direction = Direction.LEFT
        self.controller.direction = Direction.UP

        self.run_one_second_of_updates()

        self.assertEqual(Direction.UP, self.tick.call_args[0][1])

    def test_pacman_is_moving_event_is_fired(self):
        self.utils.pacman_moved = Mock(return_value=True)
        self.controller.events.pacman_is_moving.append(Mock())
        self.run_one_second_of_updates()

        self.controller.events.pacman_is_moving[0].assert_called()

    def run_one_second_of_updates(self):
        for _ in range(self.fps):
            self.controller.update()
