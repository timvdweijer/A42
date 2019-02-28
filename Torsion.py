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
from reactionforces import *
from MoI_non_idealized import J



"""
Calculation of the torsion due to Fact, P and q around hinge 2 check if that's okay
these are split up in the u,v,w components of the'new' reference frame
"""
def heaviside(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1
F_act = 39.72774618*1000
theta_r = radians(theta)                                    #convert degrees to radians
q_w = 0#sin(theta_r) * q                                      #z_component of q
q_v = cos(theta_r) * q                                      #y_component of q
P_w = 0#cos(theta_r) * P                                  #z_component of P
P_v = 0#sin(theta_r) * P                                      #y_component of P
Fact_w = cos(theta_r) *  F_act                            #z_component of jammed actuator
Fact_v = 0#sin(theta_r) * F_act                                #y_component of jammed actuator


lstep = .001                                                #define spanwise step
x = np.arange(0, l_a + lstep, lstep)                        #create array of x points spanwise
"""
if F_1V is in positive y direction, and shearloc_y is negative from reference frame--> negative location, no sign modification needed as pitch down is positve moment
same principle upholds for F_1W  but now sign modification is needed
Fact_v: moment is negative due to direction of F act, sign modification needed ----> other sign for P as it has opporite vector
Fact_w: no sign modification is needed because of direction ---> other sign for P
"""
# =============================================================================
# 
# T = []
# for x in np.arange(0, l_a+step, step):
#     T.append(\
#         F_1V * shearloc_z* (heaviside(x-x_1)) +\      
#     -1* F_1W * shearloc_y* (heaviside(x-x_1)) +\            
#         F_2V * shearloc_z* (heaviside(x-x_2)) +\
#     -1* F_2W * shearloc_y* (heaviside(x-x_2)) +\
#         F_3V * shearloc_z* (heaviside(x-x_3)) +\
#     -1* F_3W * shearloc_y* (heaviside(x-x_3)) +\
#     -1* Fact_v * (h/2 - shearloc_z) * (heaviside(x-(x_2 - x_a / 2.))) +\
#         Fact_w * (h/2 - shearloc_y) * (heaviside(x-(x_2 - x_a / 2.))) +\     
#         P_v * (h/2 - shearloc_z) * (heaviside(x-(x_2 + x_a / 2.))) +\     
#     -1* P_w * (h/2 - shearloc_y) * (heaviside(x-(x_2 + x_a / 2.))) +\     
#         q_v * (-1 * (0.25*C_a - h/2.) - shearloc_z) +\
#     -1* q_w * (shearloc_y))
# =============================================================================
T = []
xx = []
for x in np.arange(0, l_a + lstep, lstep):
    T.append(-1*Fact_v * (h/2) * (heaviside(x-(x_2 - x_a / 2.))) + Fact_w * (h/2) * (heaviside(x-(x_2 - x_a / 2.))) + P_v * (h/2) * (heaviside(x-(x_2 + x_a / 2.))) - P_w * (h/2) * (heaviside(x-(x_2 + x_a / 2.))) +  q_v * x* (-1 * (0.25*C_a - h/2.)))
    xx.append(x*1000)
# =============================================================================
# plt.plot(xx ,T)
# =============================================================================
# =============================================================================
# T = []                                                      #create empty list for torque, the zero is to d
# xx =[]                                                      #create empty list for x_positions, the zero is to d
# for i in np.nditer(x):
#     if i == 0:
#         Tq = (-1*q_v*lstep* (0.25*C_a - h/2.))              #if x = 0 then calculate first torque due to q, loter on the value before is needed
#         T.append(Tq)                                        
#         xx.append(i)
#     elif i >= (x_2 - x_a/2) and i < (x_2 - x_a/2.+lstep):   #at actuator 1 which is jammed
#         Tq = (-1*q_v*lstep* (0.25*C_a - h/2.))              #calculate torque due to q 
#         Tact = -1* (Fact_w * h/2 + -1* Fact_v *h/2)         #calculate torque due to 
#         T.append(Tq +Tact + T[int(i*1000) - 1])             #append value to T_lst of all components + last component
#         xx.append(i)
#     elif i >= (x_2 + x_a/2.) and i < (x_2 + x_a/2.+lstep):  #non-jammed actuator     
#         TP = P_w * h/2 + -1* P_v *h/2                       #calculate torque due to P
#         Tq = (-1*q_v*lstep* (0.25*C_a - h/2.))              #calculate torque due to q
#         T.append(Tq + TP + T[int(i*1000) - 1])              #append value to T_lst of all components + last component
#         xx.append(i)
#     else:
#         Tq = (-1*q_v*lstep* (0.25*C_a - h/2.) )             #at all values except actuators add only q_acts
#         T.append(Tq + T[int(i*1000) - 1])
#         xx.append(i)
# plt.plot(xx,T)
# plt.show()
# =============================================================================

area_1 = pi * (h/2)**2 /2                                   #enclosed areas of cell 1 and two
area_2 = (C_a- h/2) * h
s_semi = pi* h/2 / t_sk                                     #integral parts of formula of semi circle 
s_rib = h / t_sp                                            #integral parts of formula of rib 
s_TE =  coordinates.coordinate(C_a, h/2, n_st)[2]*2 / t_sk  #integral parts of formula of part with straight lines 

def shear_torque(T, s_semi, s_rib, s_TE, area_1, area_2):
    """
    find shear flow due to torsion; cell 1 is semicircular part, cell2 is TE
    deflection cell 1 = deflection cell 2 
    and T = Tcell_1 + Tcell_2 
    now you can solve #see page 613 of Megson aircraft structures
    matrix [qcell_1, qcell_2]
    s_.. = distance of element / thickness
    """
    q_T = []
    for i in range(0, len(T)):                                  #for all x as before calculate shear 1 and two
        A = np.array([[(s_semi + s_rib)/(2*area_1*G)+ (s_rib)/(2*area_2*G), -1*((s_TE + s_rib)/(2*area_2*G) + (s_rib)/(2*area_1*G))], [2*area_1, 2*area_2]])
        B = np.array([0, T[i]])
        q1_T, q2_T = np.linalg.solve(A,B)
        q_T.append([q1_T, q2_T]) 
    return q_T
q_T = shear_torque(T, s_semi, s_rib, s_TE, area_1, area_2)

def theta(q_T, lstep): #gives the angle at all location
    theta = [] 
    theta.append( (q_T[0][0]* (s_semi+s_rib) - q_T[0][1]*s_rib)/(2*area_1*G) * lstep) #p.613 formula megson where lstep = dz                                                   #deflection in terms of theta                                            #deflection theta
    for i in range(1, len(q_T[:])):
        d_theta_torque = (q_T[i][0]* (s_semi+s_rib) - q_T[i][1]*s_rib)/(2*area_1*G) * lstep #p.613 formula megson where lstep = dz
        theta.append(d_theta_torque + theta[i-1])
    return (theta)

theta_corrected = theta(q_T, lstep) - theta(q_T, lstep)[418] #assume deflection is zero at hinge 1 
plt.plot(xx, theta_corrected)

# =============================================================================
# def theta(q_T, lstep): #gives the angle at all location
#     theta = [] 
#     theta.append( (q_T[0][0]* (s_semi+s_rib) - q_T[0][1]*s_rib)/(2*area_1*G) * lstep) #p.613 formula megson where lstep = dz                                                   #deflection in terms of theta                                            #deflection theta
#     for i in range(1, len(q_T[:])):
#         d_theta_torque = (q_T[i][0]* (s_semi+s_rib) - q_T[i][1]*s_rib)/(2*area_1*G) * lstep #p.613 formula megson where lstep = dz
#         theta.append(d_theta_torque + theta[i-1])
#     return (theta)
# =============================================================================


