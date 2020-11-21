import matplotlib.pyplot as plt
from numpy import *


def f(t, degree):
    return t ** degree * exp(-t ** 2)


t = linspace(0, 3, 51)
y1 = f(t, 2)
y2 = f(t, 4)

plt.plot(t, y1, 'm--', label='t^2*exp(-t^2)')
plt.plot(t, y2, 'k', label='t^4*exp(-t^2)')

plt.xlabel('t')
plt.ylabel('y')
plt.title('My first normal plot')
plt.legend()

plt.show()
