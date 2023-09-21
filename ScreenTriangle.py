import pygame

from Vec3Vec4 import Vec3


class ScreenTriangle:
    def __init__(self, v0: Vec3, v1: Vec3, v2: Vec3):
        self.v0, self.v1, self.v2 = v0, v1, v2

    def draw(self, window):
        pygame.draw.line(window, "red", (self.v0.x,
                                         self.v0.y), (self.v1.x, self.v1.y), 1)
        pygame.draw.line(window, "red", (self.v1.x,
                                         self.v1.y), (self.v2.x, self.v2.y), 1)
        pygame.draw.line(window, "red", (self.v2.x,
                                         self.v2.y), (self.v0.x, self.v0.y), 1)
