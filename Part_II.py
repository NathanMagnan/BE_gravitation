## Import
import numpy as np
import math as m
import pickle
import functions as functions
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex = True)

print("All imports successful")

""" All number will start with small letters (a, b, c). All vectors or lists will start by a capital letter (A, B, C)"""

## Parameters
draw_anyway = False # Drawing / Loading the abacus of light geodesics
Inclinaison = np.linspace(0.01, m.pi / 2 - 0.01, 50)
Whole_inclinaison = np.concatenate((Inclinaison, (m.pi - Inclinaison)[::-1]), axis = 0)
inclinaison = Whole_inclinaison[5] # inclinaison of the disk
inclination_latex = "$i = \pi / 20$" # latex legend for the inclinaison
R_d = [1.1, 1.5, 2, 2.5, 3, 4] # actually this is r_d / r_s
Colors = ['b', 'g', 'y', 'orange', 'r', 'purple'] # colors associated with R_d
Labels = ['$r_{d} / r_{s} = 1.1$', '$r_{d} / r_{s} = 1.5$', '$r_{d} / r_{s} = 2$', '$r_{d} / r_{s} = 2.5$', '$r_{d} / r_{s} = 3$', '$r_{d} / r_{s} = 4$'] # labels associated with R_d

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

## Plotting the iso-radius

plt.figure(figsize = (6, 6))
plt.suptitle("Iso-radius for an observer at infinity. " + inclination_latex)
plt.title("solid lines = primary images, dashed lines = secondary images")
plt.xlabel("$x / r_{s}$")
plt.ylabel("$y / r_{s}$")
plt.xlim(-5, 5)
plt.ylim(-5, 5)

Whole_alpha = np.concatenate(((-m.pi - Alpha[:50])[::-1], Alpha, (m.pi - Alpha[50:])[::-1]), axis = 0)

j = 0
for r_d in R_d:
    X, Y = functions.read_abacus(inclinaison, r_d, Whole_alpha, Abacus_1, Abacus_1_support)
    plt.plot(X, Y, color = Colors[j], label = Labels[j])
    
    X, Y = functions.read_abacus(inclinaison, r_d, Whole_alpha, Abacus_2, Abacus_2_support)
    plt.plot(X, Y, color = Colors[j], linestyle =  '--')
    j += 1

plt.legend()
plt.show()