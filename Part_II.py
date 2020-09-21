## Import

import numpy as np
import math as m

import pickle

import sys
import os
sys.path.append('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/BE')
import functions as functions

import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex = True)

print("All imports successful")

""" All number will start with small letters (a, b, c). All vectors or lists will start by a capital letter (A, B, C)"""

## Drawing / Loading the abacus of light geodesics

draw_anyway = False

# we test if the abacus has already been drawn
try:
    my_path = os.path.abspath('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/BE/')
    
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
Inclinaison = np.linspace(0.01, m.pi - 0.01, 100)
Alpha = np.linspace(0.01, 2 * m.pi + 0.01, 100, endpoint=True)

if draw:    
    functions.abacus(Inclinaison, Alpha)
    my_path = os.path.abspath('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/BE/')
    
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

## Plotting the iso-radius

plt.figure(figsize = (6, 6))
plt.suptitle("Iso-radius for an observer at infinity. $r_{d} = 3 r_{s}$")
plt.title("(primary images only)")
plt.xlabel("$x / r_{s}$")
plt.ylabel("$y / r_{s}$")
plt.xlim(-5, 5)
plt.ylim(-5, 5)

r_d = 3 # actually this is r_d / r_s

Inclinaisons = [Inclinaison[5], Inclinaison[25], Inclinaison[50], Inclinaison[75], Inclinaison[95]]
Colors = ['b', 'g', 'y', 'orange', 'r']
Labels = ['$i = \epsilon$', '$i = \pi / 4$', '$i = \pi / 2$', '$i = 3 \pi / 4$', '$i = \pi - \epsilon$']

j = 0
for inclinaison in Inclinaisons:
    X, Y = functions.read_abacus(inclinaison, r_d, Alpha, Abacus_1, Abacus_1_support)
    plt.plot(X, Y, color = Colors[j], label = Labels[j])
    j += 1

plt.legend()
plt.show()