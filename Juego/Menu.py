import pygame as pg
import random
import sys
import time 
# Inicializar Pygame
pg.init()


# Crear la ventana de Pygame
ancho, alto = 1000, 600
Menu = pg.display.set_mode((ancho, alto))
pg.display.set_caption("Menú del Juego")

# Cargar la imagen de fondo
fondo = pg.image.load("Imagenes/FondoMenu.png").convert()

# Cargar la imagen del botón Inicio
imagen_boton = pg.image.load("Imagenes\\boton inicio.png").convert_alpha()
boton_rect = imagen_boton.get_rect()


# Cargar la imagen del botón Niveles
imagen_niveles = pg.image.load("Imagenes\\boton_Niveles.png").convert_alpha()
boton_rect = imagen_boton.get_rect()

# Cargar la imagen del botón Inicio
imagen_salir = pg.image.load("Imagenes\\Boton_Salir.png").convert_alpha()
boton_rect = imagen_boton.get_rect()


# Calcular las coordenadas centradas para el botón de inicio
x_inicio = (ancho - boton_rect.width) // 2
y_inicio = (alto - boton_rect.height) // 2

# Calcular las coordenadas para el botón de niveles a la izquierda del botón de inicio
x_niveles = x_inicio - boton_rect.width - 120  # 10 píxeles de espacio entre los botones
y_niveles = y_inicio

# Calcular las coordenadas para el botón de salir a la derecha del botón de inicio
x_salir = x_inicio + boton_rect.width + 120  # 10 píxeles de espacio entre los botones
y_salir = y_inicio

# Actualizar las posiciones de los rectángulos
boton_rect.topleft = (x_inicio, y_inicio)
niveles_rect = imagen_niveles.get_rect(topleft=(x_niveles, y_niveles))
salir_rect = imagen_salir.get_rect(topleft=(x_salir, y_salir))

class Personaje:
    def __init__(self):
        self.movimiento = [pg.image.load('Personajes\\Enemigo1\\Volar1.png'),
                           pg.image.load('Personajes\\Enemigo1\\Volar2.png'),
                           pg.image.load('Personajes\\Enemigo1\\Volar3.png'),
                           pg.image.load('Personajes\\Enemigo1\\Volar4.png')]
        self.muerte = [pg.image.load('Personajes\\Enemigo1\\Muerte1.png'),
                       pg.image.load('Personajes\\Enemigo1\\Muerte2.png')]
        self.estado = 'movimiento'  # Estado inicial
        self.indice_animacion = 0
        self.tiempo_ultimo_cambio = time.time()
        self.intervalo_animacion = 0.1  # Intervalo de tiempo en segundos para cambiar la animación
        self.x, self.y = 800, 284
        self.velocidad = 4
        self.limite_inferior = 600 - 350
        self.vivo = True

    def actualizar_animacion(self):
        tiempo_actual = time.time()
        if tiempo_actual - self.tiempo_ultimo_cambio >= self.intervalo_animacion:
            self.indice_animacion = (self.indice_animacion + 1) % len(getattr(self, self.estado))
            self.tiempo_ultimo_cambio = tiempo_actual

    def dibujar(self, pantalla):
        imagen = getattr(self, self.estado)[self.indice_animacion]
        pantalla.blit(imagen, (self.x, self.y))
        self.hitbox = imagen.get_rect(topleft=(self.x, self.y))
        pg.draw.rect(pantalla, (255, 0, 0), self.hitbox, 2)  # Dibujar la hitbox
    def morir(self):
        self.estado = 'muerte'
        self.indice_animacion = 0
        self.tiempo_ultimo_cambio = time.time()
        

class Proyectil:
    def __init__(self, x, y, velocidad,imagen):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.imagen = imagen
        self.rect = self.imagen.get_rect(topleft=(self.x, self.y))
        self.radio = 15  # Radio del proyectil

    def mover(self):
        self.x -= self.velocidad
        self.rect.x = self.x

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def colision(self, personaje_rect):
        return personaje_rect.collidepoint(self.x, self.y)

class Niveles:
    def Nivel1():
        pg.init()
        w, h = 1000, 600
        
        PANTALLA = pg.display.set_mode((w, h))
        pg.display.set_caption("Nivel 2")
        x_pos=0

        fondo = pg.image.load("Imagenes\\FondoJuego_resized.jpg").convert()
        fondo = pg.transform.scale(fondo, (w, h))
        velocidad_fondo = 1

        #Imagen del Proyectil
        imagen_proyectil = pg.image.load("Personajes\\PersonajeNv2\\Animacion Ataque.png").convert_alpha()
          
        
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
        
        SaltoIzquierda = [pg.image.load('Personajes\\PersonajeNv2\\character_jump_0I.png'),
                      pg.image.load('Personajes\\PersonajeNv2\\character_jump_1I.png')]
                
        # Índice para la animación de movimiento a la derecha
        indice_animacion = 0
        tiempo_ultimo_cambio = time.time()
        intervalo_animacion = 0.1  # Intervalo de tiempo en segundos para cambiar la animación
        
        #Coordenadas Inicales
        personaje_x, personaje_y = 54 , 284
        velocidad_personaje = 4
        limite_inferior =  h - 350
        
        # Límites permitidos para el personaje
        limite_izquierdo, limite_derecho = 25, w - 50
        limite_superior = 5  # Límite superior de la pantalla
    
        distancia_maxima_elevacion = 250
        posicion_inicial_y = personaje_y
        
        #Variables para salto
        saltando = False
        velocidad_salto = 20
        gravedad = 0.8
        velocidad_y = 0

        # Fuente para la alerta de daño
        fuente_alerta = pg.font.Font(None, 36)
        alertas = []

        def mostrar_alerta(pantalla, x, y, texto, alertas):
            tiempo_alerta = 2  # Duración de la alerta en segundos
            alertas.append((texto, x, y, time.time(), tiempo_alerta))

        # Inicializar el temporizador
        tiempo_inicial = time.time()
        limite_minutos = 0.70
        #Vida del personaje
        vida_personaje = 100
        vida_maxima  = 100

        # Lista de proyectiles
        proyectiles = []
        tiempo_ultimo_proyectil = time.time()
        intervalo_proyectil = 1 # Intervalo de tiempo en segundos para generar proyectiles4
        velocidad_proyectil = 5 # Aumentar la velocidad de los proyectiles
        posicion_original_y = 284 

        personaje = Personaje()
        reloj = pg.time.Clock()
        
        
        ejecuta = True
        while ejecuta:
            if vida_personaje <= 0:
                print("Has muerto")
                # Mostrar mensaje en pantalla
                fuente = pg.font.Font(None, 36)
                texto = fuente.render("Has muerto", True, (255, 0, 0))
                PANTALLA.blit(texto, (PANTALLA.get_width() // 2 - texto.get_width() // 2, PANTALLA.get_height() // 2 - texto.get_height() // 2))
                pg.display.flip()
                pg.time.wait(3000)  # Esperar 3 segundos antes de cerrar
                ejecuta = False
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
            
            if not saltando:
                if teclas[pg.K_SPACE]:
                    saltando = True
                    velocidad_salto_inicial = velocidad_salto
            else:
                personaje_y -= velocidad_salto_inicial
                velocidad_salto_inicial -= gravedad
                if personaje_y >= posicion_original_y:
                    personaje_y = posicion_original_y
                    saltando = False
            
            #LLamamiento al fono en movimient
            PANTALLA.blit(fondo, (x_pos, 0))
            PANTALLA.blit(fondo, (x_pos + w, 0))
            # Personaje 1
            if saltando:
                if teclas[pg.K_a]:
                    PANTALLA.blit(SaltoIzquierda[0], (personaje_x, personaje_y))
                else:
                    PANTALLA.blit(Salto[0], (personaje_x, personaje_y))
            elif teclas[pg.K_d]:
                PANTALLA.blit(MDerecha[indice_animacion], (personaje_x, personaje_y))
            elif teclas[pg.K_a]:
                PANTALLA.blit(MIzquierda[indice_animacion], (personaje_x, personaje_y))
            else:
                PANTALLA.blit(Quieto[0], (personaje_x, personaje_y))

            # Calcular el tiempo transcurrido
            tiempo_transcurrido = time.time() - tiempo_inicial
            minutos = int(tiempo_transcurrido // 60)
            segundos = int(tiempo_transcurrido % 60)

            # Renderizar el temporizador
            fuente = pg.font.Font(None, 36)
            texto_tiempo = fuente.render(f"Tiempo: {minutos:02}:{segundos:02}", True, (255, 255, 255))
            PANTALLA.blit(texto_tiempo, (10, 10))

            # Renderizar la barra de vida
            ancho_barra_vida = 200
            alto_barra_vida = 20
            vida_actual_ancho = int((vida_personaje / vida_maxima) * ancho_barra_vida)
            barra_vida_rect = pg.Rect(10, 40, ancho_barra_vida, alto_barra_vida)
            vida_actual_rect = pg.Rect(10, 40, vida_actual_ancho, alto_barra_vida)
            pg.draw.rect(PANTALLA, (255, 0, 0), barra_vida_rect)  # Fondo de la barra de vida
            pg.draw.rect(PANTALLA, (0, 255, 0), vida_actual_rect)  # Vida actual

            # Generar nuevos proyectiles
            tiempo_actual = time.time()
            if tiempo_actual - tiempo_ultimo_proyectil >= intervalo_proyectil:
                x = 800  # Define la posición x del proyectil
                y = random.randint(200, 400)  # Generar una posición y aleatoria entre 285 y 600
                nuevo_proyectil = Proyectil(x, y, velocidad_proyectil, imagen_proyectil)
                proyectiles.append(nuevo_proyectil)
                tiempo_ultimo_proyectil = tiempo_actual


            # Mover y dibujar proyectiles
            for proyectil in proyectiles[:]:
                proyectil.mover()
                proyectil.dibujar(PANTALLA)
                personaje_hitbox = pg.Rect(personaje_x , personaje_y , Quieto[0].get_width(), Quieto[0].get_height())
                if proyectil.colision(personaje_hitbox):
                    vida_personaje -= 10
                    proyectiles.remove(proyectil)
                    mostrar_alerta(PANTALLA, personaje_x, personaje_y, "-1", alertas)
                # Dibujar la hitbox del personaje
                #pg.draw.rect(PANTALLA, (255, 255, 0), personaje_hitbox, 2)

            # Dibujar alertas activas
            for alerta in alertas[:]:
                texto, x, y, tiempo_inicio, duracion = alerta
                if time.time() - tiempo_inicio < duracion:
                    alerta_render = fuente_alerta.render(texto, True, (255, 0, 0))
                    PANTALLA.blit(alerta_render, (x, y - 50))  # Mostrar la alerta 50 píxeles arriba del personaje
                else:
                    alertas.remove(alerta)

            if minutos >= limite_minutos:
                texto_ganado = fuente.render("¡Has ganado!", True, (255, 255, 255))
                PANTALLA.blit(texto_ganado, (w // 2 - texto_ganado.get_width() // 2, h // 2 - texto_ganado.get_height() // 2))
                pg.display.flip()
                pg.time.delay(3000)  # Pausar por 3 segundos antes de cerrar
                ejecuta = False
            
            # Actualizar la animación del personaje
            personaje.actualizar_animacion()

            # Dibujar el personaje y su hitbox
            
            personaje.dibujar(PANTALLA)
            pg.display.flip()

              # Actualizar la pantalla

            pg.time.delay(10)
        # Reproducir la animación de muerte antes de cerrar el juego
        while personaje.indice_animacion < len(personaje.muerte) - 1:
            personaje.actualizar_animacion()
            PANTALLA.fill((0, 0, 0))  # Limpiar la pantalla
            personaje.dibujar(PANTALLA)
            pg.display.flip()
            reloj.tick(30)  # Limitar a 30 FPS
            

        pg.quit()

#Nivel 2 
class Proyectil:
    def __init__(self, x, y, velocidad,imagen):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.imagen = imagen
        self.rect = self.imagen.get_rect(topleft=(self.x, self.y))
        self.radio = 15  # Radio del proyectil

    def mover(self):
        self.x -= self.velocidad
        self.rect.x = self.x

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def colision(self, personaje_rect):
        return personaje_rect.collidepoint(self.x, self.y)



def Nivel21():
    pg.init()
    w, h = 1000, 600
    
    PANTALLA = pg.display.set_mode((w, h))
    pg.display.set_caption("Nivel 2")
    x_pos=0

    fondo = pg.image.load("Imagenes\\Fondo_Nivel2.png").convert()
    fondo = pg.transform.scale(fondo, (w, h))
    velocidad_fondo = 1

    #Imagen del Proyectil
    imagen_proyectil = pg.image.load("Personajes\\PersonajeNv2\\Animacion Ataque.png").convert_alpha()
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
    SaltoIzquierda = [pg.image.load('Personajes\\PersonajeNv2\\character_jump_0I.png'),
                    pg.image.load('Personajes\\PersonajeNv2\\character_jump_1I.png')]

    # Índice para la animación de movimiento a la derecha
    indice_animacion = 0
    tiempo_ultimo_cambio = time.time()
    intervalo_animacion = 0.1  # Intervalo de tiempo en segundos para cambiar la animación
    
    #Coordenadas Inicales
    personaje_x, personaje_y = 54 , 400
    velocidad_personaje = 4
    limite_inferior =  h - 350
    
    # Límites permitidos para el personaje
    limite_izquierdo, limite_derecho = 25, w - 50
    limite_superior = 5  # Límite superior de la pantalla

    distancia_maxima_elevacion = 250
    posicion_inicial_y = personaje_y
    
    #Variables para salto
    saltando = False
    velocidad_salto = 20
    gravedad = 0.8
    velocidad_y = 0

    # Fuente para la alerta de daño
    fuente_alerta = pg.font.Font(None, 36)
    alertas = []

    def mostrar_alerta(pantalla, x, y, texto, alertas):
        tiempo_alerta = 2  # Duración de la alerta en segundos
        alertas.append((texto, x, y, time.time(), tiempo_alerta))

    # Inicializar el temporizador
    tiempo_inicial = time.time()
    limite_minutos = 0.70
    #Vida del personaje
    vida_personaje = 100
    vida_maxima  = 100

    # Lista de proyectiles
    proyectiles = []
    tiempo_ultimo_proyectil = time.time()
    intervalo_proyectil = 0.8  # Intervalo de tiempo en segundos para generar proyectiles4
    velocidad_proyectil =  5 # Aumentar la velocidad de los proyectiles
    posicion_original_y = personaje_y
    
    nivel_ganado = False
    ejecuta = True
    while ejecuta:
        if vida_personaje <= 0:
            print("Has muerto")
            # Mostrar mensaje en pantalla
            fuente = pg.font.Font(None, 36)
            texto = fuente.render("Has muerto", True, (255, 0, 0))
            PANTALLA.blit(texto, (PANTALLA.get_width() // 2 - texto.get_width() // 2, PANTALLA.get_height() // 2 - texto.get_height() // 2))
            pg.display.flip()
            pg.time.wait(3000)  # Esperar 3 segundos antes de cerrar
            ejecuta = False
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
        
        if not saltando:
            if teclas[pg.K_SPACE]:
                saltando = True
                velocidad_salto_inicial = velocidad_salto
        else:
            personaje_y -= velocidad_salto_inicial
            velocidad_salto_inicial -= gravedad
            if personaje_y >= posicion_original_y:
                personaje_y = posicion_original_y
                saltando = False
        
        #LLamamiento al fono en movimient
        PANTALLA.blit(fondo, (x_pos, 0))
        PANTALLA.blit(fondo, (x_pos + w, 0))
        # Personaje 1
        if saltando:
            if teclas[pg.K_a]:
                PANTALLA.blit(SaltoIzquierda[0], (personaje_x, personaje_y))
            else:
                PANTALLA.blit(Salto[0], (personaje_x, personaje_y))
        elif teclas[pg.K_d]:
            PANTALLA.blit(MDerecha[indice_animacion], (personaje_x, personaje_y))
        elif teclas[pg.K_a]:
            PANTALLA.blit(MIzquierda[indice_animacion], (personaje_x, personaje_y))
        else:
            PANTALLA.blit(Quieto[0], (personaje_x, personaje_y))

        # Calcular el tiempo transcurrido
        tiempo_transcurrido = time.time() - tiempo_inicial
        minutos = int(tiempo_transcurrido // 60)
        segundos = int(tiempo_transcurrido % 60)

        # Renderizar el temporizador
        fuente = pg.font.Font(None, 36)
        texto_tiempo = fuente.render(f"Tiempo: {minutos:02}:{segundos:02}", True, (255, 255, 255))
        PANTALLA.blit(texto_tiempo, (10, 10))

        # Renderizar la barra de vida
        ancho_barra_vida = 200
        alto_barra_vida = 20
        vida_actual_ancho = int((vida_personaje / vida_maxima) * ancho_barra_vida)
        barra_vida_rect = pg.Rect(10, 40, ancho_barra_vida, alto_barra_vida)
        vida_actual_rect = pg.Rect(10, 40, vida_actual_ancho, alto_barra_vida)
        pg.draw.rect(PANTALLA, (255, 0, 0), barra_vida_rect)  # Fondo de la barra de vida
        pg.draw.rect(PANTALLA, (0, 255, 0), vida_actual_rect)  # Vida actual

        # Generar nuevos proyectiles
        tiempo_actual = time.time()
        if tiempo_actual - tiempo_ultimo_proyectil >= intervalo_proyectil:
            x = 800  # Define la posición x del proyectil
            y = random.randint(285, 600)  # Generar una posición y aleatoria entre 285 y 600
            nuevo_proyectil = Proyectil(x, y, velocidad_proyectil, imagen_proyectil)
            proyectiles.append(nuevo_proyectil)
            tiempo_ultimo_proyectil = tiempo_actual


        # Mover y dibujar proyectiles
        for proyectil in proyectiles[:]:
            proyectil.mover()
            proyectil.dibujar(PANTALLA)
            personaje_hitbox = pg.Rect(personaje_x , personaje_y , Quieto[0].get_width(), Quieto[0].get_height())
            if proyectil.colision(personaje_hitbox):
                vida_personaje -= 10
                proyectiles.remove(proyectil)
                mostrar_alerta(PANTALLA, personaje_x, personaje_y, "-1", alertas)
            # Dibujar la hitbox del personaje
            #pg.draw.rect(PANTALLA, (255, 255, 0), personaje_hitbox, 2)

        # Dibujar alertas activas
        for alerta in alertas[:]:
            texto, x, y, tiempo_inicio, duracion = alerta
            if time.time() - tiempo_inicio < duracion:
                alerta_render = fuente_alerta.render(texto, True, (255, 0, 0))
                PANTALLA.blit(alerta_render, (x, y - 50))  # Mostrar la alerta 50 píxeles arriba del personaje
            else:
                alertas.remove(alerta)

        if minutos >= limite_minutos:
            texto_ganado = fuente.render("¡Has ganado!", True, (255, 255, 255))
            PANTALLA.blit(texto_ganado, (w // 2 - texto_ganado.get_width() // 2, h // 2 - texto_ganado.get_height() // 2))
            pg.display.flip()
            pg.time.delay(3000)  # Pausar por 3 segundos antes de cerrar
            ejecuta = False
            nivel_ganado = True
            

        pg.display.flip()  # Actualizar la pantalla

        pg.time.delay(10)
    return nivel_ganado
    pg.quit()

# Bucle principal del menú
corriendo = True
while corriendo:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False
        elif evento.type == pg.MOUSEBUTTONDOWN:
            if boton_rect.collidepoint(evento.pos):
                print("Botón de inicio oprimido")               
                if Nivel21() == True:
                    Niveles.Nivel1()
            elif salir_rect.collidepoint(evento.pos):
                print("Botón de salir oprimido")
                corriendo = False
    
    if not corriendo:
        break

    Menu.blit(fondo, (0, 0))

    # Dibujar las imágenes de los botones
    Menu.blit(imagen_boton, boton_rect.topleft)
    Menu.blit(imagen_salir, salir_rect.topleft)

    # Actualizar la pantalla
    pg.display.flip()

# Salir de Pygame
pg.quit()