from node import node
import pygame
import random
class network(object):
    def __init__(self,nodenum):
        self.nodenum=nodenum
        self.nodes={}
        for i in range(1,nodenum+1):
            self.addnode(i)

    def addnode(self,nodeid):
        self.nodes[nodeid]=node(nodeid)

    def print(self):
        for i in self.nodes:
            print("第"+str(i)+"个"+str(self.nodes[i].nodeid))
            for j in self.nodes[i].ins:
                print(" "+str(i)+"<<"+str(j))
            for k in self.nodes[i].outs:
                print(" "+str(i)+">>" + str(k))

    def addlink(self,nodefrom,nodeto):
        self.nodes[nodefrom].addout(nodeto)
        self.nodes[nodeto].addin(nodefrom)

    def setpoints(self,rev1,rev2):
        for i in self.nodes:
            ranx=random.randint(25,rev1-25)
            rany=random.randint(25,rev2-25)
            self.nodes[i].setpoint(ranx,rany)

    def drawnet(self,screen,maincolor):
        for i in self.nodes:
            self.nodes[i].drawcircle(screen,maincolor)
    def drawline(self,screen,maincolor):
        for i in self.nodes:
            print("馊了"+str(self.nodes[i].outs))
            for j in self.nodes[i].outs:
                print("画了：")
                pygame.draw.line(screen, maincolor, (self.nodes[i].x,self.nodes[i].y), (self.nodes[j].x,self.nodes[j].y))