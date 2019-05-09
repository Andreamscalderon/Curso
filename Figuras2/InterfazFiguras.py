

from Tkinter import *
from threading import *
from time import sleep
from figura import *
from rectangulo import *
from circulo import *
from cuadrado import *
from triangulo import *
from puntos import *
class InterfaceFigura():

    def __init__(self):
        self.root = Tk()
       
        #self.frame.pack()
        
        #self.crono.cambiarEstado()
        #self.frame = Frame(self.root)
        #self.frame.pack()

        #self.cadena = StringVar()
        #self.display = Entry(self.frame, textvariable=self.cadena)
        #self.display = Label(self.frame, textvariable=self.cadena, font=("Helvetica", 30))
        #self.display.pack(side=TOP,padx=10,pady=10)

        #def figura():
            #print ("ha elegido la figura"+ variable.get())
            
        
        self.variable = StringVar(self.root)
        self.radiobutton1 = Radiobutton(text="Rectangulo", variable=self.variable, value=1, command=figura, activebackground="#555555", activeforeground="#AAAAAA")
        self.radiobutton2 = Radiobutton(text="cuadrado", variable=self.variable, value=2, command=figura, activebackground="#555555", activeforeground="#AAAAAA")
        self.radiobutton3 = Radiobutton(text="Triangulo", variable=self.variable, value=3, command=figura, activebackground="#555555", activeforeground="#AAAAAA")
        self.radiobutton4 = Radiobutton(text="circulo", variable=self.variable, value=4, command=figura,activebackground="#555555", activeforeground="#AAAAAA")
        self.radiobutton1.pack()
        self.radiobutton2.pack()
        self.radiobutton3.pack()
        self.radiobutton4.pack()

        self.buttonCalArea = Button(self.root, text="calcular Area")
        self.buttonCalArea.bind("<Button-1>", self.area)
        self.buttonCalArea.pack(side=RIGHT)
        
        self.buttonCalperimetro = Button(self.root, text="calcular Perimetro")
        self.buttonCalperimetro.bind("<Button-1>", self.perimetro)
        self.buttonCalperimetro.pack(side=LEFT)
        

        label1 = Label(self.root, text='ingrese coordenadas')
        label1.pack()
        self.valor = StringVar(self.root)
        entry1 = Entry(self.root, textvariable=self.valor)
        entry1.pack()

        self.resultado = StringVar(self.root)
        resultado_area = Label(self.root, textvariable=self.resultado)
        resultado_area.pack()
        self.root.mainloop()
        
    def area (self, event):
        self.figura()
        self.puntos ()
        self.f.calcularArea()
        self.resultado.set("el area es "+str(self.f.area))
        
    def perimetro (self, event):
        self.figura()
        self.puntos ()
        self.f.calperimetro()
        self.resultado.set("el perimetro es "+str (self.f.perimetro))
        
    def puntos (self):
        self.p = punto()
        self.q = punto()
        valores = [int(p) for p in self.valor.get().split()]
        self.p.x=valores[0]
        self.p.y=valores[1]
        self.q.x=valores[2]
        self.q.y=valores[3]
        self.f.setPuntos(self.p,self.q)
    
    def figura(self):
            if self.variable.get()=="1":
                self.f=rectangulo()
            elif self.variable.get()=="2":
                self.f=cuadrado()
            elif self.variable.get()=="3":
                self.f=triangulo()
            elif self.variable.get()=="4":
                self.f=circulo()
                        
            else:
                self.f=cuadrado()
    

it=InterfaceFigura()


