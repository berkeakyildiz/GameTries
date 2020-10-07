import pygame
from pygame.locals import *
from random import randint
import os, sys

pygame.init()

ARRAY_SIZE = 50

DIRECTIONS = {
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
    "UP": (0, 1),
    "DOWN": (0, -1),
}

snake, fruit = None, None
curPoint = None

def init():
    global snake
    global curPoint
    curPoint = 0
    snake = [(0, 2), (0, 1), (0, 0)]

    place_fruit((ARRAY_SIZE // 2, ARRAY_SIZE // 2))


def place_fruit(coord=None):
    global fruit
    if coord:
        fruit = coord
        return

    while True:
        x = randint(0, ARRAY_SIZE - 1)
        y = randint(0, ARRAY_SIZE - 1)
        if (x, y) not in snake:
            fruit = x, y
            return


def addPoints(point):
    global curPoint
    curPoint += 1
    print("current point: " + str(curPoint))

def step(direction):
    old_head = snake[0]
    movement = DIRECTIONS[direction]
    new_head = (old_head[0] + movement[0], old_head[1] + movement[1])

    if (
            new_head[0] < 0 or
            new_head[0] >= ARRAY_SIZE or
            new_head[1] < 0 or
            new_head[1] >= ARRAY_SIZE or
            new_head in snake
    ):
        return True

    if new_head == fruit:
        place_fruit()
        addPoints(1)
    else:
        tail = snake[-1]
        del snake[-1]

    snake.insert(0, new_head)
    return False


def print_field():
    os.system('clear')
    print('=' * (ARRAY_SIZE + 2))
    for y in range(ARRAY_SIZE - 1, -1, -1):
        print('|', end='')
        for x in range(ARRAY_SIZE):
            out = ' '
            if (x, y) in snake:
                out = 'X'
            elif (x, y) == fruit:
                out = 'O'
            print(out, end='')
        print('|')
    print('=' * (ARRAY_SIZE + 2))


def test():
    global fruit
    init()
    assert step('UP')

    assert snake == [(0, 3), (0, 2), (0, 1)]

    fruit = (0, 4)
    assert step('UP')

    assert snake == [(0, 4), (0, 3), (0, 2), (0, 1)]
    assert fruit != (0, 4)

    assert not step('DOWN'), 'Kdyz nacouvam do sebe, umru!'


DIRS = ['UP', 'RIGHT', 'DOWN', 'LEFT']


def run():
    init()

    direction = 0

    pygame.init()
    s = pygame.display.set_mode((ARRAY_SIZE * 10, ARRAY_SIZE * 10))
    pygame.display.set_caption('Snake')
    appleimage = pygame.Surface((10, 10))
    appleimage.fill((0, 255, 0))
    img = pygame.Surface((10, 10))
    img.fill((255, 0, 0))
    clock = pygame.time.Clock()

    pygame.time.set_timer(1, 100)
    game_over = False



    while True:
        e = pygame.event.wait()
        if e.type == QUIT:
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                direction = 0
                print("UP")
            elif e.key == pygame.K_DOWN:
                direction = 2
                print("DOWN")
            elif e.key == pygame.K_RIGHT:
                direction = 1
                print("RIGHT")
            elif e.key == pygame.K_LEFT:
                direction = 3
                print("LEFT")
        if step(DIRS[direction]):
            #print("Your Score: " + str(curPoint))
            game_over = True
            #pygame.quit()
            #sys.exit(1)
        font = None
        if game_over:
            pygame.font.init()
            print("cyka")
            WHITE = (0, 0, 0)
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over", True, WHITE)
            text_rect = text.get_rect()
            text_x = s.get_width() / 2 - text_rect.width / 2
            text_y = s.get_height() / 2 - text_rect.height / 2
            s.blit(text, [text_x, text_y])
            #pygame.quit()
            #sys.exit(1)
        s.fill((255, 255, 255))
        for bit in snake:
            s.blit(img, (bit[0] * 10, (ARRAY_SIZE - bit[1] - 1) * 10))
        s.blit(appleimage, (fruit[0] * 10, (ARRAY_SIZE - fruit[1] - 1) * 10))
        pygame.display.flip()


run()
