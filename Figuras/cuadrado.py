from figura import *

class cuadrado (figura):
    
    def calcularArea(self):
        p3=punto()
        p3.x=self.p1.x
        p3.y=self.p2.y
        self.area= p3.calDistancia(self.p1)**2

    def calperimetro(self):
        p3=punto()
        p3.x=self.p1.x
        p3.y=self.p2.y
        self.perimetro= p3.calDistancia(self.p1)*4
    
    
