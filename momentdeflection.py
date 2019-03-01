# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:51:33 2019

@author: Harold
"""
import numpy as np
#import boomarea
from constants import *
import math as m
from MoI_non_idealized import I_yy, I_zz, I_zy
from reactionforces import *
import matplotlib.pyplot as plt


#To Hinge 1
x = 0
y = 0
Defl = np.zeros((1692,3))
#while x <= 1.691:
while x <= (x_1+0.001):
    dv = (1/(E*I_zz)) * q*m.cos(rad)*x**4/24
    dw = (1/(E*I_yy)) * q*m.sin(rad)*x**4/24
    Defl[y,0] = x
    Defl[y,1] = dv
    Defl[y,2] = dw
    y= y+1
    x = x + 0.001
    #return y, x
    
# #To act 1   
x = 0.150
y = 150
while x <= (x_2-x_a/2+0.001) and x > x_1:
    dv = dv + (1/(E*I_zz)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6)
    dw = dw + (1/(E*I_yy)) * (q*m.sin(rad)*x**4/24 + F_1W*(x-x_1)**3/6)
    Defl[y,0] = x
    Defl[y,1] = dv
    Defl[y,2] = dw
    y= y+1
    x = x + 0.001

#To Hinge 2    
x = 0.419
y = 419
while x <= (x_2+0.001)  and x > (x_2-x_a/2):
    dv = dv + (1/(E*I_zz)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2)))
    dw = dw + (1/(E*I_yy)) * (q*m.sin(rad)*x**4/24 + F_1W*(x-x_1)**3/6 + F_act*m.cos(rad)*(x-(x_2-x_a/2)))
    Defl[y,0] = x
    Defl[y,1] = dv
    Defl[y,2] = dw
    y= y+1
    x = x + 0.001

#To P    
x = 0.555
y = 555
while x <= (x_2+x_a/2+0.001)  and x > x_2 :
    dv = dv + (1/(E*I_zz)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))**3/6 + F_2V*(x-x_2)**3/6)
    dw = dw + (1/(E*I_yy)) * (q*m.sin(rad)*x**4/24 + F_1W*(x-x_1)**3/6 + F_act*m.cos(rad)*(x-(x_2-x_a/2))**3/6 + F_2W*(x-x_2)**3/6)
    Defl[y,0] = x
    Defl[y,1] = dv
    Defl[y,2] = dw
    y= y+1
    x = x + 0.001
    

#To Hinge 3
x = 0.691
y = 691
while x <= (x_3+0.001)  and x > (x_2+x_a/2):
    dv = dv + (1/(E*I_zz)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))**3/6 + F_2V*(x-x_2)**3/6 - P*m.sin(rad)*(x-(x_2+x_a/2))**3/6)
    dw = dw + (1/(E*I_yy)) * (q*m.sin(rad)*x**4/24 + F_1W*(x-x_1)**3/6 + F_act*m.cos(rad)*(x-(x_2-x_a/2))**3/6 + F_2W*(x-x_2)**3/6 - P*m.cos(rad)*(x-(x_2+x_a/2))**3/6)
    Defl[y,0] = x
    Defl[y,1] = dv
    Defl[y,2] = dw
    y= y+1
    x = x + 0.001

#To end    
x = 1.542
y = 1542
while x <= (l_a)  and x > x_3:
    dv = dv + (1/(E*I_zz)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))**3/6 + F_2V*(x-x_2)**3/6 - P*m.sin(rad)*(x-(x_2+x_a/2))**3/6 + F_3V*(x-x_3)**3/6)
    dw = dw + (1/(E*I_yy)) * (q*m.sin(rad)*x**4/24 + F_1W*(x-x_1)**3/6 + F_act*m.cos(rad)*(x-(x_2-x_a/2))**3/6 + F_2W*(x-x_2)**3/6 - P*m.cos(rad)*(x-(x_2+x_a/2))**3/6 + F_3W*(x-x_3)**3/6)
    Defl[y,0] = x
    Defl[y,1] = dv
    Defl[y,2] = dw
    y= y+1
    x = x + 0.001

#plots
# =============================================================================
plt.figure(1)
plt.subplot(211)
plt.plot(Defl[:,0], Defl[:,1], Defl[:,0], Defl[:,2])
plt.show()
# =============================================================================
#Deflection in V    ================
# #To Hinge 1
# #To act 1
# dact1V = (1/(E*I)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6
# #To Hinge 2
# d2V = (1/(E*I)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))
# #To P
# dPV = (1/(E*I)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))**3/6 + F_2V*(x-x_2)**3/6
# #To Hinge 3
# d3V = (1/(E*I)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))**3/6 + F_2V*(x-x_2)**3/6 - P*m.sin(rad)*(x-(x_2+x_a/2))**3/6
# #To end
# dend = (1/(E*I)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))**3/6 + F_2V*(x-x_2)**3/6 - P*m.sin(rad)*(x-(x_2+x_a/2))**3/6 + F_3V*(x-x_3)**3/6
# 
# =============================================================================


#Deflection in W   ===========

#To Hinge 1
   #(1/(E*I)) * (q*m.sin(rad)*x**4/24
#To act 1
   #(1/(E*I)) * (q*m.sin(rad)*x**4/24 + F_1V*(x-x_1)**3/6
#To Hinge 2
#To P
#To Hinge 3