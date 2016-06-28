from network import network
from windows import windows
'''
n1=network(9)
n1.addlink(4,5)
n1.setpoints(800,600)
'''
n1=network(9)
n1.addlink(1,9)
n1.addlink(2,4)
w1=windows(800,600,n1)