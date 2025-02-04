from tkinter import *                                           #importar componentes
from tkinter import ttk                                         #importar como ttk


class Libro:
    def __init__(self, autor,titulo,pais,genero, presentacion, disponibilidad):
        self.autor = autor                                      #string para un autor
        self.titulo = titulo                                    #string para un titulo
        self.pais = pais                                        #string para un pais
        self.genero = genero                                    #string para un genero literario
        self.presentacion = presentacion                        #arreglo string digita / Fisico
        self.disponibilidad = disponibilidad                    #Disponible y agotado


root = Tk() 


campo_autor = StringVar()                                   #StringVar para un autor
campo_titulo = StringVar()                                  #StringVar para un titulo
campo_pais = StringVar()                                    #StringVar para pais
campo_genero = StringVar()                                  #StringVar para genero
campo_presentacion_fisico = BooleanVar()                    #BooleanVar TRUE / FALSE
campo_presentacion_digital = BooleanVar()                   #BooleanVar TRUE / FALSE
campo_disponibilidad = StringVar()                          #StringVar Disponibilidad                              

lista_libros =[]


def  InterfazG(raiz):   
    #titulo de la ventana                                      
    raiz.title("Libros")                                        
    mainframe = ttk.Frame(raiz, padding="3 3 12 12")                    #Panel principal espacion T-B:3 R-L:12
    mainframe.grid(column=0, row= 0, sticky= (N,W,E,S))

    #Etiqueta e input Autor
    ttk.Label(mainframe, text= "Autor").grid(column=0,row=0, sticky=W)
    txAutor = ttk.Entry (mainframe, width=7, textvariable=campo_autor)                            
    txAutor.grid(column=1,row=0, sticky=(W,E))
     
     #Etiqueta e input Titulo
    ttk.Label(mainframe, text= "Titulo").grid(column=0, row=1, sticky=W)
    txtTitulo = ttk.Entry (mainframe, width=7, textvariable=campo_titulo)
    txtTitulo.grid(column=1,row=1, sticky=(W,E))
    
    #Etiqueta e input Pais
    ttk.Label(mainframe, text="Pais").grid(column=0, row=2, sticky=W)
    txtPais = ttk.Entry (mainframe, width=7,textvariable=campo_pais)
    txtPais.grid(column=1,row=2, sticky=(W,E))
    
    #Etiqueta y combobox Genero                                         
    ttk.Label(mainframe, text="Genero").grid(column=0, row=3, sticky=W)
    #parametro values contiene opciones a mostrar
    cbGenero = ttk.Combobox(mainframe, values=["Ciencia","Infantil","Fantasia","Terror","Ciencia ficción"], textvariable=campo_genero)
    cbGenero.grid(column=1,row=3)
    
    #Etiqueta y checkbox Presentacion  
    ttk.Label(mainframe, text="Presentacion").grid(column=0, row=4, sticky=W)
    chPresentacion_fisico = ttk.Checkbutton(mainframe,text="Físico",variable=campo_presentacion_fisico)
    chPresentacion_fisico.grid(column=1,row=4,sticky=W)
    chPresentacion_digital = ttk.Checkbutton(mainframe,text="Digital",variable=campo_presentacion_digital)
    chPresentacion_digital.grid(column=1,row=5,sticky=W)
    
    #Etiqueta y combobox Genero
    ttk.Label(mainframe, text="Disponibilidad").grid(column=0, row=6, sticky=W)
    rDisp_disponible = ttk.Radiobutton(mainframe, text='Disponible', variable=campo_disponibilidad, value='disponible')
    rDisp_disponible.grid(column=1,row = 7, sticky=W)
    rDisp_disponible = ttk.Radiobutton(mainframe, text='Agotado', variable=campo_disponibilidad, value='agotado')
    rDisp_disponible.grid(column=1,row = 8, sticky=W)
    
    ttk.Button(mainframe, text="Registrar", command=registrar).grid(column=0, row=9, sticky=(W,E), columnspan=2)
    ttk.Button(mainframe, text="limpiar", command=limpiar).grid(column=0, row=10, sticky=(W,E), columnspan=2)
    ttk.Button(mainframe, text="Ver Tabla", command=verTabla).grid(column=0, row=11, sticky=(W,E), columnspan=2)
    
    
def obtener_libro():
    lista_presentaciones = []
    if(campo_presentacion_fisico.get()):
        lista_presentaciones.append("fisico")
    if(campo_presentacion_digital.get()):
        lista_presentaciones.append("digital")

    return Libro(campo_autor.get(),
        campo_titulo.get(),
        campo_pais.get(),
        campo_genero.get(),
        lista_presentaciones,
        campo_disponibilidad.get())

def registrar():
    libro = obtener_libro()
    lista_libros.append(libro)
    print("libro agregado")
    
def limpiar():
    campo_autor.set("")
    campo_titulo.set("")
    campo_pais.set("")
    campo_genero.set("")
    campo_disponibilidad.set("")
    campo_presentacion_fisico.set(FALSE)
    campo_presentacion_digital.set(FALSE)
    
def verTabla():
    nuevaVentana =Toplevel()
    InterfazTabla(nuevaVentana)
    
def verRegistro():
    InterfazG(root)
    

def InterfazTabla(raiz):

    raiz.title("Tabla Libros")                                              
    mainframe = ttk.Frame(raiz, padding="3 3 12 12")                    #Panel principal espacion T-B:3 R-L:12
    mainframe.grid(column=0, row= 0, sticky= (N,W,E,S)) 
    tabla = ttk.Treeview(mainframe, columns=('autor','pais','genero', 'pres','disp'), show='headings')  #componente padre y columnas
    #Nombrando cada cabecera
    tabla.heading('autor', text ="Autor")                                                
    tabla.heading('pais', text ="Pais")                                                  
    tabla.heading('genero', text ="Genero")    
    tabla.heading('pres', text ="Presentación")  
    tabla.heading('disp', text ="Disposición")                                              
    # insertar datos 
    for libro in lista_libros:
        #unir las opciones de presentacion en una linea
        cadena_presentacion = ""
        for opcion in libro.presentacion:
            cadena_presentacion= cadena_presentacion+" "+opcion
        #insertar    
        tabla.insert('','end', values=(libro.autor,libro.pais, libro.genero, cadena_presentacion,libro.disponibilidad))                             
    tabla.grid(column=0, row = 0)                                                          
    





InterfazG(root)
root.mainloop()


#root = Tk()





'''OBJETOS
from tkinter import *                                           #importar componentes
from tkinter import ttk                                         #importar como ttk
                                                                #Clase libro 
class Libro:
    def __init__(self, autor,titulo,pais,
        genero, presentacion, disponibilidad):

        self.autor = autor                                      #string para un autor
        self.titulo = titulo                                    #string para un titulo
        self.pais = pais                                        #string para un pais
        self.genero = genero                                    #string para un genero literario
        self.presentacion = presentacion                        #arreglo string digita / Fisico
        self.disponibilidad = disponibilidad                    #Disponible y agotado


class InterfazG:
    def __init__(self, raiz):
                                                                #Variables de enlace componente
        self.campo_autor = StringVar()                          #stringVar para un autor
        self.campo_titulo = StringVar()                         #stringVar para un Titulo
        self.campo_pais = StringVar()                           #
        self.campo_genero = StringVar()
        self.campo_presentacion_fisico = BooleanVar()
        self.campo_presentacion_digital = BooleanVar()
        self.campo_disponibilidad = StringVar()

                                                                #titulo de la ventana
        raiz.title("Libros")
        mainframe = ttk.Frame(raiz, padding="3 3 12 12")        #Panel principal espacion T-B:3 R-L:12
        mainframe.grid(column=0, row= 0, sticky= (N,W,E,S))

                                                                #Etiqueta e input Autor
        ttk.Label(mainframe, text= "Autor").grid(column=0,row=0, sticky=W)
        txAutor = ttk.Entry (mainframe, width=7, textvariable=self.campo_autor)                            
        txAutor.grid(column=1,row=0, sticky=(W,E))
                                                                #Etiqueta e input Titulo
        ttk.Label(mainframe, text= "Titulo").grid(column=0, row=1, sticky=W)
        txtTitulo = ttk.Entry (mainframe, width=7)
        txtTitulo.grid(column=1,row=1, sticky=(W,E))
                                                                #Etiqueta e input Pais
        ttk.Label(mainframe, text="Pais").grid(column=0, row=2, sticky=W)
        txtPais = ttk.Entry (mainframe, width=7)
        txtPais.grid(column=1,row=2, sticky=(W,E))
                                                                #Etiqueta y combobox Genero
                                                                #parametro values contiene opciones a mostrar
        ttk.Label(mainframe, text="Genero").grid(column=0, row=3, sticky=W)
        cbGenero = ttk.Combobox(mainframe, values=("Ciencia","Infantil","Fantasia","Terror","Ciencia ficción"), textvariable=self.campo_genero)
        cbGenero.grid(column=1,row=3)
        ttk.Label(mainframe, text="Presentacion").grid(column=0, row=4, sticky=W)
        chPresentacion_fisico = ttk.Checkbutton(mainframe,text="Físico",variable=self.campo_presentacion_fisico)
        chPresentacion_fisico.grid(column=1,row=4,sticky=W)
        chPresentacion_digital = ttk.Checkbutton(mainframe,text="Digital",variable=self.campo_presentacion_digital)
        chPresentacion_digital.grid(column=1,row=5,sticky=W)
        ttk.Label(mainframe, text="Disponibilidad").grid(column=0, row=6, sticky=W)
        rDisp_disponible = ttk.Radiobutton(mainframe, text='Disponible', variable=self.campo_disponibilidad, value='disponible')
        rDisp_disponible.grid(column=1,row = 7, sticky=W)
        rDisp_disponible = ttk.Radiobutton(mainframe, text='Agotado', variable=self.campo_disponibilidad, value='agotado')
        rDisp_disponible.grid(column=1,row = 8, sticky=W)

        ttk.Button(mainframe, text="Registrar", command=self.registrar).grid(column=0, row=9, sticky=(W,E), columnspan=2)
    
    def obtener_libro(self):
        lista_presentaciones = []
        if(self.campo_presentacion_fisico.get()):
            lista_presentaciones.append("fisico")
        if(self.campo_presentacion_digital.get()):
            lista_presentaciones.append("digital")

        return Libro(self.campo_autor.get(),
            self.campo_titulo.get(),
            self.campo_pais.get(),
            self.campo_genero.get(),
            lista_presentaciones,
            self.campo_disponibilidad)

    def registrar(self):
        libro = self.obtener_libro()
        print(str(libro))


        


root = Tk()
InterfazG(root)
root.mainloop()
'''



'''
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

        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=3, row=3, sticky=W)                       #crear un button
                                                            #agregar en otro renglon
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
'''



'''
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

        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=3, row=3, sticky=W)                       #crear un button
                                                            #agregar en otro renglon
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
'''







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
