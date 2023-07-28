from built_modules import import_matrices as mat
import math

t = math.pi / 4
a = [[1, 0, 0],
     [0, math.cos(t), math.sin(t)],
     [0, -math.sin(t), math.cos(t)]]
b = [[math.cos(t), 0, math.sin(t)],
     [0, 1, 0],
     [-math.sin(t), 0, math.cos(t)]]
c = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

for i in range(round(math.pi / t)):
     c = mat.mult(a, c)
     c = mat.mult(b, c)

for i in range(3):
     for j in range(3):
          c[i][j] = round(c[i][j], 6)
     print(c[i])

c = [[1, 0, 0],
     [0, 0, 1],
     [0, -1, 0]]

for i in mat.mult(c, c):
     print(i)