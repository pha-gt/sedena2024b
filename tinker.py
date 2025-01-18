from tkinter import *                                                                       #importar componentes
from tkinter import ttk                                                                     #importar como ttk

class Conversor:                                                                            #clases Conversor
    def __init__(self, raiz):                                                               #constructor
        raiz.title("pies a Metros")                                                         #Define titulo a ventana
        
        self.pies = StringVar()                                                             #Atributos StringVar "relacionar"
        self.metros = StringVar()                                                           #Atributos StringVar "relacionar"
        
        mainframe = ttk.Frame(raiz, padding="3 3 12 12")                                    #Panel principal espacion T-B:3 R-L:12
        mainframe.grid(column=0, row= 0, sticky= (N,W,E,S))                                 #pintan dentro de raiz
        
        txPies = ttk.Entry (mainframe, width=7 , textvariable=self.pies)                    #Cuadro Pies, Asociar con self.pies
        txPies.grid(column=2, row= 1, sticky= (W,E))                                        #pinta en mainframe 2,1
        
        resMetros = ttk.Label(mainframe, textvariable=self.metros)                          #Etiqueta resMetros, Asociar con self.metros 
        resMetros.grid(column=2, row= 2, sticky= (W,E))                                     #pinta en mainframe 2,2
        
        ttk.Label(mainframe, text="pies").grid(column=3, row=1, sticky=W)                   #etiqueta y pintar
        ttk.Label(mainframe, text="es equivalente a ").grid(column=1, row=2, sticky=E)      #etiqueta y pintar
        ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)                 #etiqueta y pintar
        
        ttk.Button(mainframe, text="Calcular", command=self.calcular)                       #crear un button
            .grid(column=3, row=3, sticky=W)                                                #agregar en otro renglon
        
        txPies.focus()                                                                      #cursor en txPies
       
    def calcular(self, *args):                                                              #metodo calcular
        try:                                                                                #intentar
            valor = float(self.pies.get())                                                  #obtener dato capturado mediante self.pies
            self.metros.set(int(0.3048 * valor * 10000.0)/10000.0)                          #asignar a self.metros *tambien en resMetros
        except ValueError:                                                                  #Excepcion
            pass                                                                            #sin codigo
    
root = Tk()                                                                                 #Generar raiz
Conversor(root)                                                                             #Crear objeto Conversor
root.mainloop()                                                                             #mostrar root Ventana
        
        






 '''raiz.bind("<Return>", self.calcular)'''












'''
from tkinter import *                             #importar componentes
from tkinter import ttk                           #importar como ttk

def evaluar():
    mensaje = ""
    edad = int(txEdad.get())                      #obtener y convertir edad
    if(edad>17):
        mensaje = "Puedes pertenecer al EM"
    else:
        mensaje = "Edad insuficiente"
    txMSG.delete(0, END)                         #limpiar txMSG desde o al fin
    txMSG.insert(0, mensaje)                     #Escribir en txMSG desde 0
                                                                
                                                                
root = Tk()                                         #definir ventana root 
frm = ttk.Frame(root, padding=10)                   #definir frm como panel
frm.grid()                                          #"pintar en el centro"
etqEdad = ttk.Label(frm, text="Edad:")              #Etiqueta de edad
etqEdad.grid(column=0, row=0)                       #"pintar en 0,0"
txEdad = ttk.Entry(frm, width=20 )                  #crear una campo entrada Edad
txEdad.grid(column=1, row=0)                        #"pintar en posicion 1,0"
etqEdad = ttk.Label(frm, text="MSG:")               #Etiqueta de msg
etqEdad.grid(column=0, row=1)                       #"pintar en 0,1"
txMSG = ttk.Entry(frm, width=20 )                   #crear una campo entrada MSG
txMSG.grid(column=1, row=1)                         #"pintar en posicion 1,1"

btnEvaluar = ttk.Button(frm, text="Evaluar",
    command=evaluar)                                #Crear un boton
btnEvaluar.grid(column=1, row=2)                    #"pintar en posicion 1,2"
root.mainloop()      
'''




'''
from tkinter import *                                           #importar componentes
from tkinter import ttk                                         #importar como ttk

def saludar():
    print ("Hola")
    
def saludar2():
    print ("Hola "+txNombre.get())
    
def saludar3(veces):
    for i in range(veces):
        print ("Hola "+str(i))

root = Tk()                                                     #definir ventana root 
frm = ttk.Frame(root, padding=10)                               #definir frm como panel
frm.grid()                                                      #"pintar en el centro"
txNombre = ttk.Entry(frm, width=20 )                            #crear una campo entrada
txNombre.grid(column=0, row=0)                                  #"pintar en posicion 0,0"
btnSaludar = ttk.Button(frm, text="Saludar", command=saludar2)  #Crear un boton
                                                                #command es invocar saludar()
btnSaludar.grid(column=1, row=0)                                #"pintar en posicion 1,0"
btnSv = ttk.Button(frm, text="Saludar varios", command= lambda:saludar3(5) )  #Crear un botonSv
                                                                #command es invocar saludar()
btnSv.grid(column=2, row=0)                                     #"pintar en posicion 2,0"

root.mainloop()                                                 #mostrar Ventana root
'''



'''

def saludar3(veces):                                            #función saludar
    for i in range(veces):                                      #desde 0 hasta veces
        print ("Hola "+str(i))                                  #imprimir
    
     
btnSaludar = ttk.Button(frm, text="Saludar", command=saludar3)  #¿donde va el parametro?
btnVarios = ttk.Button(frm, text="varios", command= lambda:saludar3(5))  #lambda parametros
btnIngles = ttk.Button(frm, text="varios", command= lambda: print ("Hello") )  #lambda sentencia

'''





'''
from tkinter import *                                           #importar componentes
from tkinter import ttk                                         #importar como ttk

def saludar():
    print ("Hola")

def saludar2():
    print ("Hola "+txNombre.get())

root = Tk()                                                     #definir ventana root 
frm = ttk.Frame(root, padding=10)                               #definir frm como panel
frm.grid()                                                      #"pintar en el centro"
txNombre = ttk.Entry(frm, width=20 )                            #crear una campo entrada
txNombre.grid(column=0, row=0)                                  #"pintar en posicion 0,0"
btnSaludar = ttk.Button(frm, text="Saludar", command=saludar2)  #Crear un boton
                                                                #command es invocar saludar()
btnSaludar.grid(column=1, row=0)                                #"pintar en posicion 1,0"

root.mainloop()                                                 #mostrar Ventana root
'''




'''
from tkinter import *                                           #importar componentes
from tkinter import ttk                                         #importar como ttk
root = Tk()                                                     #definir ventana root 
frm = ttk.Frame(root, padding=10)                               #definir frm como panel
                                                                #root: frm esta dentro de root
                                                                #padding: espacio alrededor
frm.grid()                                                      #"pintar en el centro"
etiqueta = ttk.Label(frm, text="Hello World!")                  #crear una etiqueta
                                                                #frm es el padre: la etiqueta esta sobre frm
                                                                #text es el texto que contendrá
etiqueta.grid(column=0, row=0)                                  #"pintar en posicion 0,0"
miBoton = ttk.Button(frm, text="Quit", command=root.destroy)    #Crear un boton
                                                                #frm: el boton esta sobre frm
                                                                #text es el texto que contendrá
                                                                #command es invocar root.destroy()
                                                                #**No requiere parentesis y puede ser una función
miBoton.grid(column=1, row=0)                                   #"pintar en posicion 1,0"
                                                                           
root.mainloop()                                                 #mostrar Ventana root
'''




