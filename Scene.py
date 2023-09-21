from Mat4 import Mat4


class Scene:
    def __init__(self, screen_width, screen_height):
        self.projection = self.projection_matrix()
        self.viewport = self.viewport_matrix(screen_width, screen_height)

    def viewport_matrix(self, screen_width, screen_height):
        originX = 0
        originY = 0
        nearDepth = 0
        farDepth = 1
        viewportMatrix = Mat4([
            [screen_width / 2, 0, 0, originX + screen_width / 2],
            [0, screen_height / 2, 0, originY + screen_height / 2],
            [0, 0, (farDepth - nearDepth) / 2, (nearDepth + farDepth) / 2 ],
            [0, 0, 0, 1]]
        )
        return viewportMatrix

    def projection_matrix(self):
        left = -2
        right = 2
        top = 2
        bottom = -2
        near = 0.1
        far = 1000

        mat = Mat4([
            [2 / (right - left), 0, 0, -(right + left) / (right - left)],
            [0, 2 / (top - bottom), 0, -(top + bottom) / (top - bottom)],
            [0, 0, -2 / (far - near), -(far + near) / (far - near)],
            [0, 0, 0, 1]]
        )

        return mat

    def render(self, window, triangle_mesh):
        triangle_mesh.draw_mesh(window, self)
