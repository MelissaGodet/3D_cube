import sys
import pygame
from Scene import Scene
from Mat4 import Mat4, identity
from TriangleMesh import TriangleMesh
from Vec3Vec4 import Vec3

pygame.init()
width = 800
height = 800
window = pygame.display.set_mode((width, height))
background = (0, 0, 0)
window.fill(background)

cube = TriangleMesh(identity())
scene = Scene(width, height)
v = Vec3(1, 0, 0)
v.apply_pipeline(identity(), scene)
speed = 0.05
keys_pressed = {
    pygame.K_KP_PLUS: False,
    pygame.K_KP_MINUS: False,
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_UP: False,
    pygame.K_DOWN: False,
    pygame.K_q: False,
    pygame.K_d: False,
    pygame.K_z: False,
    pygame.K_s: False
}
last_action_time = 0
action_delay = 50
while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
        if event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed[event.key] = False

    window.fill(background)

    # Vérifiez le délai entre chaque exécution de l'action
    if current_time - last_action_time >= action_delay:
        if keys_pressed[pygame.K_KP_PLUS]:
            cube = cube.apply_scaling(Vec3(1.2, 1.2, 1.2))
        if keys_pressed[pygame.K_KP_MINUS]:
            cube = cube.apply_scaling(Vec3(1/1.2, 1/1.2, 1/1.2))
        if keys_pressed[pygame.K_LEFT]:
            cube = cube.apply_translation(Vec3(-0.5, 0, 0))
        if keys_pressed[pygame.K_RIGHT]:
            cube = cube.apply_translation(Vec3(0.5, 0, 0))
        if keys_pressed[pygame.K_UP]:
            cube = cube.apply_translation(Vec3(0, -0.5, 0))
        if keys_pressed[pygame.K_DOWN]:
            cube = cube.apply_translation(Vec3(0, 0.5, 0))
        if keys_pressed[pygame.K_q]:
            cube = cube.apply_rotation(Vec3(0, 1, 0), speed)
        if keys_pressed[pygame.K_d]:
            cube = cube.apply_rotation(Vec3(0, 1, 0), -speed)
        if keys_pressed[pygame.K_z]:
            cube = cube.apply_rotation(Vec3(1, 0, 0), -speed)
        if keys_pressed[pygame.K_s]:
            cube = cube.apply_rotation(Vec3(1, 0, 0), speed)

        # Mettez à jour le moment de la dernière exécution de l'action
        last_action_time = current_time

    scene.render(window, cube)
    pygame.display.flip()

