from node import node
import pygame
import random
class network(object):
    def __init__(self,nodenum):
        self.nodenum=0
        self.nodes={}
        for i in range(1,nodenum+1):
            self.addnode(i)

    def addnode(self,nodeid):
        self.nodes[nodeid]=node(nodeid)
        self.nodenum+=1



    def print(self):
        for i in self.nodes:
            print("第"+str(i)+"个"+str(self.nodes[i].nodeid))
            for j in self.nodes[i].ins:
                print(" "+str(i)+"<<"+str(j))
            for k in self.nodes[i].outs:
                print(" "+str(i)+">>" + str(k))

    def havelink(self,nodefrom,nodeto):
        have=False
        for i in self.nodes[nodefrom].outs:
            if (i==nodeto):
                have = True

        for i in self.nodes[nodefrom].ins:
            if (i==nodeto):
                have = True
        return have

    def addlink(self,nodefrom,nodeto):
        if not self.havelink(nodefrom,nodeto) and (nodefrom!=nodeto):
            self.nodes[nodefrom].addout(nodeto)
            self.nodes[nodeto].addin(nodefrom)
            self.nodes[nodefrom].size += 1
            self.nodes[nodeto].size += 1

    def setpoints(self,rev1,rev2):
        for i in self.nodes:
            itsnotok=True
            ranx=1
            rany=1
            while itsnotok:
                somethingwrong=False
                ranx=random.randint(20,rev1-20)
                rany=random.randint(20,rev2-20)
                for j in self.nodes:
                    if (somethingwrong):
                        break
                    x1=ranx
                    y1=rany
                    x2=self.nodes[j].x
                    y2=self.nodes[j].y
                    if( x2!=0  and y2!=0 ):
                        if(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 <= self.nodes[i].size*2):
                            somethingwrong=True


                if(somethingwrong):
                    itsnotok=True
                else:
                    itsnotok = False

            self.nodes[i].setpoint(ranx,rany)

    def drawnet(self,screen,maincolor):
        for i in self.nodes:
            self.nodes[i].drawcircle(screen,maincolor,self.nodes[i].size)
    def drawline(self,screen,maincolor):
        for i in self.nodes:
            for j in self.nodes[i].outs:
                pygame.draw.line(screen, maincolor, (self.nodes[i].x,self.nodes[i].y), (self.nodes[j].x,self.nodes[j].y))