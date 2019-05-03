from Cronometro import *

print ("ingrese numero")
v=input()

c=Cronometro ()
c.setTiempo(v)

for i in range(3600):
    c.retroceder()
    print c.getTiempo()
