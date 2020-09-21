## Imports

import numpy as np

import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex = True)

print("all imports successful")

## F(x) / F(1)

def Flux(x):
    a = x**(-5 / 2) / (x - 3 / 2) # I'm pretty sure the bottom of this fraction should be x**(-3/2), but I have to ask the teacher.
    b = np.sqrt(x) - np.sqrt(3)
    c1 = (np.sqrt(x) + np.sqrt(3 / 2)) * (np.sqrt(2) - 1)
    c2 = (np.sqrt(x) - np.sqrt(3 / 2)) * (np.sqrt(2) + 1)
    d = np.sqrt(3/8) * np.log(c1 / c2)
    return(a * (b + d))

plt.figure(figsize = (6, 6))
plt.title("Flux emmited by the disk, as a function of radius")
plt.xlabel("$x$")
plt.ylabel("$F_{emitted}(x) / F_{0}$")
plt.yscale('log')
plt.xlim(1, 5)

X = np.linspace(1, 5, 100)
Y = Flux(X)

plt.plot(X, Y, 'k')
plt.show()