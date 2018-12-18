import matplotlib.pyplot as plt
import numpy as np

a = 1
b1 = 0.97
b2 = 0.91
zs = -0.74
zm = -0.77

b3 = ((zs - zm) ** 2 + (b2 ** 2 / zs - zs) * (zs - zm)) / \
     (b2 ** 2 / zs + zs - 2 * zm)
a3 = b3 * a / b2 * np.sqrt(zs / (zs - zm - b3))
c = zm + b3


def curve1(z):
    return a * np.sqrt(1 - z ** 2 / b1 ** 2)


def curve2(z):
    return a * np.sqrt(1 - z ** 2 / b2 ** 2)


def curve3(z):
    return a3 * np.sqrt(1 - (z - c) ** 2 / b3 ** 2)

z1 = np.linspace(0, b1, 1000)
z2 = np.linspace(zs, 0, 1000)
z3 = np.linspace(zm, zs, 10000)

x1 = curve1(z1)
x2 = curve2(z2)
x3 = curve3(z3)

plt.axis("equal")
plt.plot(x1, z1, "r")
plt.plot(x2, z2, "b")
plt.plot(x3, z3, "g")
plt.plot(-x1, z1, "r")
plt.plot(-x2, z2, "b")
plt.plot(-x3, z3, "g")
plt.savefig("sim_dropshape.png")
