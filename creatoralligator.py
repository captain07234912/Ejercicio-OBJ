from Render import Render, color
from  ModelObj import *

"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/07/2020
SR3 : Obj
"""

########################### Lista de colores para probar
Fondo = color(0,0,0) #negro
Blanco = color(1,1,1)
CYAN = color(0,1,1)
Red = color(1,0,0)
BLUE = (0,0,1)
YELLOW = (1,1,0)

###########################################################
# tamaño de la imagen
prueba = Render(700,700)
# introduzca el tamaño del viewport
#prueba.glViewport(500, 150, 200 ,400)

# ingrese el color del fondo
prueba.glClearColor(0,0,0)

# ingrese el color para pintar
prueba.glColor(0, 0, 1)
prueba.glClear()

######################Punto ##################################
# si quiere pintar un punto es aqui
#prueba.punto(150,275)
#prueba.glColor(1,0,0)
#prueba.punto(100,200)

# quiere pintar una linea, perfecto! aca es el espacio
#prueba.glLinea(-1,1, 1,-1)
#prueba.glLinea(-1,-1,1,1)
#prueba.glLinea(1,0,-1,-1)
#prueba.glLinea(1,-1,1,1)


#################### Model Obj #############################################

prueba.generacionObj('./modelos/Charizard.obj', (350,100), (20,20))


prueba.glFinish('Modelo.bmp')



