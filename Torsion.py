# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:11:10 2019

@author: timvd
"""
from math import *
from constants import *
import numpy as np
import coordinates

"""
Calculation of the torsion due to Fact, P and q around hinge 2 check if that's okay
these are split up in the u,v,w components of the'new' reference frame
"""
Fact = 37900 ################################################################import right value and sign
theta_r = radians(theta)        #convert degrees to radians

q_w = sin(theta_r) * q
q_v = cos(theta_r) * q 
P_w = cos(theta_r) * -1* P
P_v = sin(theta_r) * P
Fact_w = cos(theta_r) * -1* Fact   ####change for right variable
Fact_v = sin(theta_r) * Fact   ####change for right variable

lstep = .001
x = np.arange(0, l_a +lstep, lstep)

T = [0]
xx =[0]
for i in np.nditer(x):
    if i == 0:
        T[0] = (-1*q_v*lstep* (0.25*C_a - h/2.))
    elif i == .554:
        Tq = (-1*q_v*lstep* (0.25*C_a - h/2.) )
        TP = P_w * h/2 + -1* P_v *h/2
        Tact = -1* (Fact_w * h/2 + -1* Fact_v *h/2)
        T.append(Tq + TP +Tact + T[int(i*1000) - 1])
        xx.append(i)        
    else:
        Tq = (-1*q_v*lstep* (0.25*C_a - h/2.) )
        T.append(Tq + T[int(i*1000) - 1])
        xx.append(i)
        
# =============================================================================
# plt.plot(xx,T)
# plt.show()
# 
# =============================================================================
"""
find shear flow due to torsion; cell 1 is semicircular part, cell2 is TE
deflection cell 1 = deflection cell 2 line 59
and T = Tcell_1 + Tcell_2 line 60
now you can solve #see page 613 of Megson aircraft structures
matrix [qcell_1, qcell_2]
s_.. = distance of element / thickness
"""
T = 1
area_1 = pi * (h/2)**2 /2
area_2 = (C_a- h/2) * h
s_semi = pi* h/2 / t_sk
s_rib = h / t_sp
s_TE =  coordinates.coordinate(C_a, h/2, n_st)[2]*2 / t_sk

A = np.array([[(s_semi + s_rib)/(2*area_1*G)+ (s_rib)/(2*area_2*G), -1*((s_TE + s_rib)/(2*area_2*G) + (s_rib)/(2*area_1*G))], [2*area_1, 2*area_2]])
B = np.array([0, T])
q1_T, q2_T = np.linalg.solve(A,B)