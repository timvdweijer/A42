# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:11:10 2019

@author: timvd
"""
from math import *
from constants import *
import numpy as np
import coordinates
import matplotlib.pyplot as plt

"""
Calculation of the torsion due to Fact, P and q around hinge 2 check if that's okay
these are split up in the u,v,w components of the'new' reference frame
"""

Fact = 39730.36831382 ################################################################import right value and sign
theta_r = radians(theta)                                    #convert degrees to radians
q_w = sin(theta_r) * q                                      #z_component of q
q_v = cos(theta_r) * q                                      #y_component of q
P_w = cos(theta_r) * -1* P                                  #z_component of P
P_v = sin(theta_r) * P                                      #y_component of P
Fact_w = cos(theta_r) * -1* Fact                            #z_component of jammed actuator
Fact_v = sin(theta_r) * Fact                                #y_component of jammed actuator

lstep = .001                                                #define spanwise step
x = np.arange(0, l_a+lstep, lstep)                         #create array of x points spanwise
T = []                                                      #create empty list for torque, the zero is to d
xx =[]                                                      #create empty list for x_positions, the zero is to d
for i in np.nditer(x):
    if i == 0:
        Tq = (-1*q_v*lstep* (0.25*C_a - h/2.))              #if x = 0 then calculate first torque due to q, loter on the value before is needed
        T.append(Tq)                                        
        xx.append(i)
    elif i >= (x_2 - x_a/2) and i < (x_2 - x_a/2.+lstep):   #at actuator 1 which is jammed
        Tq = (-1*q_v*lstep* (0.25*C_a - h/2.))              #calculate torque due to q 
        Tact = -1* (Fact_w * h/2 + -1* Fact_v *h/2)         #calculate torque due to 
        T.append(Tq +Tact + T[int(i*1000) - 1])             #append value to T_lst of all components + last component
        xx.append(i)
    elif i >= (x_2 + x_a/2.) and i < (x_2 + x_a/2.+lstep):  #non-jammed actuator     
        TP = P_w * h/2 + -1* P_v *h/2                       #calculate torque due to P
        Tq = (-1*q_v*lstep* (0.25*C_a - h/2.))              #calculate torque due to q
        T.append(Tq + TP + T[int(i*1000) - 1])              #append value to T_lst of all components + last component
        xx.append(i)
    else:
        Tq = (-1*q_v*lstep* (0.25*C_a - h/2.) )             #at all values except actuators add only q_acts
        T.append(Tq + T[int(i*1000) - 1])
        xx.append(i)
# =============================================================================
# plt.plot(xx,T)
# plt.show()
# =============================================================================

"""
find shear flow due to torsion; cell 1 is semicircular part, cell2 is TE
deflection cell 1 = deflection cell 2 
and T = Tcell_1 + Tcell_2 
now you can solve #see page 613 of Megson aircraft structures
matrix [qcell_1, qcell_2]
s_.. = distance of element / thickness
"""
area_1 = pi * (h/2)**2 /2                                   #enclosed areas of cell 1 and two
area_2 = (C_a- h/2) * h
s_semi = pi* h/2 / t_sk                                     #integral parts of formula of semi circle 
s_rib = h / t_sp                                            #integral parts of formula of rib 
s_TE =  coordinates.coordinate(C_a, h/2, n_st)[2]*2 / t_sk  #integral parts of formula of part with straight lines 
q_T = []
for i in range(0, len(T)):                                  #for all x as before calculate shear 1 and two
    A = np.array([[(s_semi + s_rib)/(2*area_1*G)+ (s_rib)/(2*area_2*G), -1*((s_TE + s_rib)/(2*area_2*G) + (s_rib)/(2*area_1*G))], [2*area_1, 2*area_2]])
    B = np.array([0, T[i]])
    q1_T, q2_T = np.linalg.solve(A,B)
    q_T.append([q1_T, q2_T])  



def_theta = []                                              #deflection in terms of theta
def_theta.append( (q_T[0][0]* (s_semi+s_rib) - q_T[0][1]*s_rib)/(2*area_1*G) * lstep) #p.613 formula megson where lstep = dz                                             #deflection theta
for i in range(1, len(q_T[:])):
    d_theta_torque = (q_T[i][0]* (s_semi+s_rib) - q_T[i][1]*s_rib)/(2*area_1*G) * lstep #p.613 formula megson where lstep = dz
    def_theta.append(d_theta_torque + def_theta[i-1])

# =============================================================================
# plt.plot(xx, q_T[:][0], xx, q_T[:][1]) ######################## beginning is at the end, not good
# plt.show()
# =============================================================================

plt.plot(xx, def_theta)
plt.show()