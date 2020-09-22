## Import

import numpy as np

import sys
import os
sys.path.append('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/B_gravitationE')
import functions as functions

import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex = True)

print("All imports successful")

""" All number will start with small letters (a, b, c). All vectors or lists will start by a capital letter (A, B, C)"""

## Question I.c

plt.figure(figsize = (6, 6))
plt.title("Light geodesics for a Schwazschild black hole")
plt.xlabel("$x / r_{s}$")
plt.ylabel("$y / r_{s}$")
plt.xlim(-5, 5)
plt.ylim(-5, 5)

B = [0.1, 0.5, 0.999, 1.001, 1.5, 2] # this actually b / bc, or b if bc = 1
Colors = ['grey', 'b', 'g', 'y', 'orange', 'r']
Labels = ['$b / b_{c}$ = 0.1','$b / b_{c}$ = 0.5', '$b / b_{c}$ = 0.999', '$b / b_{c}$ = 1.001', '$b / b_{c}$ = 1.5', '$b / b_{c}$ = 2']

Theta = np.linspace(0, 4 * 2 * m.pi, 1000) # these will be the angles, expressed in radians. We need them to integrate the equation

i = 0
for b in B:
    R = functions.r_s(b, Theta)
    X, Y = R * np.cos(Theta), R * np.sin(Theta)
    
    plt.plot(X, Y, color = Colors[i], label = Labels[i])
    i += 1

plt.scatter([0], [0], color = 'black', label = 'BH center')
X, Y = np.cos(Theta), np.sin(Theta)
plt.plot(X, Y, 'k', label = '$R_{s}$')

plt.legend()
plt.show()