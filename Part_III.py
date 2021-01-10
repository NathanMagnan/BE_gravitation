## Imports
import numpy as np
import math as m
import pickle
import functions as functions
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex = True)

print("all imports successful")

""" All number will start with small letters (a, b, c). All vectors or lists will start by a capital letter (A, B, C)"""

## Parameters
draw_anyway = False # Drawing / Loading the abacus of light geodesics
Inclinaison = np.linspace(0.01, m.pi / 2 - 0.01, 50)
Whole_inclinaison = np.concatenate((Inclinaison, (m.pi - Inclinaison)[::-1]), axis = 0)
inclinaison = Whole_inclinaison[5] # inclinaison of the disk
inclination_latex = "$i = \pi / 20$" # latex legend for the inclinaison

## Plotting F(x) / F(1)

plt.figure(figsize = (6, 6))
plt.title("Flux emmited by the disk, as a function of radius")
plt.xlabel("$x$")
plt.ylabel("$F_{emitted}(x) / F_{0}$")
plt.yscale('log')
plt.xlim(3, 5)

X = np.linspace(3.01, 5, 100)
Y = functions.flux(X)

plt.plot(X, Y, 'k')
plt.show()

# we test if the abacus has already been drawn
try:
    my_file = 'Abacus_1' + '.pkl'
    f = open(my_file, "rb")
    Abacus_1 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_1_support' + '.pkl'
    f = open(my_file, "rb")
    Abacus_1_support = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2' + '.pkl'
    f = open(my_file, "rb")
    Abacus_2 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2_support' + '.pkl'
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
Alpha = np.linspace(- m.pi / 2 + 0.01, m.pi / 2 - 0.01, 200, endpoint=True)

if draw:    
    functions.abacus(Inclinaison, Alpha)
    
    my_file = 'Abacus_1' + '.pkl'
    f = open(my_file, "rb")
    Abacus_1 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_1_support' + '.pkl'
    f = open(my_file, "rb")
    Abacus_1_support = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2' + '.pkl'
    f = open(my_file, "rb")
    Abacus_2 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2_support' + '.pkl'
    f = open(my_file, "rb")
    Abacus_2_support = pickle.load(f)
    f.close()

## Plotting the redshift map

fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (6, 5))
plt.suptitle("Redshift map for a disk between $3 r_{s}$ and $5 r_{s}$, with " + inclination_latex + ".")
axes.set_xlabel("$x / r_{s}$")
axes.set_ylabel("$y / r_{s}$")
axes.set_xlim(-5, 5)
axes.set_ylim(-5, 5)

Whole_alpha = np.concatenate(((-m.pi - Alpha[:50])[::-1], Alpha, (m.pi - Alpha[50:])[::-1]), axis = 0)

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

## Plotting the final map

fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (5, 5))
plt.suptitle("Approximate image of an accretion disk between $3 r_{s}$ and $5 r_{s}$, \n around a Schwarzshild Black Hole, seen with " + inclination_latex)
axes.set_xlabel("$x / r_{s}$")
axes.set_ylabel("$y / r_{s}$")
axes.set_xlim(-5, 5)
axes.set_ylim(-5, 5)
axes.set_facecolor('black')

Whole_alpha = np.concatenate(((-m.pi - Alpha[:50])[::-1], Alpha, (m.pi - Alpha[50:])[::-1]), axis = 0)

R_d = np.linspace(3, 5, 10) # this is actually r_d / r_s

cmap = 'Greys_r'
norm = mpl.colors.Normalize(vmin = 0, vmax = 2 * 10**(-3))

# secondary images
for r_d in R_d:
    X, Y, Z = functions.read_abacus_flux(inclinaison, r_d, Whole_alpha, Abacus_2, Abacus_2_support)
    line = axes.scatter(x = X, y = Y, c = Z, cmap = cmap, norm = norm)

# primary images
for r_d in R_d:
    X, Y, Z = functions.read_abacus_flux(inclinaison, r_d, Whole_alpha, Abacus_1, Abacus_1_support)
    line = axes.scatter(x = X, y = Y, c = Z, cmap = cmap, norm = norm)

plt.show()