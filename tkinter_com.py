from tkinter import *                                           #importar componentes
from tkinter import ttk                                         #importar como ttk

def funcion1():
        print("hola")

def check1():
        global valorCheck
        print("check:"+valorCheck.get())

def check2():
        global valorCheck2
        if(valorCheck2.get()=='1'):
                print("Terminos aceptados")
 
def fdescripcion():                                     #Rutina de boton descripcion
        global tDescripcion                             #Especificar que el componente es global
        print(tDescripcion.get(1.0, END))               #imprimir desde el primer renglon al ultimo 


root = Tk()                                             #Ventana
mainframe = ttk.Frame(root, padding="3 3 12 12")        #Panel principal padding son espacio
mainframe.grid(column=0, row= 0, sticky= (N,W,E,S))     #Definir en ubicacion en Grid


#parent es un Frame base
label = ttk.Label(mainframe, text='Full name:')           #Etiqueta con texto
label.grid(column=0, row= 0, sticky= (N,W,E,S))           #Ubicar en grid

#Etiqueta con imagen
imagen_darwin= PhotoImage(file='hexley.png')              #Imagen en raiz   
imagen_darwin = imagen_darwin.subsample(2)               #reducir
#imagen_darwin = imagen_darwin.zoom(2)                    #ampliar
label_image = ttk.Label(mainframe, image = imagen_darwin) #Etiqueta con imagen
label_image.grid(column=0, row= 1)                        #ubicar en grid

#label "anonimo"
ttk.Label(mainframe, text='anonimo').grid(column=0, row= 2)

#button invoca una función
button1 = ttk.Button(mainframe, text='botton1', command=funcion1 )
button1.grid(column=0, row= 3)                          #Ubicar en grid 

#button invoca un metodo
button2 = ttk.Button(mainframe, text='botton2', command=funcion1 )
button2.grid(column=0, row= 4)                          #Ubicar en grid
button2.state(['disabled'])                             #desabilitar
button2.state(['!disabled'])                            #quitar deshabilitar                
#button "anonimo"
ttk.Button(mainframe, text='botton3', command=funcion1).grid(column=0, row= 5)



#checkbox
valorCheck = StringVar()                                #variable string asociada
check = ttk.Checkbutton(mainframe, text='Métrico',      #componente padre y  texto a aparecer
	        command=check1, variable=valorCheck,    #rutina a realizar, variable asociada
	        onvalue='metrico', offvalue='imperial') #valor checado y valor no checado
check.grid(column=0, row= 6)

#checkbox por defecto, onvalue='1' offvalue='0'
valorCheck2= StringVar()   
check2 = ttk.Checkbutton(mainframe, text='Acepto',      #componente padre y texto a aparecer
                command=check2, variable=valorCheck2)   #rutina a realizar, variable asociada
check2.grid(column=0, row= 7)



#Radiobutton
valorIdioma = StringVar()                               #Misma variable para todos los radiobutton 
rbOpcion1 = ttk.Radiobutton(mainframe, text ='Ingles',  #Componente padre y texto a aparecer
        variable = valorIdioma, value="ing")            #variable asociada y valor
rbOpcion2 = ttk.Radiobutton(mainframe, text ='Español', #Componente padre y texto a aparecer
        variable = valorIdioma, value="esp")            #variable asociada y valor    
rbOpcion3 = ttk.Radiobutton(mainframe, text ='Coreano', #Componente padre y texto a aparecer
        variable = valorIdioma, value="cor")            #variable asociada y valor      
rbOpcion1.grid(column=0, row= 8)
rbOpcion2.grid(column=0, row= 9)
rbOpcion3.grid(column=0, row= 10)

#Entry
urlValor = StringVar()
eUrl = ttk.Entry(mainframe, textvariable = urlValor)    #Componente padre y variable asociada
eUrl. grid(column = 0, row = 11)
urlValor.set("mi Entry")                                #escribir en componente
print(urlValor.get())                                   #obtener dato

#Entry password
secreto = StringVar()
ePass = ttk.Entry(mainframe, textvariable = secreto,    #Componente padre y variable asociada
        show="*")                                       #caracter escritura 
ePass.grid(column = 0, row = 12)
ePass.state(['disabled'])                               #deshabilidado
ePass.state(['!disabled'])                              #habilidado

#Combobox *solo escritura
paisValor = StringVar()
cbPais = ttk.Combobox(mainframe, textvariable= paisValor)   #Componente padre y variable asociada
cbPais.grid(column = 0, row = 13)       

#Combobox opciones
marcaValor = StringVar()
cbMarca = ttk.Combobox(mainframe, textvariable= marcaValor, #Componente padre y variable asociada
        values=['Nike', 'Puma', 'Adidas'] )               #Opciones
cbMarca.grid(column = 0, row = 14)       

#Combobox evento
colorValor = StringVar()
colores= ['rojo', 'verde', 'azul', 'amarillo', 'rosa']
cbColor = ttk.Combobox(mainframe, textvariable= colorValor)#Componente padre y variable asociada
cbColor['values']= colores                                 #Opciones
cbColor.grid(column = 0, row = 15)  
cbColor.state(["readonly"])                                #Solo seleccionar

#Text
#los Text no tienen variable de referencia
tDescripcion = Text(mainframe, width=40, height=10)                         #componente padre y dimención
tDescripcion.grid(column = 0, row = 16)                                     
bDescripcion = ttk.Button(mainframe, text='imprimir', command=fdescripcion )#Crear un boton
bDescripcion.grid(column = 0, row = 17)                         

#treeview
tree = ttk.Treeview(mainframe, columns=('nombre','marca','precio'), show='headings')  #componente padre y columnas
tree.heading('nombre', text ="NOMBRE")                                                #Columna nombre a NOMBRE 
tree.heading('marca', text ="MARCA")                                                  #Columna marca a MARCA
tree.heading('precio', text ="PRECIO")                                                #Columna precio a PRECIO
# insertar datos 
tree.insert('','end', values=('Playera','Puma','750.00'))                             #playera
tree.insert('','end', values=('Gorra','Nike','350.00'))                               #Gorra
tree.insert('','end', values=('Tenis','Nike','3499.00'))                              #Tenis
#definir coordenada
tree.grid(column=0, row = 18)                                                           


#button invoca 
root.mainloop()


