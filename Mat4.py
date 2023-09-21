from Vec3Vec4 import Vec4


class Mat4:
    def __init__(self, matrix):
        if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
            raise ValueError("The matrix must be 4x4")
        else:
            self.matrix = matrix

    def add(self, m):
        n = 4
        mat = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                mat[i][j] = self.matrix[i][j] + m.matrix[i][j]
        return Mat4(mat)

    def mul_scal(self, k):
        n = 4
        mat = [[0 for i in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                mat[i][j] = self.matrix[i][j] * k
        return Mat4(mat)

    def mul_vect(self, v):
        n = 4
        vec = [0, 0, 0, 0]
        v = [v.x, v.y, v.z, v.w]
        for i in range(n):
            for j in range(n):
                vec[i] += self.matrix[i][j] * v[j]  # Voir channel code
        return Vec4(vec[0], vec[1], vec[2], vec[3])

    def mul_mat(self, m):
        n = 4
        mat = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for l in range(n):
                    mat[i][j] += self.matrix[i][l] * m.matrix[l][j]
        return Mat4(mat)

    def adjointe(self):
        n = 4
        adj = []
        for i in range(n):
            adj.append([])
            for j in range(n):
                sm = sub_matrix(self.matrix, j, i)
                cofactor = (-1) ** (i + j) * determinant(sm)
                adj[i].append(cofactor)

        return adj

    def inverse(self):
        n = 4
        det = determinant(self.matrix)
        if det == 0:
            raise ValueError("The matrix doesn't have an inverse")
        adj = self.adjointe()
        mat_inv = []
        for i in range(n):
            mat_inv.append([])
            for j in range(n):
                mat_inv[i].append((1 / det) * adj[i][j])

        return mat_inv

    def print(self):
        n = 4
        for i in range(n):
            print("\n[", end=" ")
            for j in range(n):
                if j != 3:
                    print(str(self.matrix[i][j]) + ", ", end=" ")
                else:
                    print(str(self.matrix[i][j]) + "]", end=" ")
        print("\n")


def identity():
    return Mat4([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])


def sub_matrix(matrix, i: int, j: int):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        raise ValueError("The coefficients are not consistent to generate the sub-matrix")

    sm = []
    for k in range(len(matrix)):
        if k != i:
            sm.append([])
            for l in range(len(matrix[k])):
                if l != j:
                    sm[-1].append(matrix[k][l])

    return sm


def determinant(matrix):
    rows, cols = len(matrix), len(matrix[0])

    if rows != cols:
        raise ValueError("The matrix must be square to calculate the determinant")

    if rows == 2:  # Cas de la matrice 2x2
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        n = len(matrix)
        det = 0
        for i in range(n):
            sub_mat = sub_matrix(matrix, 0, i)
            cofactor = matrix[0][i] * determinant(sub_mat)
            if i % 2 == 0:
                det += cofactor
            else:
                det -= cofactor
        return det

