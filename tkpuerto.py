import serial
from tkinter import *                                                                       #importar componentes
from tkinter import ttk                                                                     #importar como ttk

#puerto = "COMX" # tipico en windows X= un entero positivo
#baudrate = 9600 #(o el baudrate adecuado/usado en putty)
#ser = serial.Serial(port=puerto, baudrate=baudrate)

class InterfazG:
    def __init__(self, raiz):

        self.raiz = raiz
        self.puerto = "COM3"
        self.baudrate = 9600
        self.ser = serial.Serial(port=self.puerto, baudrate=self.baudrate)


        raiz.title("Libros")
        mainframe = ttk.Frame(raiz, padding="3 3 12 12")                                    #Panel principal espacion T-B:3 R-L:12
        mainframe.grid(column=0, row= 0, sticky= (N,W,E,S))
        ttk.Button(mainframe, text="Apagar", command=self.apagar).grid(column=0, row=0, sticky=(W,E))
        ttk.Button(mainframe, text="Encender", command=self.encender).grid(column=0, row=1, sticky=(W,E))
        ttk.Button(mainframe, text="Salir", command=self.salir).grid(column=0, row=2, sticky=(W,E))
    def apagar(self):
        self.ser.write(b'A')

    def encender(self):
        self.ser.write(b'E')
    
    def salir(self):
        self.ser.close()
        self.raiz.destroy()

root = Tk()
InterfazG(root)
root.mainloop()
    



