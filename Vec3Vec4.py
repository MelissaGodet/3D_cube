from math import sqrt


class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        if self.x == 0 and self.y == 0 and self.z == 0:
            raise ValueError("The null vector can't be normalize")
        xn, yn, zn = self.x / self.length(), self.y / self.length(), self.z / self.length()
        return Vec3(xn, yn, zn)

    def neg(self):
        xn, yn, zn = -self.x, -self.y, -self.z
        return Vec3(xn, yn, zn)

    def mul(self, k):
        xm, ym, zm = self.x * k, self.y * k, self.z * k
        return Vec3(xm, ym, zm)

    def add(self, v):
        if isinstance(v, Vec3):
            xa, ya, za = self.x + v.x, self.y + v.y, self.z + v.z
            return Vec3(xa, ya, za)
        else:
            raise ValueError("The vector can only do an addition with an other 3D vector")

    def sub(self, v):
        if isinstance(v, Vec3):
            xa, ya, za = self.x - v.x, self.y - v.y, self.z - v.z
            return Vec3(xa, ya, za)
        else:
            raise ValueError("The vector can only do a subdivision with an other 3D vector")

    def dot(self, v):
        if isinstance(v, Vec3):
            dp = self.x * v.x + self.y * v.y + self.z * v.z
            return dp
        else:
            raise ValueError("The vector needs to be a 3D vector")

    def cross(self, v):
        if isinstance(v, Vec3):
            cpx, cpy, cpz = self.y * v.z - self.z * v.y, self.z * v.x - self.x * v.z, self.x * v.y - self.y * v.x
            return Vec3(cpx, cpy, cpz)

        else:
            raise ValueError("The vector can only do a subdivision with an other 3D vector")

    def print(self):
        print("[" + str(self.x) + "," + str(self.y) + "," + str(self.z) + "]\n")

    def cart2hom(self):
        return Vec4(self.x, self.y, self.z, 1)

    def apply_pipeline(self, model, scene):
        homogenous = self.cart2hom()
        v_mod = model.mul_vect(homogenous)
        v_proj = scene.projection.mul_vect(v_mod)
        v = scene.viewport.mul_vect(v_proj)
        return v


class Vec4:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def hom2cart(self):
        if self.w != 0:
            return Vec3(self.x / self.w, self.y / self.w, self.z / self.w)
        else:
            return Vec3(self.x, self.y, self.z)

    def print(self):
        print("[" + str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(
            self.w) + "]\n")
