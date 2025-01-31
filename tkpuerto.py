import serial
from tkinter import *                                                                      
from tkinter import ttk                                                                    

class InterfazG:
    def __init__(self, raiz):
        
        #Datos de conexión
        self.raiz = raiz
        self.puerto = "COM3"
        self.baudrate = 9600
        self.ser = serial.Serial(port=self.puerto, baudrate=self.baudrate)

        #Ventana
        raiz.title("Encender")
        mainframe = ttk.Frame(raiz, padding="3 3 12 12")                                   
        mainframe.grid(column=0, row= 0, sticky= (N,W,E,S))
        ttk.Button(mainframe, text="Apagar", command=self.apagar).grid(column=0, row=0, sticky=(W,E))
        ttk.Button(mainframe, text="Encender", command=self.encender).grid(column=0, row=1, sticky=(W,E))
        ttk.Button(mainframe, text="Salir", command=self.salir).grid(column=0, row=2, sticky=(W,E))

    # Eventos    
    def apagar(self):
        self.ser.write(b'A')

    def encender(self):
        self.ser.write(b'E')
    
    def salir(self):
        self.ser.close()
        self.raiz.destroy()
#Rutina
root = Tk()
InterfazG(root)
root.mainloop()
    



