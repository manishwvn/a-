import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* algorithm")

RED = (255, 0, 0)  # closed set nodes
GREEN = (0, 255, 0)  # open set nodes
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)  # initial or unvisited nodes
BLACK = (0, 0, 0)  # obstacles or barriers
PURPLE = (128, 0, 128)  # path nodes
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = list()
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        # to check if a spot in the closed set, represent using RED
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rec(win, self.color,
                        (self.x, self.y, self.width, self.width))

    def update_neighbors(self):
        pass

    def __lt__(self, other):
        return False

# heuristic


def h(p1, p2):
    pass
