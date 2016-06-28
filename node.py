import pygame
class node():
    nodeid=0
    def __init__(self,id):
        self.nodeid=id
        self.outs=[]
        self.ins=[]
        self.x=0
        self.y=0

    def addout(self,nodeid):
        self.outs.append(nodeid)
    def addin(self,nodeid):
        self.ins.append(nodeid)
    def setpoint(self,x,y):
        self.x=x
        self.y=y
    def drawcircle(self,screen,maincolor):
        position = self.x, self.y
        radius = 20
        width = 2

        myfont = pygame.font.SysFont("simsunnsimsun", 15)
        txtImage = myfont.render("点"+str(self.nodeid), True, maincolor)

        screen.blit(txtImage, (position[0] - 11, position[1] - 9))
        # pygame.draw.rect(self.screen, color, (200, 300, 100, 200), width)
        pygame.draw.circle(screen, maincolor, position, radius, width)