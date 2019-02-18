# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:21:27 2019

@author: Harold
"""

#Unkown Reaction Forces
#F_1Y
#F_1Z
#F_2X
#F_2X
#F_2Y
#F_3Z
#F_3Z
#F_act1

#Known Forces 
P = 37.9*10**3      #F_act2 [N]
q = 2.71*10**3      #Aerodynamic loac [N/m]

#Known Variables
C_a = 0.484             #chord length [m]
l_a = 1.691             #span aileron [m]
x_1 = 0.149             #location hinge 1 [m]
x_2 = 0.554             #location hinge 2 [m]
x_3 = 1.541             #location hinge 3 [m]
x_a = 0.274             #distance between act 1 and 2 [m]
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
I =                     #Moment of Inertia []
G = 28*10**9            #Shear Modulus [Pa]
tau_ult = 283*10**6     #Shear Strength []
#F_2X
F_2X = 0.

#F_1Y from eq 3.10
F_1Y = (d_1-(-q*(x_2-x_1)**4)/(*8*E*I))*((3*E*I)/(x_2-x_1)**2)

#F_3Y from eq 3.14
F_3Y = (d_3-(-q*(x_3-x_2)**4)/(*8*E*I))*((3*E*I)/(x_3-x_2)**2)