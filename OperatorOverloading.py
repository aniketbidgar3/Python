class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, x):
        return Vector(self.i+x.i, self.j+x.j, self.k+x.k)

    def __sub__(self, x):
        return Vector(self.i-x.i, self.j-x.j, self.k-x.k)

    def __str__(self):
        return (f"{self.i}i + {self.j}j + {self.k}k")


v1 = Vector(2, 3, 4)
print(v1)
v2 = Vector(3, 4, 5)
print(v2)

v3 = v1 + v2
print("Addition : ", v3)

v3 = v2 - v1
print("Substraction : ", v3)
