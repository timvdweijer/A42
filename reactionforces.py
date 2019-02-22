# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:21:27 2019

@author: Harold
"""
import numpy as np
#import boomarea
from constants import *
#a = boomarea.coordinates
I = 1000
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

#Equations, note that it is in u (x') v(y') w(z')
#F_1V       F_1W            F_act       F_2V        F_2W        F_3V        F_3W        C1      C2      C3      C4      Knowns                                          =
#EQ1
F_1V                        +F_actv     +F_2V                   +F_3V                                                   +q_v*l_a + P_v                                  = 0
#EQ2
            F_1W            +F_actw                 +F_2W                   +F_3W                                       +q_w*l_a + P_w                                  = 0
#EQ3
-d_1W*F_1V  -d_1V*F_1W      +d_actv*F_actv-d_actw*F_actw        -d_3W*F_3V  -d_3V*F_3W                                  +q_v*d_q*l_a + P_v*d_actv - P_w*d_actw          = 0
#EQ4
            (x_2-x_1)*F_1W  +(x_a/2)*F_actw                                 -(x_3-x_2)*F_3W                             q_w*(x_2**2/2)-q_w*(l_a-x_2)**2/2 - P_w*(x_a/2)   = 0
#EQ5
-(x_2-x_1)*F_1V             -(x_a/2)*F_actv                     (x_3-x_2)*F_3                                           q_v*(l_a-x_2)**2/2-q_v*(x_2**2/2) + P_v*(x_a/2)     = 0 
#EQ6










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
