## Import
import numpy as np
import sys
import matplotlib.pyplot as plt

print("All imports successful")

""" All number will start with small letters (a, b, c). All vectors or lists will start by a capital letter (A, B, C)"""

## Parameters
xkcd = False # Use xkcd style for plots ; requires XKCD.py. May require to restart the kernel.

## Question I.b
if xkcd:
    import XKCD as XKCD # additional import to make rough plots that are only used for qualitative analysis

ax = plt.axes()

# define u
u = np.linspace(0, 1, 100)

# draw V(u)
u_c = 1.5
ax.plot(u, u**2 * (1 - u) - 4 * u_c**2 / 27, color = 'red', lw=1)
u_c = 0.9
ax.plot(u, u**2 * (1 - u) - 4 * u_c**2 / 27, color = 'green', lw=1)

# add commentaries
ax.text(0.3, -0.4, "faible parametre d'impact\n(b < b )", color = 'red')
ax.text(0.53, -0.41, "c", color = 'red')
ax.text(0.3, 0.05, "fort parametre d'impact\n(b > b )", color = 'green')
ax.text(0.53, 0.04, "c", color = 'green')

# add tick labels
ax.text(-0.42, - 4 * 1.5**2 / 27, '- 4 * uc^2\n    27', color = 'red')
ax.plot([-0.02, 0.02], [- 4 * 1.5**2 / 27, - 4 * 1.5**2 / 27], 'red', lw = 1)

ax.text(-0.42, - 4 * 0.9**2 / 27, '- 4 * uc^2\n    27', color = 'green')
ax.plot([-0.02, 0.02], [- 4 * 0.9**2 / 27, - 4 * 0.9**2 / 27], 'green', lw = 1)

ax.text(-0.3, -0.2, 'infini', color = 'k')

ax.text(0.475, -0.05, 'u', color = 'green')
ax.text(0.52, -0.06, 'p', color = 'green')
ax.plot([0.475, 0.475], [- 0.02, 0.02], 'green', lw = 1)

# add line at x = 1
ax.text(1.05, -0.2, 'horizon des\nevenements', color = 'k')
ax.plot([1, 1], [-0.33, -0.05], 'k', lw=1)

# setup the plot
ax.set_xlabel('u')
ax.set_ylabel('V(u)')
ax.set_xlim(-0.3, 1.3)

# XKCDify the axes -- this operates in-place
if xkcd:
    XKCD.XKCDify(ax, xaxis_loc = 0.0, yaxis_loc = 0.0, xaxis_arrow = None, yaxis_arrow = None, expand_axes = True)

plt.show()


## Question I.d
if xkcd:
    import XKCD as XKCD # additional import to make rough plots that are only used for qualitative analysis
plt.figure()
sys.path.append(r"C:\Users\Nathan\Documents\F - Exemple XKCDify")

ax = plt.axes()

# define u
u = np.linspace(0, 1, 100)

# draw V(u)
u_c = 1.5
u = np.linspace(0, 1, 100)
u_prime = np.sqrt(- (u**2 * (1 - u) - 4 * u_c**2 / 27))
ax.plot(u, u_prime, color = 'red', lw=1)

u_c = 1
u = np.linspace(0, 2/3- 0.001, 100)
u_prime = np.sqrt(- (u**2 * (1 - u) - 4 * u_c**2 / 27))
ax.plot(u, u_prime, color = 'blue', lw=1)

u_c = 0.9
u = np.linspace(0, 0.48, 100)
u_prime_forward = np.sqrt(- (u**2 * (1 - u) - 4 * u_c**2 / 27))
u_prime_backward = - np.sqrt(- (u**2 * (1 - u) - 4 * u_c**2 / 27))
ax.plot(u, u_prime_forward, color = 'green', lw=1)
ax.plot(u, u_prime_backward, color = 'green', lw=1)

# add commentaries
ax.text(0.3, 0.6, "b < b ", color = 'red')
ax.text(0.5, 0.55, "c", color = 'red')
ax.text(0.5, 0.2, "b = b ", color = 'blue')
ax.text(0.7, 0.15, "c", color = 'blue')
ax.text(0.2, -0.4, "b > b ", color = 'green')
ax.text(0.4, -0.45, "c", color = 'green')

# add tick labels
ax.text(-0.3, 0.2, 'infini', color = 'k')
ax.text(1.05, 0.2, 'horizon des\nevenements', color = 'k')
ax.plot([1, 1], [0, 0.65], 'k', lw=1)

ax.text(0.48, -0.1, 'u', color = 'green')
ax.text(0.525, -0.15, 'p', color = 'green')
ax.plot([0.48, 0.48], [- 0.02, 0.02], 'green', lw = 1)

ax.text(2/3, -0.1, '2/3', color = 'blue')
ax.plot([2/3, 2/3], [- 0.02, 0.02], 'blue', lw = 1)

# setup the plot
ax.set_xlabel("u")
ax.set_ylabel("u '")
ax.set_xlim(-0.3, 1.3)

# XKCDify the axes -- this operates in-place
if xkcd:
    XKCD.XKCDify(ax, xaxis_loc = 0.0, yaxis_loc = 0.0, xaxis_arrow = None, yaxis_arrow = None, expand_axes = True)

plt.show()