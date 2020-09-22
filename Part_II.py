## Import

import numpy as np
import math as m

import pickle

# import sys
import os
# sys.path.append('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/BE')
import functions as functions

import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex = True)

print("All imports successful")

""" All number will start with small letters (a, b, c). All vectors or lists will start by a capital letter (A, B, C)"""

# Save figure in this file ; can be None

save_fig = "2.1_0.05pi.png"

# Draw the event horizon in the center

draw_bh = True

## Drawing / Loading the abacus of light geodesics

draw_anyway = True

# we test if the abacus has already been drawn
try:
    # my_path = os.path.abspath('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/BE/')
    
    my_file = 'Abacus_1' + '.pkl'
    # my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_1 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_1_support' + '.pkl'
    # my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_1_support = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2' + '.pkl'
    # my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_2 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2_support' + '.pkl'
    # my_file = os.path.join(my_path, my_file)
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
# Inclinaison = np.linspace(0.01, m.pi - 0.01, 100)
Inclinaison = np.array([m.pi/20, m.pi/4, m.pi/2])
Alpha = np.linspace(0.01, 2 * m.pi + 0.01, 10000, endpoint=True)

if draw:    
    functions.abacus(Inclinaison, Alpha)
    # my_path = os.path.abspath('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/BE/')
    
    my_file = 'Abacus_1' + '.pkl'
    # my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_1 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_1_support' + '.pkl'
    # my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_1_support = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2' + '.pkl'
    # my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_2 = pickle.load(f)
    f.close()
    
    my_file = 'Abacus_2_support' + '.pkl'
    # my_file = os.path.join(my_path, my_file)
    f = open(my_file, "rb")
    Abacus_2_support = pickle.load(f)
    f.close()

## Plotting the iso-radius

if save_fig is not None:
    fig = plt.figure(dpi = 200, figsize=[12.8, 12.8], tight_layout=True, clear=True)
    plt.rcParams.update({'font.size': 22})
else:
    fig = plt.figure(figsize = (6, 6))
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
plt.suptitle("Iso-radius for an observer at infinity. $i = \pi / 20$")
plt.title("solid lines = primary images, dashed lines = secondary images")
plt.xlabel("$x / r_{s}$")
plt.ylabel("$y / r_{s}$")
plt.xlim(-6, 6)
plt.ylim(-6, 6)

if draw_bh:
    circle1=plt.Circle((0,0),1,color='black')
    ax.add_artist(circle1)

inclinaison = Inclinaison[0]

R_d = [1.1, 1.5, 2, 2.5, 3, 5] # actually this is r_d / r_s
Colors = ['b', 'g', 'y', 'orange', 'r', 'purple']
Labels = ['$r_{d} / r_{s} = 1.1$', '$r_{d} / r_{s} = 1.5$', '$r_{d} / r_{s} = 2$', '$r_{d} / r_{s} = 2.5$', '$r_{d} / r_{s} = 3$', '$r_{d} / r_{s} = 5$']

j = 0
for r_d in R_d:
    X, Y = functions.read_abacus(inclinaison, r_d, Alpha, Abacus_1, Abacus_1_support)
    plt.plot(X, Y, color = Colors[j], label = Labels[j])
    
    X, Y = functions.read_abacus(inclinaison, r_d, Alpha, Abacus_2, Abacus_2_support)
    plt.plot(X, Y, color = Colors[j], linestyle =  '--')
    j += 1

plt.legend()
if save_fig is not None:
    plt.savefig(save_fig)
plt.show()