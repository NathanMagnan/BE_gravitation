## Imports
import numpy as np
import scipy.integrate as sc
import math as m
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
            Abacus_1_support[(round(i, 4), round(alpha, 4))] = []
            Abacus_2_support[(round(i, 4), round(alpha, 4))] = []
    
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
                
                Abacus_1[(round(i, 4), r_d, round(alpha, 4))] = b
                Abacus_1_support[(round(i, 4), round(alpha, 4))].append(r_d)
                
                """secondary image, which might not exist"""
                #try :
                theta_d = (np.arccos(- np.sin(alpha) * np.cos(i) / np.sqrt(1 - np.cos(alpha)**2 * np.cos(i)**2)) + m.pi) % (2 * m.pi)
                index = int(len(Theta) * theta_d / (2 * m.pi))
                r_d = R[index]
                
                Abacus_2[(round(i, 4), r_d, round(alpha, 4))] = b
                Abacus_2_support[(round(i, 4), round(alpha, 4))].append(r_d)
                #except:
                    #continue
    
    # saving the data
    my_file = 'Abacus_1' + '.pkl'
    f = open(my_file, "wb")
    pickle.dump(Abacus_1, f)
    f.close()
    
    my_file = 'Abacus_1_support' + '.pkl'
    f = open(my_file, "wb")
    pickle.dump(Abacus_1_support, f)
    f.close()
    
    my_file = 'Abacus_2' + '.pkl'
    f = open(my_file, "wb")
    pickle.dump(Abacus_2, f)
    f.close()
    
    my_file = 'Abacus_2_support' + '.pkl'
    f = open(my_file, "wb")
    pickle.dump(Abacus_2_support, f)
    f.close()

def read_abacus(i, r_d, Alpha, Abacus, Abacus_support):
    X = []
    Y = []
    
    for alpha in Alpha:
        if (i < m.pi / 2): # we use the symmetry (i, alpha) <-> (pi / 2 - i, alpha + pi)
            true_i = round(i, 4)
            if ((alpha > - m.pi / 2) and (alpha < m.pi / 2)): # we use the symmetry alpha <-> 2 pi - alpha
                true_alpha = round(alpha, 4)
            elif (alpha < - m.pi / 2):
                true_alpha = round(- m.pi - alpha, 4)
            else:
                true_alpha = round(m.pi - alpha, 4)
        else:
            true_i = round(m.pi - i, 4)
            alpha_sym = - alpha
            if ((alpha_sym > - m.pi / 2) and (alpha_sym < m.pi / 2)): # we use the symmetry alpha <-> 2 pi - alpha
                true_alpha = round(alpha_sym, 4)
            elif (alpha_sym < - m.pi / 2):
                true_alpha = round(- m.pi - alpha_sym, 4)
            else:
                true_alpha = round(m.pi - alpha_sym, 4)
                
        Acceptable_rd = np.sort(Abacus_support[(true_i, true_alpha)])
        
        j = 0 # we look for the r_d in the abacus that is the closest to the goal
        while ((Acceptable_rd[j] < r_d) and (j < len(Acceptable_rd) - 1)):
            j += 1
        
        try : # we try to make a linear interpolation between the two closest r_d. If that is not possible, we take the closest r_d
            r1 = Acceptable_rd[j - 1]
            r2 = Acceptable_rd[j]
            b1 = Abacus[(true_i, r1, true_alpha)]
            b2 = Abacus[(true_i, r2, true_alpha)]
            b = b2 * (r_d - r1) / (r2 - r1) + b1 * (r2 - r_d) / (r2 - r1)
        except:
            r = Acceptable_rd[j]
            b = Abacus[(true_i, r, true_alpha)]
        
        b = b * 3**(3/2) / 2 # translation from b / b_c to b / r_s, which makes more sense from a physics perspective
        
        x, y = np.cos(alpha) * b, np.sin(alpha) * b # translation from (alpha, b) to (x, y) in the observer's plane
        X.append(x)
        Y.append(y)
    
    return(X, Y)

def redshift(i, r_d, alpha, b): # takes r_d / r_s as an entry, and gives the redshift as an output
    a = np.sqrt(1 - 3 / (2 * r_d))**(-1)
    b = 1 + (3 / (2 * r_d))**(3 / 2) * b * np.cos(i) * np.cos(alpha)
    return(a * b - 1)

def read_abacus_redshift(i, r_d, Alpha, Abacus, Abacus_support):
    X = []
    Y = []
    Z = []
    
    for alpha in Alpha:
        if (i < m.pi / 2): # we use the symmetry (i, alpha) <-> (pi / 2 - i, alpha + pi)
            true_i = round(i, 4)
            if ((alpha > - m.pi / 2) and (alpha < m.pi / 2)): # we use the symmetry alpha <-> 2 pi - alpha
                true_alpha = round(alpha, 4)
            elif (alpha < - m.pi / 2):
                true_alpha = round(- m.pi - alpha, 4)
            else:
                true_alpha = round(m.pi - alpha, 4)
        else:
            true_i = round(m.pi - i, 4)
            alpha_sym = - alpha
            if ((alpha_sym > - m.pi / 2) and (alpha_sym < m.pi / 2)): # we use the symmetry alpha <-> 2 pi - alpha
                true_alpha = round(alpha_sym, 4)
            elif (alpha_sym < - m.pi / 2):
                true_alpha = round(- m.pi - alpha_sym, 4)
            else:
                true_alpha = round(m.pi - alpha_sym, 4)
                
        Acceptable_rd = np.sort(Abacus_support[(true_i, true_alpha)])
        
        j = 0 # we look for the r_d in the abacus that is the closest to the goal
        while ((Acceptable_rd[j] < r_d) and (j < len(Acceptable_rd) - 1)):
            j += 1
        
        try : # we try to make a linear interpolation between the two closest r_d. If that is not possible, we take the closest r_d
            r1 = Acceptable_rd[j - 1]
            r2 = Acceptable_rd[j]
            b1 = Abacus[(true_i, r1, true_alpha)]
            b2 = Abacus[(true_i, r2, true_alpha)]
            b = b2 * (r_d - r1) / (r2 - r1) + b1 * (r2 - r_d) / (r2 - r1)
        except:
            r = Acceptable_rd[j]
            b = Abacus[(true_i, r, true_alpha)]
        
        z = redshift(i, r_d, alpha, b)
        b = b * 3**(3/2) / 2 # translation from b / b_c to b / r_s, which makes more sense from a physics perspective
        
        x, y = np.cos(alpha) * b, np.sin(alpha) * b # translation from (alpha, b) to (x, y) in the observer's plane
        X.append(x)
        Y.append(y)
        Z.append(z)
        
    return(X, Y, np.asarray(Z))

def flux(r_d): # actually r_d/ r_s
    a = r_d**(-5 / 2) / (r_d - 3 / 2) # I'm pretty sure the bottom of this fraction should be x**(-3/2), but I have to ask the teacher.
    b = np.sqrt(r_d) - np.sqrt(3)
    c1 = (np.sqrt(r_d) + np.sqrt(3 / 2)) * (np.sqrt(2) - 1)
    c2 = (np.sqrt(r_d) - np.sqrt(3 / 2)) * (np.sqrt(2) + 1)
    d = np.sqrt(3/8) * np.log(c1 / c2)
    return(a * (b + d))

def read_abacus_flux(i, r_d, Alpha, Abacus, Abacus_support):
    X = []
    Y = []
    F = []
    
    for alpha in Alpha:
        if (i < m.pi / 2): # we use the symmetry (i, alpha) <-> (pi / 2 - i, alpha + pi)
            true_i = round(i, 4)
            if ((alpha > - m.pi / 2) and (alpha < m.pi / 2)): # we use the symmetry alpha <-> 2 pi - alpha
                true_alpha = round(alpha, 4)
            elif (alpha < - m.pi / 2):
                true_alpha = round(- m.pi - alpha, 4)
            else:
                true_alpha = round(m.pi - alpha, 4)
        else:
            true_i = round(m.pi - i, 4)
            alpha_sym = - alpha
            if ((alpha_sym > - m.pi / 2) and (alpha_sym < m.pi / 2)): # we use the symmetry alpha <-> 2 pi - alpha
                true_alpha = round(alpha_sym, 4)
            elif (alpha_sym < - m.pi / 2):
                true_alpha = round(- m.pi - alpha_sym, 4)
            else:
                true_alpha = round(m.pi - alpha_sym, 4)
                
        Acceptable_rd = np.sort(Abacus_support[(true_i, true_alpha)])
        
        j = 0 # we look for the r_d in the abacus that is the closest to the goal
        while ((Acceptable_rd[j] < r_d) and (j < len(Acceptable_rd) - 1)):
            j += 1
        
        try : # we try to make a linear interpolation between the two closest r_d. If that is not possible, we take the closest r_d
            r1 = Acceptable_rd[j - 1]
            r2 = Acceptable_rd[j]
            b1 = Abacus[(true_i, r1, true_alpha)]
            b2 = Abacus[(true_i, r2, true_alpha)]
            b = b2 * (r_d - r1) / (r2 - r1) + b1 * (r2 - r_d) / (r2 - r1)
        except:
            r = Acceptable_rd[j]
            b = Abacus[(true_i, r, true_alpha)]
        
        z = redshift(i, r_d, alpha, b)
        f = flux(r_d) / (1 + z)**4
        b = b * 3**(3/2) / 2 # translation from b / b_c to b / r_s, which makes more sense from a physics perspective
        
        x, y = np.cos(alpha) * b, np.sin(alpha) * b # translation from (alpha, b) to (x, y) in the observer's plane
        X.append(x)
        Y.append(y)
        F.append(f)
        
    return(X, Y, np.asarray(F))