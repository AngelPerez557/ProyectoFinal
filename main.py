import pygame as pg
import sys

# Inicializar Pygame
pg.init()


#Pantalla o Ventana
w,h=(1000,600)
PANTALLA = pg.display.set_mode((w,h))
FPS = 30
RELOJ = pg.time.Clock()


#Fondo del juego
fondo=pg.image.load("Imagenes\\FondoJuego_resized.jpg").convert()

#Imagenes Movimiento
Mderecha=[pg.image.load('Personajes\\Personaje1\\Derecho1.png'),
          pg.image.load('Personajes\\Personaje1\\Derecho2.png'),
          pg.image.load('Personajes\\Personaje1\\Derecho3.png'),
          pg.image.load('Personajes\\Personaje1\\Derecho4.png')]

SaltoMovimiento= [pg.image.load('Personajes\\Personaje1\\Salto2.png'),
                  pg.image.load('Personajes\\Personaje1\\Salto3.png'),
                  pg.image.load('Personajes\\Personaje1\\Salto4.png')]

MIzquierda=[pg.image.load('Personajes\\Personaje1\\Izquierdo1.png'),
            pg.image.load('Personajes\\Personaje1\\Izquierdo2.png'),
            pg.image.load('Personajes\\Personaje1\\Izquierdo3.png'),
            pg.image.load('Personajes\\Personaje1\\Izquierdo4.png')]

Quieto = pg.image.load('Personajes\\Personaje1\\Derecho1.png')


#Variables
x=0
px=50
py=200
ancho = 40
velocidad = 10
velocidad_animacion = 50

#Variables de Salto
salto = False
#Altura del salto 
cuentaSalto = 10
#Variables de direccion
Derecha = False
Izquierda = False
#Pasos
cuentaPasos = 0

#Movimiento
def recargarPantalla():
    #Variables Globales
    global cuentaPasos
    global x

    #Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width , 0))
    if x_relativa < w:
        PANTALLA.blit(fondo,(x_relativa,0))
    x-=1

    # Contador de pasos actualizado para todas las direcciones
    if cuentaPasos + 1 >= 6:
        cuentaPasos = 0

    # Movimiento a la Izquierda
    if Izquierda:
        PANTALLA.blit(MIzquierda[cuentaPasos // 1 % len(MIzquierda)], (int(px), int(py)))
        cuentaPasos += 1

# Movimiento a la derecha
    elif Derecha:
        PANTALLA.blit(Mderecha[cuentaPasos // 1 % len(Mderecha)], (int(px), int(py)))
        cuentaPasos += 1

# Movimiento de Salto
    elif salto + 1 >=2 :
        PANTALLA.blit(SaltoMovimiento[cuentaPasos // 1 % len(SaltoMovimiento)], (int(px), int(py)))
        cuentaPasos += 1

#Movimiento estatico
    else: 
        PANTALLA.blit(Quieto, (int(px), int(py)))
    
    pg.display.update()


ejecuta  = True
#Bucle del Juego
while ejecuta:
    
    RELOJ.tick(FPS)
    
    #Bucle del Juego
    for event in pg.event.get():
        if event.type == pg.QUIT:
            ejecuta = False
    #Teclas presionadas
    keys = pg.key.get_pressed()

    #Tecla A-Movimiento a la Izquierda
    if keys[pg.K_a] and px > velocidad:
        px -= velocidad
        Izquierda = True
        Derecha = False

    #Tecla D-Movimiento a la Izquierda
    elif keys[pg.K_d] and px < 900  - velocidad - ancho:
        px += velocidad
        Izquierda = False
        Derecha = True
    #Personaje Quieto
    else:
        Izquierda = False
        Derecha = False
        cuentaPasos = 0
    #Tecla W-Salto
    if not (salto):
        if keys[pg.K_SPACE] :
            salto = True
            Izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else: 
            cuentaSalto = 10
            salto = False   

    recargarPantalla()

#Salida del Juego
pg.quit()
   
   

