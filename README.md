Triángulo en movimiento con Pygame

Default (GPT-3.5)

User
genera un codigo en python que usando pygame genere un triangulo en constante movimiento que al presionar las teclas arriba y abajo aumente y disminuya su velocidad, y al presionar las teclas de los lados gire  

ChatGPT
Claro, aquí tienes un ejemplo de código en Python que utiliza Pygame para crear un triángulo en constante movimiento que puedes controlar con las teclas de flecha arriba, abajo, izquierda y derecha para ajustar su velocidad y rotación:

python
Copy code
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

    # Control de rotación
    if keys[pygame.K_LEFT]:
        angle += rotation_speed
    elif keys[pygame.K_RIGHT]:
        angle -= rotation_speed

    # Actualizar la posición del triángulo
    rad_angle = math.radians(angle)
    x += speed * math.cos(rad_angle)
    y -= speed * math.sin(rad_angle)

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Rotar y dibujar el triángulo en la nueva posición
    rotated_triangle, triangle_rect = rotate_triangle(triangle_surface, angle, x, y)
    screen.blit(rotated_triangle, triangle_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
Este código crea una ventana de Pygame y dibuja un triángulo en ella. Puedes controlar la velocidad de movimiento con las teclas arriba y abajo, y la rotación con las teclas izquierda y derecha. El triángulo se mueve en la dirección en la que está apuntando. ¡Espero que te sea útil!




User
al ejemplo anterior añadele limites en la ventana para evitar perder de vista el triangulo

ChatGPT
Claro, aquí tienes una versión modificada del código que incluye límites en la ventana para evitar que el triángulo salga de la vista:

python
Copy code
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

    # Control de rotación
    if keys[pygame.K_LEFT]:
        angle += rotation_speed
    elif keys[pygame.K_RIGHT]:
        angle -= rotation_speed

    # Actualizar la posición del triángulo
    rad_angle = math.radians(angle)
    x += speed * math.cos(rad_angle)
    y -= speed * math.sin(rad_angle)

    # Limitar el movimiento dentro de la ventana
    x = max(triangle_width / 2, min(x, screen_width - triangle_width / 2))
    y = max(triangle_height / 2, min(y, screen_height - triangle_height / 2))

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Rotar y dibujar el triángulo en la nueva posición
    rotated_triangle, triangle_rect = rotate_triangle(triangle_surface, angle, x, y)
    screen.blit(rotated_triangle, triangle_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
Ahora, el triángulo no puede salir de la ventana y se detendrá en los límites de la ventana cuando intentes moverlo más allá.




User
al codigo anterior elimina los limites y agrega aritmetica modular

ChatGPT
Claro, puedes utilizar aritmética modular para que el triángulo aparezca en el lado opuesto de la ventana cuando se sale de un borde. Aquí tienes una versión del código que hace eso:

python
Copy code
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
Ahora, cuando el triángulo se sale de un borde de la ventana, aparecerá en el lado opuesto debido al uso de la aritmética modular en las coordenadas x e y.




User
al codigo anterior agrega un limite de velocidad del triangulo igual a 10

ChatGPT
Puedes agregar un límite de velocidad para el triángulo asegurándote de que no supere un valor máximo de velocidad. Aquí tienes la versión actualizada del código con un límite de velocidad máximo de 10:

python
Copy code
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
Ahora el triángulo tiene un límite de velocidad máximo de 10 y no puede exceder ese valor.

