import math


class GameEvents(object):
    pacman_is_moving = []
    pacman_stops_moving = []


class GameController(object):
    TIMES_PER_SECOND = 3

    def __init__(self, initial_board, tick_func, utils, fps):
        self.old_state = None
        self.current_state = initial_board
        self.tick = tick_func
        self.move_utils = utils
        self.fps = fps
        self.frames_count = 0
        self.max_frames = math.floor(self.fps/self.TIMES_PER_SECOND)
        self.direction = None
        self.events = GameEvents()
        self.pacman_moves = False

    def update(self):
        if self.frames_count == self.max_frames - 1:
            self.old_state = self.current_state
            self.current_state = self.tick(self.old_state, self.direction)
            if not self.pacman_moves and self.move_utils.pacman_moved(self.old_state, self.current_state):
                self.pacman_moves = True

        if self.pacman_moves:
            for ev in self.events.pacman_is_moving:
                ev()

        self.frames_count = (self.frames_count + 1) % self.max_frames
