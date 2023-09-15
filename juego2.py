import pygame
import math

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Triángulo en movimiento")

# Colores
white = (255, 255, 255)

# Posición inicial del triángulo
x = screen_width // 2
y = screen_height // 2

# Velocidad inicial
speed = 2
rotation_speed = 2

# Velocidad máxima
max_speed = 10

# Ángulo inicial
angle = 0

# Función para rotar el triángulo
def rotate_triangle(surface, angle, x, y):
    rotated_triangle = pygame.transform.rotate(surface, -angle)
    new_rect = rotated_triangle.get_rect(center=surface.get_rect(topleft=(x, y)).center)
    return rotated_triangle, new_rect

# Cargar el triángulo
triangle_width = 50
triangle_height = 50
triangle_surface = pygame.Surface((triangle_width, triangle_height), pygame.SRCALPHA)
pygame.draw.polygon(triangle_surface, (255, 0, 0), [(0, 0), (triangle_width, 0), (triangle_width / 2, triangle_height)])
triangle_rect = triangle_surface.get_rect()

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    # Control de velocidad
    if keys[pygame.K_UP]:
        speed += 0.1
    elif keys[pygame.K_DOWN]:
        speed -= 0.1

    # Limitar la velocidad máxima
    speed = min(max_speed, max(0, speed))

    # Control de rotación
    if keys[pygame.K_LEFT]:
        angle += rotation_speed
    elif keys[pygame.K_RIGHT]:
        angle -= rotation_speed

    # Actualizar la posición del triángulo
    rad_angle = math.radians(angle)
    x += speed * math.cos(rad_angle)
    y -= speed * math.sin(rad_angle)

    # Aplicar aritmética modular para mantener el triángulo dentro de la ventana
    x %= screen_width
    y %= screen_height

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Rotar y dibujar el triángulo en la nueva posición
    rotated_triangle, triangle_rect = rotate_triangle(triangle_surface, angle, x, y)
    screen.blit(rotated_triangle, triangle_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
