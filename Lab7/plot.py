import matplotlib.pyplot as plt
from numpy import *
import numpy as np


def f(t):
    return 5 * np.cos(10 * t) * np.sin(3 * t) / exp(t ** (1 / 2))


t = np.arange(0, 5, 0.01)
y = f(t)

plt.plot(t, y, 'm')

plt.xlabel('t')
plt.ylabel('y')
plt.title('Y(x)=5*cos(10*x)*sin(3*x)/(x^(1/2)), x=[0...5]')

plt.show()
