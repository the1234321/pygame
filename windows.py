import pygame
import sys
from pygame.locals import *
from network import network
from node import node

class windows(object):
    def __init__(self, rev1, rev2,n1):
        self.backcolor = 0, 0, 200
        self.maincolor = 255, 255, 255
        pygame.init()
        self.screen = pygame.display.set_mode((rev1, rev2))

        self.x = rev1
        self.y = rev2

        self.n1=n1

        self.screen.fill(self.backcolor)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if pygame.key.get_pressed()[K_SPACE]:
                    self.refresh_circle()

                pygame.display.update()

    def refresh_circle(self):
        self.screen.fill(self.backcolor)
        self.n1.setpoints(self.x, self.y)
        self.n1.drawnet(self.screen, self.maincolor)
        self.n1.drawline(self.screen, self.maincolor)

