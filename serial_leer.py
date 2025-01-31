import serial, time                     #Import bibliotecas
interfaz = serial.Serial("COM4", 9600)  #Interfaz com4 y bautrate 9600
time.sleep(2)                           #esperar
interfaz.write(b'9')                    #Imprimir escribir byte
interfaz.close()                        #Cerrar interfaz








'''import serial, time                     #Import bibliotecas
interfaz = serial.Serial('COM4', 9600)  #Interfaz com4 y bautrate 9600
time.sleep(2)                           #esperar 
rawString = interfaz.readline()         #leer linea en raw
print(rawString)                        #Imprimir en cosola
interfaz.close()                        #Cerrar interfaz
'''




