from figura import *
import math 

class circulo (figura):

    def calcularArea(self):
        self.area= ((self.p1.calDistancia(self.p2))**2)*math.pi
    
    def calperimetro(self):
        self.perimetro= self.p1.calDistancia(self.p2)*2*math.pi
