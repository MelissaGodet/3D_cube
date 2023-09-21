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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_PLUS:
                cube = cube.apply_scaling(Vec3(1.2, 1.2, 1.2))
            if event.key == pygame.K_KP_MINUS:
                cube = cube.apply_scaling(Vec3(1/1.2, 1/1.2, 1/1.2))
            if event.key == pygame.K_LEFT:
                cube = cube.apply_translation(Vec3(-0.5, 0, 0))
            if event.key == pygame.K_RIGHT:
                cube = cube.apply_translation(Vec3(0.5, 0, 0))
            if event.key == pygame.K_UP:
                cube = cube.apply_translation(Vec3(0, -0.5, 0))
            if event.key == pygame.K_DOWN:
                cube = cube.apply_translation(Vec3(0, 0.5, 0))
            if event.key == pygame.K_q:
                cube = cube.apply_rotation(Vec3(0, 1, 0), speed)
            if event.key == pygame.K_d:
                cube = cube.apply_rotation(Vec3(0, 1, 0), -speed)
            if event.key == pygame.K_z:
                cube = cube.apply_rotation(Vec3(1, 0, 0), -speed)
            if event.key == pygame.K_s:
                cube = cube.apply_rotation(Vec3(1, 0, 0), speed)

    window.fill(background)
    scene.render(window, cube)
    pygame.display.flip()


