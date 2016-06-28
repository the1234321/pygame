import pygame
import sys
from pygame.locals import *
from network import network
from node import node
import random

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
                if event.type == KEYDOWN:
                    #空格重新随机布局
                    if event.key==K_SPACE:
                        self.randomit()
                    elif event.key == K_p:
                        self.addpoint()
                    elif event.key == K_l:
                        self.addlink()
                pygame.display.update()

    def refresh_circle(self):
        self.screen.fill(self.backcolor)
        self.n1.drawnet(self.screen, self.maincolor)
        self.n1.drawline(self.screen, self.maincolor)

    def randomit(self):
        self.n1.setpoints(self.x, self.y)
        self.refresh_circle()

    def addpoint(self):
        nodeid=self.n1.nodenum+2
        self.n1.addnode(nodeid)
        ranx = random.randint(25, self.x - 25)
        rany = random.randint(25, self.y - 25)
        self.n1.nodes[nodeid].setpoint(ranx, rany)
        self.refresh_circle()

    def addlink(self):
        self.n1.addlink(random.randint(1,self.n1.nodenum),random.randint(1,self.n1.nodenum))
        self.refresh_circle()