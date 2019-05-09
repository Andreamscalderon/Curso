from Tkinter import *
from threading import *
from time import sleep

from puntos import*
from rectangulo import *
from cuadrado import *
from circulo import *
from triangulo import *


print ("ingrese x punto1")
p1=punto()
p2=punto()
p1.x=input()
print ("ingrese y punto1")
p1.y=input()
print ("ingrese x punto2")
p2.x=input()
print ("ingrese y punto2")
p2.y=input()

r=rectangulo ()
r.setPuntos(p1,p2)
r.calcularArea()
r.calperimetro()
print "area del rectangulo " + str(r.area)
print "perimetro del rectangulo " +  str(r.perimetro)

c=cuadrado()
c.setPuntos(p1,p2)
c.calcularArea()
c.calperimetro()
print "area del cuadro " +  str(c.area)
print "perimetro del cuadro " +  str(c.perimetro)

ci=circulo ()
ci.setPuntos(p1,p2)
ci.calcularArea()
ci.calperimetro()
print "area del circulo " +  str(ci.area)
print "perimetro del circulo " +  str(ci.perimetro)

t=triangulo ()
t.setPuntos(p1,p2)
t.calcularArea()
t.calperimetro()
print "area del triangulo " +  str(t.area)
print "perimetro del triangulo " +  str(t.perimetro)
