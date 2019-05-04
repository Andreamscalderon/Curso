from math import *
class punto():
    def __init__(self):
        self.x=0
        self.y=0
    def calDistancia (self, punto):
        return sqrt((self.x - punto.x)**2 +(self.y-punto.y)**2)
