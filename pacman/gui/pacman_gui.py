import pygame
import os
from pacman import board_reader
from pacman.pacman import Direction
from pacman.engine import game

SPRITE_SIZE = 16
FPS = 3
GAME_KEYS = {
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT
}

game_board = board_reader.read('pacman/resources/board.txt')
board_width = len(game_board[0])
board_height = len(game_board)

current_direction = None

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
    for j, row in enumerate(game_board):
        for i, item in enumerate(list(row)):
            if item == '#':
                screen.blit(wall, (i * SPRITE_SIZE, j * SPRITE_SIZE))
            elif item == '.':
                screen.blit(dot, (i * SPRITE_SIZE, j * SPRITE_SIZE))
            elif item in ['>', '<', '^', 'v']:
                angle = 0
                if item == '>':
                    angle = 180
                elif item == 'v':
                    angle = 90
                elif item == '^':
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


while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            current_direction = _handle_input(event)

    game_board = game.tick(game_board, current_direction)
    __render_board()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
