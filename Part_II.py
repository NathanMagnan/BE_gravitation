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
plt.suptitle("Iso-radius for an observer at infinity. $i = \pi / 20$")
plt.title("solid lines = primary images, dashed lines = secondary images")
plt.xlabel("$x / r_{s}$")
plt.ylabel("$y / r_{s}$")
plt.xlim(-5, 5)
plt.ylim(-5, 5)

inclinaison = Inclinaison[5]

R_d = [1.1, 1.5, 2, 2.5, 3] # actually this is r_d / r_s
Colors = ['b', 'g', 'y', 'orange', 'r']
Labels = ['$r_{d} / r_{s} = 1.1$', '$r_{d} / r_{s} = 1.5$', '$r_{d} / r_{s} = 2$', '$r_{d} / r_{s} = 2.5$', '$r_{d} / r_{s} = 3$']

j = 0
for r_d in R_d:
    X, Y = functions.read_abacus(inclinaison, r_d, Alpha, Abacus_1, Abacus_1_support)
    plt.plot(X, Y, color = Colors[j], label = Labels[j])
    
    X, Y = functions.read_abacus(inclinaison, r_d, Alpha, Abacus_2, Abacus_2_support)
    plt.plot(X, Y, color = Colors[j], linestyle =  '--')
    j += 1

plt.legend()
plt.show()