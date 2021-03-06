# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:40:05 2019

@author: Harold
"""

#Known Forces 
P = 37.9*10**3      #F_act2 [N]
q = 2.71*10**3      #Aerodynamic load [N/m]

#Known Variables
C_a = 0.484             #chord length [m]
l_a = 1.691             #span aileron [m]
x_1 = 0.149             #location hinge 1 [m]
x_2 = 0.554             #location hinge 2 [m]
x_3 = 1.541             #location hinge 3 [m]
x_a = 0.272             #distance between act 1 and 2 [m]
h = 0.173               #aileron height [m]
t_sk = 1.1*10**-3       #skin thickness [m]
t_sp = 2.5*10**-3       #spar thickness [m]
t_st = 1.2*10**-3       #stiffener thickness [m]
h_st = 1.4*10**-2       #height stiffener [m]
w_st = 1.8*10**-2       #width stiffener [m]
n_st = 13               #number of stiffeners [-]
d_1 = 0.681*10**-2      #vert displ hinge 1 [m]
d_3 = 2.03*10**-2       #vert displ hinge 3 [m]
theta = 26.             #max upwards deflect [deg]

#Material and Sturctural Properties
E = 73.1*10**9          #E-modulus [Pa]
G = 28.*10**9            #Shear Modulus [Pa]
tau_ult = 283.*10**6     #Shear Strength [Pa]

