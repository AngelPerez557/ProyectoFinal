import pygame as pg
import random
import sys
import time 


class Niveles:
    def Nivel2():
        pg.init()
        w, h = 1000, 600
        
        PANTALLA = pg.display.set_mode((w, h))
        pg.display.set_caption("Nivel 2")
        x_pos=0

        fondo = pg.image.load("Imagenes\\Fondo_Nivel2.png").convert()
        fondo = pg.transform.scale(fondo, (w, h))
        velocidad_fondo = 0.1

        #Personaje1=   
        Quieto = [pg.image.load('Personajes\\PersonajeNv2\\character_idle_0.png'),
        pg.image.load('Personajes\\PersonajeNv2\\character_idle_0.png')]

        MDerecha = [pg.image.load('Personajes\\PersonajeNv2\\character_run_0.png'),
        pg.image.load('Personajes\\PersonajeNv2\\character_run_1.png'),
        pg.image.load('Personajes\\PersonajeNv2\\character_run_2.png'),
        pg.image.load('Personajes\\PersonajeNv2\\character_run_3.png'),]

        MIzquierda = [pg.image.load('Personajes\\PersonajeNv2\\character_run_0I.png'),
        pg.image.load('Personajes\\PersonajeNv2\\character_run_1I.png'),
        pg.image.load('Personajes\\PersonajeNv2\\character_run_2I.png'),
        pg.image.load('Personajes\\PersonajeNv2\\character_run_3I.png'),]

        Salto = [pg.image.load('Personajes\\PersonajeNv2\\character_jump_0.png'),
                pg.image.load('Personajes\\PersonajeNv2\\character_jump_1.png')]

        # Índice para la animación de movimiento a la derecha
        indice_animacion = 0
        tiempo_ultimo_cambio = time.time()
        intervalo_animacion = 0.1  # Intervalo de tiempo en segundos para cambiar la animación
        
        #Coordenadas Inicales
        personaje_x, personaje_y = 54 , 250
        velocidad_personaje = 1
        limite_inferior =  h - 350
        
        # Límites permitidos para el personaje
        limite_izquierdo, limite_derecho = 25, w - 50
        limite_superior = 5  # Límite superior de la pantalla
    
        distancia_maxima_elevacion = 250
        posicion_inicial_y = personaje_y
        
        #Variables para salto
        saltando = False
        velocidad_salto = 5
        gravedad = 0.1
        velocidad_y = 0

        ejecuta = True

        while ejecuta:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    ejecuta = False
            x_pos -= velocidad_fondo
            if x_pos <= -w:
                x_pos = 0


            # Obtener las teclas presionadas
            teclas = pg.key.get_pressed()             
            if teclas[pg.K_a] and personaje_x > limite_izquierdo:
                personaje_x -= velocidad_personaje
                if time.time() - tiempo_ultimo_cambio > intervalo_animacion:
                    tiempo_ultimo_cambio = time.time()
                    indice_animacion = (indice_animacion + 1) % len(MIzquierda)
            if teclas[pg.K_d] and personaje_x < limite_derecho - MDerecha[0].get_width():
                personaje_x += velocidad_personaje
                if time.time() - tiempo_ultimo_cambio > intervalo_animacion:
                    tiempo_ultimo_cambio = time.time()
                    indice_animacion = (indice_animacion + 1) % len(MDerecha)  # Reiniciar la animación cuando no se presiona la tecla A
            
            if teclas[pg.K_w] and not saltando:
                saltando = True
                velocidad_y = -velocidad_salto

            if saltando:
                personaje_y += velocidad_y
                velocidad_y += gravedad
                if personaje_y >= limite_inferior:
                    personaje_y = limite_inferior
                    saltando = False
            
            #LLamamiento al fono en movimient
            PANTALLA.blit(fondo, (x_pos, 0))
            PANTALLA.blit(fondo, (x_pos + w, 0))
            # Personaje 1
            if saltando:
                PANTALLA.blit(Salto[0], (personaje_x, personaje_y))
            elif teclas[pg.K_d]:
                PANTALLA.blit(MDerecha[indice_animacion], (personaje_x, personaje_y))
            elif teclas[pg.K_a]:
                PANTALLA.blit(MIzquierda[indice_animacion], (personaje_x, personaje_y))
            else:
                PANTALLA.blit(Quieto[0], (personaje_x, personaje_y))  

            pg.display.flip()  # Actualizar la pantalla

        pg.quit()
Niveles.Nivel2()