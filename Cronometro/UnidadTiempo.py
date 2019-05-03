class UnidadTiempo():
    def __init__(self):
        self.valor=0
        self.tope=0
    def avanzar (self):
        if self.valor<self.tope:
            self.valor+=1
        else:
            self.valor=0
    def getValor(self):
        return self.valor

    def retroceder (self):
        if self.valor>0:
            self.valor-=1
        else:
            self.valor=self.tope
        
    def getTope (self):
        return self.tope
    def setValor(self,v):
        self.valor=v
