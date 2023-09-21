import math

import pygame

from Mat4 import Mat4
from ScreenTriangle import ScreenTriangle
from Vec3Vec4 import Vec3


class TriangleMesh:
    def __init__(self, model):
        vertices = [
            Vec3(-1, -1, -1),
            Vec3(-1, -1, 1),
            Vec3(-1, 1, -1),
            Vec3(-1, 1, 1),
            Vec3(1, -1, -1),
            Vec3(1, -1, 1),
            Vec3(1, 1, -1),
            Vec3(1, 1, 1),
        ]

        faces = [
            [0, 1, 2],
            [1, 3, 2],
            [2, 3, 7],
            [2, 7, 6],
            [1, 7, 3],
            [1, 5, 7],
            [4, 6, 7],
            [4, 7, 5],
            [0, 5, 1],
            [0, 4, 5],
            [0, 2, 6],
            [0, 6, 4]
        ]

        self.vertices = vertices
        self.faces = faces
        self.model = model

    def apply_rotation(self, axis: Vec3, angle):
        m = rotation_matrix(axis, angle)
        return TriangleMesh(m.mul_mat(self.model))

    def apply_translation(self, trans_vec):
        m = translation_matrix(trans_vec)
        return TriangleMesh(m.mul_mat(self.model))

    def apply_scaling(self, scale_vec):
        m = scaling_matrix(scale_vec)
        return TriangleMesh(m.mul_mat(self.model))

    def draw_mesh(self, window, scene):
        for face in self.faces:
            draw_face(window, face, self.vertices, self.model, scene)


def translation_matrix(trans_vec):
    return Mat4([
        [1, 0, 0, trans_vec.x],
        [0, 1, 0, trans_vec.y],
        [0, 0, 1, trans_vec.z],
        [0, 0, 0, 1]
    ])


def rotation_matrix(axis, angle):
    x, y, z = axis.normalize().x, axis.normalize().y, axis.normalize().z
    c = math.cos(angle)
    s = math.sin(angle)
    t = 1 - c

    return Mat4([
        [t * x * x + c, t * x * y - s * z, t * x * z + s * y, 0],
        [t * x * y + s * z, t * y * y + c, t * y * z - s * x, 0],
        [t * x * z - s * y, t * y * z + s * x, t * z * z + c, 0],
        [0, 0, 0, 1]
    ])


def scaling_matrix(scale_vec):
    return Mat4([
        [scale_vec.x, 0, 0, 0],
        [0, scale_vec.y, 0, 0],
        [0, 0, scale_vec.z, 0],
        [0, 0, 0, 1]
    ])


def draw_face(window, face, vertices, model, scene):
    n = 3
    for i in range(n):
        v1, v2, v3 = vertices[face[0]].apply_pipeline(model, scene), vertices[face[1]].apply_pipeline(model, scene), \
        vertices[face[2]].apply_pipeline(model, scene)
        t = ScreenTriangle(v1, v2, v3)
        t.draw(window)
