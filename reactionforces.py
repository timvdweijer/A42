# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:21:27 2019

@author: Harold
"""
import numpy as np
#import boomarea
from constants import *
import math as m
from MoI_non_idealized import I_yy, I_zz, I_zy
#a = boomarea.coordinates

rad = m.radians(theta)
#Unkown Reaction Forces
#F_1Y
#F_1Z
#F_2X
#F_2X
#F_2Y
#F_3Z
#F_3Z
#F_act1

#Calculating reaction forces in X
#F_2X
F_2U = 0.

# =============================================================================
# #Equations, note that it is in u (x') v(y') w(z')
# #F_1V       F_1W                        F_act                                   F_2V            F_2W        F_3V            F_3W        C1      C2      C3      C4      Knowns                                                                                                      =
# #EQ1
# F_1V                                    +(m.sin(rad))*F_act                     +F_2V                       +F_3V                                                       +(-q*m.cos(rad))*l_a + (-P*m.sin(rad))                                                                       = 0
# #EQ2
#             F_1W                        +(m.cos(rad))*F_act                                     +F_2W                       +F_3W                                       +q*m.sin(rad)*l_a + (-P*m.cos(rad))                                                                         = 0
# #EQ3
# -(d_1*m.sin(rad))*F_1V  -(d_1*m.cos(rad))*F_1W    +((h/2)*(m.sin(rad))-(h/2)*(m.cos(rad)))*F_act            -(d_3*m.sin(rad))*F_3V  -(d_3*m.cos(rad))*F_3W              +(-q*m.cos(rad))*(0.25*C_a-h/2)*l_a + (-P*m.sin(rad))*(h/2) - (-P*m.cos(rad))*(h/2)                          = 0
# #EQ4
#             (x_2-x_1)*F_1W              +(x_a/2)*(m.cos(rad))*F_act                                                         -(x_3-x_2)*F_3W                             +q*m.sin(rad)*(x_2**2/2)-q*m.sin(rad)*(l_a-x_2)**2/2 - (-P*m.cos(rad))*(x_a/2)                               = 0
# #EQ5
# -(x_2-x_1)*F_1V                         -(x_a/2)*(m.sin(rad))*F_act                                          (x_3-x_2)*F_3V                                             (-q*m.cos(rad))*(l_a-x_2)**2/2-(-q*m.cos(rad))*(x_2**2/2) + (-P*m.sin(rad))*(x_a/2)                           = 0 
# #EQ6
#                                                                                                                                         C1*x_1  +C2                     -(-q*m.cos(rad))*(x_1)**4/24                                                                                 = (d_1*m.cos(rad))*(-E*I)
# #EQ7
# -((x_2-x_1)**3/6)*F_1V                  -((x_2-(x_2-(x_a/2))**3)/6)*(m.sin(rad))*F_act                                                  C1*x_2  +C2                     -(-q*m.cos(rad))*(x_2)**4/24                                                                                 = d_2v*(-E*I)
# #EQ8
# -((x_3-x_1)**3/6)*F_1V                  -((x_3-(x_2-(x_a/2))**3)/6)*(m.sin(rad))*F_act      -((x_3-x_2)**3/6)*F_2V                      C1*x_3  +C2                     +(-(-q*m.cos(rad))*(x_3)**4/24)-(-P*m.sin(rad))*((x_3-(x_2+(x_a/2))**3)/6)                                    = (d_3*m.cos(rad))*(-E*I)
# #EQ9
#                                                                                                                                                         C3*x_1  +C4     +q*m.sin(rad)*(x_1)**4/24                                                                                    = (d_1*m.sin(rad))*(-E*I)
# #EQ10
#              ((x_2-x_1)**3/6)*F_1W      +((x_2-(x_2-(x_a/2))**3)/6)*(m.cos(rad))*F_act                                                                   C3*x_2  +C4     +q*m.sin(rad)*(x_2)**4/24                                                                                    = d_2w*(-E*I)
# #EQ11
#              ((x_3-x_1)**3/6)*F_1W      +((x_3-(x_2-(x_a/2))**3)/6)*(m.cos(rad))*F_act      +((x_3-x_2)**3/6)*F_2W                                        C3*x_3  +C4     +(q*m.sin(rad)*(x_3)**4/24)-(-P*m.cos(rad))*((x_3-(x_2+(x_a/2))**3)/6)                                       = (d_3*m.sin(rad))*(-E*I)
# =============================================================================


# #Matrix of the multiplyers of F_1Y and F_2Y
                   #F_1V                    F_1W                        F_act                                       F_2V                F_2W                F_3V                F_3W                C1      C2  C3      C4 
ymulti = np.array([[1,                       0,                          (m.sin(rad)),                               1,                  0,                  1,                  0,                  0,      0,  0,      0], \
                  [0,                       1,                          (m.cos(rad)),                               0,                  1,                  0,                  1,                  0,      0,  0,      0], \
                  [-(d_1*m.sin(rad)),       -(d_1*m.cos(rad)),          ((h/2)*(m.sin(rad))-(h/2)*(m.cos(rad))),    0,                  0,                  -(d_3*m.sin(rad)),  -(d_3*m.cos(rad)),  0,      0,  0,      0], \
                  [0,                       (x_2-x_1),                  (x_a/2)*(m.cos(rad)),                       0,                  0,                  0,                  -(x_3-x_2),         0,      0,  0,      0], \
                  [-(x_2-x_1),              0,                          -(x_a/2)*(m.sin(rad)),                      0,                  0,                  (x_3-x_2),          0,                  0,      0,  0,      0], \
                  [0,                       0,                          0,                                          0,                  0,                  0,                  0,                  x_1,    1,  0,      0], \
                  [-((x_2-x_1)**3/6),       0,                          -((x_2-(x_2-(x_a/2))**3)/6)*(m.sin(rad)),   0,                  0,                  0,                  0,                  x_2,    1,  0,      0], \
                  [-((x_3-x_1)**3/6),       0,                          -((x_3-(x_2-(x_a/2))**3)/6)*(m.sin(rad)),   -((x_3-x_2)**3/6),  0,                  0,                  0,                  x_3,    1,  0,      0], \
                  [0,                       0,                          0,                                          0,                  0,                  0,                  0,                  0,      0,  x_1,    1], \
                  [0,                       ((x_2-x_1)**3/6),           ((x_2-(x_2-(x_a/2))**3)/6)*(m.cos(rad)),    0,                  0,                  0,                  0,                  0,      0,  x_2,    1], \
                  [0,                       ((x_3-x_1)**3/6),           ((x_3-(x_2-(x_a/2))**3)/6)*(m.cos(rad)),    0,                  ((x_3-x_2)**3/6),   0,                  0,                  0,      0,  x_3,    1]])
# #Matrix of the result of the cross product of multiplyers and the forces matrix
yresult = np.array([[-((-q*m.cos(rad))*l_a + (-P*m.sin(rad)))], \
                   [-(q*m.sin(rad)*l_a + (-P*m.cos(rad)))], \
                   [-((-q*m.cos(rad))*(0.25*C_a-h/2)*l_a + (-P*m.sin(rad))*(h/2) - (-P*m.cos(rad))*(h/2))], \
                   [-(q*m.sin(rad)*(x_2**2/2)-q*m.sin(rad)*(l_a-x_2)**2/2 - (-P*m.cos(rad))*(x_a/2))], \
                   [-((-q*m.cos(rad))*(l_a-x_2)**2/2-(-q*m.cos(rad))*(x_2**2/2) + (-P*m.sin(rad))*(x_a/2))], \
                   [(d_1*m.cos(rad))*(-E*I_zz)-(-(-q*m.cos(rad))*(x_1)**4/24)], \
                   [0*(-E*I_zz)-(-(-q*m.cos(rad))*(x_2)**4/24)], \
                   [(d_3*m.cos(rad))*(-E*I_zz)-((-(-q*m.cos(rad))*(x_3)**4/24)-(-P*m.sin(rad))*((x_3-(x_2+(x_a/2))**3)/6))], \
                   [(d_1*m.sin(rad))*(-E*I_yy)-(q*m.sin(rad)*(x_1)**4/24)], \
                   [0*(-E*I_yy)-(q*m.sin(rad)*(x_2)**4/24)], \
                   [(d_3*m.sin(rad))*(-E*I_yy)-((q*m.sin(rad)*(x_3)**4/24)-(-P*m.cos(rad))*((x_3-(x_2+(x_a/2))**3)/6))]])
# #Solving previous matrices to get the F_1Y and F_2Y
FY12 = np.linalg.solve(ymulti,yresult)

F_1V = FY12[0]
F_1W = FY12[1]
F_act = FY12[2]
F_2V = FY12[3]
F_2W = FY12[4]
F_3V = FY12[5]
F_3W = FY12[6]
C1 = FY12[7]
C2 = FY12[8]
C3 = FY12[9]
C4 = FY12[10]
#print (F_1V, F_1W, F_act, F_2V, F_2W, F_3V, F_3W)

print ("Ry1 = ", F_1V/1000, "kN")
print ("Ry2 = ", F_2V/1000, "kN")
print ("Ry3 = ", F_3V/1000, "kN")
print ("Rz1 = ", F_1W/1000, "kN")
print ("Rz2 = ", F_2W/1000, "kN")
print ("Rz3 = ", F_3W/1000, "kN")
print ("Fact = ", F_act/1000, "kN")

Fy_sum = F_1V+(m.sin(rad))*F_act  +F_2V +F_3V +(-q*m.cos(rad))*l_a + (-P*m.sin(rad)) 
Fz_sum = F_1W +(m.cos(rad))*F_act +F_2W  +F_3W +q*m.sin(rad)*l_a + (-P*m.cos(rad))


print ("Sum of y forces: ", Fy_sum)
print ("Sum of z forces: ", Fz_sum)



# =============================================================================
# #Calculating reaction forces in Y
# 
# # =============================================================================
# # #EQUATION 1
# # #2.03 = (1/EI)*((q/24)*(x_2-x_3) + F_1Y*(((x_3-x_1)^3-(x_2-x_1)^3)/6) +F_2Y*((x_3-x_2)^3/6) + (x_3-x_2)*((0.681*EI+(q/24)*(x_1-x_2)+F_1Y*((x_2-x_1)^3/6))/(x_1-x_2)))
# # #matrix form
# # #[(2.03 - (1/EI)*(q/24)*(x_2-x_3) -(x_3-x_2)*((0.681*EI+(q/24)*(x_1-x_2))/(x_1-x_2)))/(1/EI) ]= F_1Y*((((x_3-x_1)^3-(x_2-x_1)^3)/6)+(x_3-x_2)*(((x_2-x_1)^3/6)/(x_1-x_2))) +F_2Y*((x_3-x_2)^3/6) 
# # 
# # #EQUATION 2
# # #0 = q*(l_a-x_3)^2/2-q*(x_3)^2/2 + F_2Y*(x_3-x_2) + F_1Y*(x_3-x_1)
# # #matrix form
# # #[-(q*(l_a-x_3)^2/2-q*(x_3)^2/2)] = F_1Y*(x_3-x_1) + F_2Y*(x_3-x_2)
# # =============================================================================
# 
# #Matrix of the multiplyers of F_1Y and F_2Y
# ymulti = np.array([[E*I*((((x_3-x_1)**3-(x_2-x_1)**3)/6)+(x_3-x_2)*(((x_2-x_1)**3/6)/(x_1-x_2))),E*I*(((x_3-x_2)**3/6))],[(x_3-x_1),(x_3-x_2)]])
# #Matrix of the result of the cross product of multiplyers and the forces matrix
# yresult = np.array([(2.03 - (1/E*I)*((q/24)*(x_2-x_3) -(x_3-x_2)*((0.681*E*I+(q/24)*(x_1-x_2))/(x_1-x_2)))),-(q*(l_a-x_3)**2/2-q*(x_3)**2/2)])
# #Solving previous matrices to get the F_1Y and F_2Y
# FY12 = np.linalg.solve(ymulti,yresult)
# 
# F_1Y = FY12[0]
# F_2Y = FY12[1]
# #EQUATION 3
# F_3Y = q*l_a - F_1Y - F_2Y
# print (F_1Y, F_2Y, F_3Y)
# #Calculating the reaction forces in Z
# 
# #EQUATION 1
# 
# 
# =============================================================================


# =============================================================================
# I = 0.0000001                  #Moment of Inertia [m^4]
# 
# 
# #F_1Y from eq 3.10
# F_1Y = (d_1-(-q*(x_2-x_1)**4)/(8*E*I))*((3*E*I)/((x_2-x_1)**3))
# print (F_1Y)
# 
# #F_3Y from eq 3.14
# F_3Y = (d_3-(-q*(x_3-x_2)**4)/(8*E*I))*((3*E*I)/((x_3-x_2)**3))
# 
# #F_2Y from 3.2
# F_2Y = -F_1Y-F_3Y+q*l_a
# print (F_2Y)
# 
# b = -q*0.5*x_2**2+F_1Y*(x_1-x_2)+F_3Y*(x_3-x_2)+q*0.5*(l_a-x_2)**2
# print (b)
# =============================================================================
