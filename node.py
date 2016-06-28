import pygame
class node():
    nodeid=0
    def __init__(self,id):
        self.nodeid=id
        self.outs=[]
        self.ins=[]
        self.x=0
        self.y=0
        self.size=10

    def addout(self,nodeid):
        self.outs.append(nodeid)
    def addin(self,nodeid):
        self.ins.append(nodeid)
    def setpoint(self,x,y):
        self.x=x
        self.y=y
    def drawcircle(self,screen,maincolor,size):
        position = self.x, self.y
        radius = size
        width = int(size/5)

        myfont = pygame.font.SysFont("simsunnsimsun", int(size*1.5))
        txtImage = myfont.render(" "+str(self.nodeid), True, maincolor)

        screen.blit(txtImage, (position[0], position[1]+int(size/2)))
        # pygame.draw.rect(self.screen, color, (200, 300, 100, 200), width)
        pygame.draw.circle(screen, maincolor, position, radius, width)