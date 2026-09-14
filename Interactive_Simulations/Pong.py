import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")

# Colores
NEGRO = (0, 0, 0) # Tupla (R,G,B)
BLANCO = (255, 255, 255)
TURQUESA = (64, 224, 208)
AZUL_ELECTRICO = (0, 128, 255)
GRIS = (80, 80, 80)

# Reloj para controlar FPS
reloj = pygame.time.Clock()
FPS = 60

# Configuración de las palas
ANCHO_PALA, ALTO_PALA = 15, 100
VELOCIDAD_PALA = 7

pala_izq = pygame.Rect(30, ALTO // 2 - ALTO_PALA // 2, ANCHO_PALA, ALTO_PALA)
pala_der = pygame.Rect(ANCHO - 30 - ANCHO_PALA, ALTO // 2 - ALTO_PALA // 2, ANCHO_PALA, ALTO_PALA)

# Configuración de la pelota
TAMANO_PELOTA = 15
pelota = pygame.Rect(ANCHO // 2 - TAMANO_PELOTA // 2, ALTO // 2 - TAMANO_PELOTA // 2, TAMANO_PELOTA, TAMANO_PELOTA)
velocidad_pelota_x = 6 * random.choice((1, -1))
velocidad_pelota_y = 6 * random.choice((1, -1))

# Puntuaciones
puntos_izq = 0
puntos_der = 0

fuente = pygame.font.SysFont("Arial", 50)
fuente_small = pygame.font.SysFont("Arial", 20)


def reiniciar_pelota():
    pelota.center = (ANCHO // 2, ALTO // 2)
    vx = random.uniform(4,5.5) # La nueva pelota sale en velocidad random entre 4 y 5.5
    vy = random.uniform(4,5.5)
    return vx, vy


def dibujar():
    pantalla.fill(NEGRO)
    # Línea central
    for y in range(0, ALTO, 30):
        pygame.draw.rect(pantalla, GRIS, (ANCHO // 2 - 2, y, 4, 15))

    pygame.draw.rect(pantalla, TURQUESA, pala_izq)
    pygame.draw.rect(pantalla, AZUL_ELECTRICO, pala_der)
    pygame.draw.ellipse(pantalla, BLANCO, pelota)

    texto_izq = fuente.render(str(puntos_izq), True, BLANCO)
    texto_der = fuente.render(str(puntos_der), True, BLANCO)
    pantalla.blit(texto_izq, (ANCHO // 4, 20))
    pantalla.blit(texto_der, (ANCHO * 3 // 4 - texto_der.get_width(), 20))

    titulo = fuente.render("PONG", True, BLANCO)
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 5))
    ayuda = fuente_small.render("W/S  -  Flechas Arriba/Abajo  -  ESC para salir", True, BLANCO)
    pantalla.blit(ayuda, (ANCHO // 2 - ayuda.get_width() // 2, ALTO - 30))


def main():
    global velocidad_pelota_x, velocidad_pelota_y, puntos_izq, puntos_der

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    corriendo = False

        teclas = pygame.key.get_pressed()
        # Jugador izquierdo (W/S)
        if teclas[pygame.K_w] and pala_izq.top > 0:
            pala_izq.y -= VELOCIDAD_PALA
        if teclas[pygame.K_s] and pala_izq.bottom < ALTO:
            pala_izq.y += VELOCIDAD_PALA

        # Jugador derecho (Flechas)
        if teclas[pygame.K_UP] and pala_der.top > 0:
            pala_der.y -= VELOCIDAD_PALA
        if teclas[pygame.K_DOWN] and pala_der.bottom < ALTO:
            pala_der.y += VELOCIDAD_PALA

        # Mover la pelota
        pelota.x += velocidad_pelota_x
        pelota.y += velocidad_pelota_y

        # Rebote arriba/abajo
        if pelota.top <= 0 or pelota.bottom >= ALTO:
            velocidad_pelota_y *= -1

        # Rebote en las palas
        if pelota.colliderect(pala_izq) and velocidad_pelota_x < 0:
            velocidad_pelota_x *= -1.055
            velocidad_pelota_y *= 1.055
        if pelota.colliderect(pala_der) and velocidad_pelota_x > 0:
            velocidad_pelota_x *= -1.055
            velocidad_pelota_y *= 1.055

        # Puntos
        if pelota.left <= 0:
            puntos_der += 1
            velocidad_pelota_x, velocidad_pelota_y = reiniciar_pelota()
        if pelota.right >= ANCHO:
            puntos_izq += 1
            velocidad_pelota_x, velocidad_pelota_y = reiniciar_pelota()

        dibujar()
        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()