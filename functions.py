## Imports

import numpy as np
import scipy.integrate as sc
import math as m

import os
import pickle

""" All number will start with small letters (a, b, c). All vectors or lists will start by a capital letter (A, B, C)"""

## Support functions

def propagator(U, t): # we define the differential equation
    u, up = U[0], U[1]
    return np.asarray([up, 3/2 * u**2 - u])

def r_s(b, Theta): # gives the radius as a function of angle, for a given impact paramter
    u, up = 0, (3**(3/2) / 2 * b)**(-1) # initial conditions
    
    U = sc.odeint(propagator, np.asarray([u, up]), Theta) # solution of the differential equation
    
    U_corrected = U[:, 0].copy() # we only keep the positions, and we remove the derivatives
    
    test = True # we remove the points that have no physical meaning, and where the integrator might have made rounding mistakes
    Zeros = np.zeros(len(Theta))
    Ones = np.ones(len(Theta))
    j = 1
    while (test and j < len(Theta)):
        if (U_corrected[j] <= 0):
            U_corrected[j:] = Zeros[j:]
            test = False
        if (U_corrected[j] >= 1):
            U_corrected[j:] = Ones[j:]
            test = False
        j += 1
    
    R = 1 / U_corrected # we translate from u to r / r_s
    return(R)

def abacus(Inclinaison, Alpha):
    Abacus_1 = {} # will store the primary images
    Abacus_1_support = {}
    Abacus_2 = {} # will store the secondary images
    Abacus_2_support = {}
    for i in Inclinaison:
        for alpha in Alpha:
            Abacus_1_support[(i, alpha)] = []
            Abacus_2_support[(i, alpha)] = []
    
    Theta = np.linspace(0, 2 * m.pi, 10000, endpoint=False) # For the numerical integration
    B = np.linspace(0, 2, 100) # for the abacus
    
    for b in B:
        R = r_s(b, Theta)
            
        for i in Inclinaison:
            for alpha in Alpha:
                """primary image"""
                theta_d = np.arccos(- np.sin(alpha) * np.cos(i) / np.sqrt(1 - np.cos(alpha)**2 * np.cos(i)**2)) # primary image's theta_d
                index = int(len(Theta) * theta_d / (2 * m.pi)) # index of this theta_d in the list Theta
                r_d = R[index] # r_d corresponding to this (b, theta_d)
                
                Abacus_1[(i, r_d, alpha)] = b
                Abacus_1_support[(i, alpha)].append(r_d)
                
                """secondary image, which might not exist"""
                #try :
                theta_d = (np.arccos(- np.sin(alpha) * np.cos(i) / np.sqrt(1 - np.cos(alpha)**2 * np.cos(i)**2)) + m.pi) % (2 * m.pi)
                index = int(len(Theta) * theta_d / (2 * m.pi))
                r_d = R[index]
                
                Abacus_2[(i, r_d, alpha)] = b
                Abacus_2_support[(i, alpha)].append(r_d)
                #except:
                    #continue
    
    # saving the data
    my_path = os.path.abspath('C:/Users/Nathan/Documents/E - Toulouse/Cours/Gravitation/BE/')
    
    my_file = 'Abacus_1' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "wb")
    pickle.dump(Abacus_1, f)
    f.close()
    
    my_file = 'Abacus_1_support' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "wb")
    pickle.dump(Abacus_1_support, f)
    f.close()
    
    my_file = 'Abacus_2' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "wb")
    pickle.dump(Abacus_2, f)
    f.close()
    
    my_file = 'Abacus_2_support' + '.pkl'
    my_file = os.path.join(my_path, my_file)
    f = open(my_file, "wb")
    pickle.dump(Abacus_2_support, f)
    f.close()

def read_abacus(i, r_d, Alpha, Abacus, Abacus_support):
    X = []
    Y = []
    
    for alpha in Alpha:
        Acceptable_rd = np.sort(Abacus_support[(i, alpha)])
        
        j = 0 # we look for the r_d in the abacus that is the closest to the goal
        while ((Acceptable_rd[j] < r_d) and (j < len(Acceptable_rd) - 1)):
            j += 1
        
        try : # we try to make a linear interpolation between the two closest r_d. If that is not possible, we take the closest r_d
            r1 = Acceptable_rd[j - 1]
            r2 = Acceptable_rd[j]
            b1 = Abacus[(i, r1, alpha)]
            b2 = Abacus[(i, r2, alpha)]
            b = b2 * (r_d - r1) / (r2 - r1) + b1 * (r2 - r_d) / (r2 - r1)
        except:
            r = Acceptable_rd[j]
            b = Abacus[(i, r, alpha)]
        
        b = b * 3**(3/2) / 2 # translation from b / b_c to b / r_s, which makes more sense from a physics perspective
        
        x, y = np.cos(alpha) * b, np.sin(alpha) * b # translation from (alpha, b) to (x, y) in the observer's plane
        X.append(x)
        Y.append(y)
    
    return(X, Y)