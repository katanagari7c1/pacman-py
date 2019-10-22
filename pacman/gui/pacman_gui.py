import pygame
import os
from pacman.utils import board_reader
from pacman.model.pacman import Direction, Pacman
from pacman.model.game_board import build_game_state_from_string_tuple as build_board
from pacman.engine.game_controller import GameController
from pacman.engine.game import tick as game_tick
from pacman.model.items import *

SPRITE_SIZE = 16
FPS = 30
GAME_KEYS = {
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT
}

game_board = build_board(board_reader.read('pacman/resources/board.txt'))
game_controller = GameController(game_board, game_tick, FPS)
board_width = len(game_board[0])
board_height = len(game_board)

pygame.init()
pygame.display.set_caption('Pacman!')
screen = pygame.display.set_mode((board_width * SPRITE_SIZE, board_height * SPRITE_SIZE))
clock = pygame.time.Clock()

pygame.key.set_repeat()  # disable key repeat
finished = False

# Pre-load images
wall = pygame.image.load(os.path.join('pacman', 'resources', 'wall.png'))
pacman = pygame.image.load('pacman/resources/pacman.png')
dot = pygame.image.load('pacman/resources/dot.png')


def __render_board():
    screen.fill((48, 48, 48))
    for j, row in enumerate(game_controller.state):
        for i, item in enumerate(list(row)):
            if isinstance(item, Wall):
                screen.blit(wall, (i * SPRITE_SIZE, j * SPRITE_SIZE))
            elif isinstance(item, Space) and isinstance(item.content, Dot):
                screen.blit(dot, (i * SPRITE_SIZE, j * SPRITE_SIZE))
            elif isinstance(item, Pacman):
                angle = 0
                if item.direction == Direction.LEFT:
                    angle = 180
                elif item.direction == Direction.UP:
                    angle = 90
                elif item.direction == Direction.DOWN:
                    angle = 270

                screen.blit(pygame.transform.rotate(pacman, angle), (i * SPRITE_SIZE, j * SPRITE_SIZE))


def _handle_input(ev):
    if ev.key == GAME_KEYS['up']:
        return Direction.UP
    if ev.key == GAME_KEYS['down']:
        return Direction.DOWN
    if ev.key == GAME_KEYS['left']:
        return Direction.LEFT
    if ev.key == GAME_KEYS['right']:
        return Direction.RIGHT


current_direction = None
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            current_direction = _handle_input(event)

    game_controller.direction = current_direction
    game_controller.update()
    __render_board()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
