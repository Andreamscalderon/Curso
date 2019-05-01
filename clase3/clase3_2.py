#import clase3
#print clase3.suma(4,3)


from clase3 import*
print ("ingrese numero")
x=input()
lista=juego(x)
print lista
cantidad=intentos(lista)
print (("tienes"),cantidad, ("intentos inicia"))

jugar(lista,cantidad)
        
    

