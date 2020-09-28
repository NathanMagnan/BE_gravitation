## Imports

import numpy as np
import math as m
import pickle

import sys
import os
sys.path.append('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/BE_gravitation')
import functions as functions

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex = True)

print("all imports successful")

## Plotting F(x) / F(1)

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

## Drawing / Loading the abacus of light geodesics

draw_anyway = False

# we test if the abacus has already been drawn
try:
    my_path = os.path.abspath('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/BE_gravitation/')
    
    my_file = 'Abacus_1' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_1 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_1_support' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_1_support = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_2 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2_support' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_2_support = pickle.load(f)
    f.close()
    
    print("Abacus found")
    draw = False
except:
    print("Abacus missing !")
    draw  = True

# we test if we want to draw the abacus anyway
if draw_anyway:
    draw = True

# if necessary , we draw the abacus
Inclinaison = np.linspace(0.01, m.pi / 2 - 0.01, 50)
Alpha = np.linspace(- m.pi / 2 + 0.01, m.pi / 2 - 0.01, 200, endpoint=True)

if draw:    
    functions.abacus(Inclinaison, Alpha)
    my_path = os.path.abspath('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/BE_gravitation/')
    
    my_file = 'Abacus_1' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_1 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_1_support' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_1_support = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_2 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2_support' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_2_support = pickle.load(f)
    f.close()

## Plotting the redshift map

fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (6, 5))
plt.suptitle("Redshift map for a disk between $3 r_{s}$ and $5 r_{s}$, with $i = \pi / 20$")
axes.set_xlabel("$x / r_{s}$")
axes.set_ylabel("$y / r_{s}$")
axes.set_xlim(-5, 5)
axes.set_ylim(-5, 5)

Whole_alpha = np.concatenate(((-m.pi - Alpha[:50])[::-1], Alpha, (m.pi - Alpha[50:])[::-1]), axis = 0)
Whole_inclinaison = np.concatenate((Inclinaison, (m.pi - Inclinaison)[::-1]), axis = 0)
inclinaison = Whole_inclinaison[5]

R_d = np.linspace(3, 5, 10) # this is actually r_d / r_s

cmap = 'gist_rainbow_r'
norm = mpl.colors.Normalize(vmin = -1, vmax = 1)

# secondary images
for r_d in R_d:
    X, Y, Z = functions.read_abacus_redshift(inclinaison, r_d, Whole_alpha, Abacus_2, Abacus_2_support)
    line = axes.scatter(x = X, y = Y, c = Z, cmap = cmap, norm = norm)

# primary images
for r_d in R_d:
    X, Y, Z = functions.read_abacus_redshift(inclinaison, r_d, Whole_alpha, Abacus_1, Abacus_1_support)
    line = axes.scatter(x = X, y = Y, c = Z, cmap = cmap, norm = norm)

cbar = axes.figure.colorbar(line, ax = axes)
cbar.ax.set_ylabel("$z$")

plt.show()
    