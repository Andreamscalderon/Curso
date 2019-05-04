from puntos import *

class figura ():
    
    def __init__(self):
        self.p1=punto()
        self.p2=punto()
        self.area=0
        self.perimetro=0
        
    def setPuntos(self,p,q):
        self.p1=p
        self.p2=q
