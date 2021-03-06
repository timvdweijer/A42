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
import copy
import Torsion as T
from deflectionreadingvalidation import xle, y_defle, xte, y_defte, z_defle, z_defte

def heaviside(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1
    
#To Hinge 1
x = 0
y = 0
Defl = np.zeros((1692,3))
#while x <= 1.691:
while x <= (l_a+0.001):
    dv = (1/(-E*I_zz)) *( q*m.cos(rad)*x**4 /24)# + C1*x + C2)
    dw = (1/(-E*I_yy)) *( q*m.sin(rad)*x**4 /24)# + C3*x + C4)
    d2v = (1/(-E*I_zz)) *( q*m.cos(rad)*heaviside(x-0.001)*(x-0.001)**4/24)#+ C1*x + C2)
    d2w = (1/(-E*I_yy)) *( q*m.sin(rad)*heaviside(x-0.001)*(x-0.001)**4/24)#+ C3*x + C4)
    y= int(x*1000)
    Defl[y,0] = x
    Defl[y,1] = Defl[(y-heaviside(x-0.001)*1),1] + dv - d2v 
    Defl[y,2] = Defl[(y-heaviside(x-0.001)*1),2] + dw - d2w 
    x = x + 0.001
    #return y, x
    
# #To act 1   
x = x_1
while x <= (l_a+0.001) and x >= x_1:
    dv = (1/(-E*I_zz)) * (F_1V*(x-x_1)**3/6)
    dw = (1/(-E*I_yy)) * -(F_1W*(x-x_1)**3/6)
    d2v =(1/(-E*I_zz)) * (F_1V*((x-0.001)-x_1)**3/6)
    d2w =(1/(-E*I_yy)) * -(F_1W*((x-0.001)-x_1)**3/6)
    y= int(x*1000)
    Defl[y,1] = Defl[(y-1),1] + dv - d2v
    Defl[y,2] = Defl[(y-1),2] + dw - d2w
    x = x + 0.001

#To Hinge 2    
#x = 0.419
#y = 419
x = (x_2-x_a/2)
while x <= (l_a+0.001)  and x >= (x_2-x_a/2):
    dv = (1/(-E*I_zz)) * (F_act*m.sin(rad)*(x-(x_2-x_a/2)))
    dw = (1/(-E*I_yy)) * -(F_act*m.cos(rad)*(x-(x_2-x_a/2)))
    d2v = (1/(-E*I_zz)) * (F_act*m.sin(rad)*((x-0.001)-(x_2-x_a/2)))
    d2w = (1/(-E*I_yy)) * -(F_act*m.cos(rad)*((x-0.001)-(x_2-x_a/2)))
    y= int(x*1000)
    Defl[y,1] = Defl[(y-1),1] + dv - d2v
    Defl[y,2] = Defl[(y-1),2] + dw - d2w
    x = x + 0.001

#To P    
#x = 0.555
#y = 555
x = x_2
while x <= (l_a+0.001)  and x >= x_2 :
    dv = (1/(-E*I_zz)) * (F_2V*(x-x_2)**3/6) 
    dw = (1/(-E*I_yy)) * -(F_2W*(x-x_2)**3/6)
    d2v = (1/(-E*I_zz)) * (F_2V*((x-0.001)-x_2)**3/6) 
    d2w = (1/(-E*I_yy)) * -(F_2W*((x-0.001)-x_2)**3/6)
    y= int(x*1000)
    Defl[y,1] = Defl[(y-1),1] + dv - d2v
    Defl[y,2] = Defl[(y-1),2] + dw - d2w
    x = x + 0.001
    

#To Hinge 3
#x = 0.691
#y = 691
x = (x_2+x_a/2)
while x <= (l_a+0.001)  and x >= (x_2+x_a/2):
    dv = (1/(-E*I_zz)) * (P*m.sin(rad)*(x-(x_2+x_a/2))**3/6)
    dw = (1/(-E*I_yy)) * (P*m.cos(rad)*(x-(x_2+x_a/2))**3/6)
    d2v = (1/(-E*I_zz)) * (P*m.sin(rad)*((x-0.001)-(x_2+x_a/2))**3/6)
    d2w = (1/(-E*I_yy)) * (P*m.cos(rad)*((x-0.001)-(x_2+x_a/2))**3/6)
    y= int(x*1000)
    Defl[y,1] = Defl[(y-1),1] + dv - d2v
    Defl[y,2] = Defl[(y-1),2] + dw - d2w
    x = x + 0.001

#To end    
#x = 1.542
#y = 1542
x = x_3
while x <= (l_a+0.001)  and x >= x_3:
    dv = (1/(-E*I_zz)) * (F_3V*(x-x_3)**3/6)
    dw = (1/(-E*I_yy)) * -(F_3W*(x-x_3)**3/6)
    d2v = (1/(-E*I_zz)) * (F_3V*((x-0.001)-x_3)**3/6)
    d2w = (1/(-E*I_yy)) * -(F_3W*((x-0.001)-x_3)**3/6)
    y= int(x*1000)
    Defl[y,1] = Defl[(y-1),1] + dv - d2v
    Defl[y,2] = Defl[(y-1),2] + dw - d2w
    x = x + 0.001

#plots
# =============================================================================
# =============================================================================
# plt.figure(1)
# plt.subplot(211)
# plt.plot(Defl[:,0], Defl[:,1], Defl[:,0], Defl[:,2])
# plt.show()
# =============================================================================
# =============================================================================
delta = copy.deepcopy(Defl)
# =============================================================================
# for i in range(0, len(Defl)):
#     delta[i,0] = Defl [i,0]
#     delta[i,1] = Defl [i,1]
#     delta[i,2] = Defl [i,2]
# =============================================================================
#Conversion for rotation
for i in range(0, len(Defl)):
    delta[i,0] = delta[i,0] - x_2
    delta[i,1] = delta[i,1] - Defl[554,1]
    delta[i,2] = delta[i,2] - Defl[554,2]

alphav1 = m.atan(d_1*m.cos(rad)/(x_2-x_1))
alphav2 = m.atan(delta[int(x_1*1000),1]/(x_2-x_1))
alphavT = alphav1 + alphav2

alphaw1 = m.atan(d_1*m.sin(rad)/(x_2-x_1))
alphaw2 = m.atan(delta[int(x_1*1000),2]/(x_2-x_1))
alphawT = alphaw1 + alphaw2

for i in range(0, len(Defl)):
    delta[i,1] = delta[i,0]*m.sin(alphavT) + delta[i,1] *m.cos(alphavT)
    delta[i,2] = delta[i,0]*m.sin(alphawT) + delta[i,2] *m.cos(alphawT)
LEdelta = np.zeros((1692,3))
TEdelta = np.zeros((1692,3))
for i in range(0, len(Defl)):
    LEdelta [i,0]= Defl[i,0]
    TEdelta [i,0]= Defl[i,0]
    LEdelta [i,1]= T.displacement[0][i] + delta[i,1]
    LEdelta [i,2]= delta[i,2]
    TEdelta [i,1]= T.displacement[1][i] + delta[i,1]
    TEdelta [i,2]= delta[i,2]
    
#plots
# =============================================================================
# =============================================================================
# plt.figure(1)
# plt.subplot(111)
# plt.plot(LEdelta[:,0], LEdelta[:,1],"r") 
# plt.plot(LEdelta[:,0], TEdelta[:,1],"b") 
# plt.show()
# =============================================================================
# =============================================================================
y_deftec = np.zeros((67,1))
y_deflec = np.zeros((68,1))
for i in range(len(y_defte)):
    y_deftec[i] = y_defte[i]-0.75*C_a*1000*m.sin(rad)
    y_deflec[i] = y_defle[i]+0.25*C_a*1000*m.sin(rad) 

plt.subplot(221)
plt.scatter(xle, y_deflec)
plt.scatter((LEdelta[:,0]*1000), (LEdelta[:,1]*1000))
plt.axis([0,1692,-80,80])
plt.title("Leading edge deflection in v-direction")
plt.xlabel("Spanwise location [mm]")
plt.ylabel("y-deflection [mm]")

plt.subplot(222)
plt.scatter(xte, y_deftec)
plt.scatter((TEdelta[:,0]*1000), (TEdelta[:,1]*1000))
plt.axis([0,1692,-80,80])
plt.title("Trailing edge deflection in v-direction")
plt.xlabel("Spanwise location [mm]")
plt.ylabel("y-deflection [mm]")

plt.subplot(223)
plt.scatter(xle, z_defle)
plt.scatter((LEdelta[:,0]*1000), (LEdelta[:,2]*1000))
plt.axis([0,1692,-80,80])
plt.title("Leading edge deflection in w-direction")
plt.xlabel("Spanwise location [mm]")
plt.ylabel("z-deflection [mm]")

plt.subplot(224)
plt.scatter(xte, z_defte)
plt.scatter((TEdelta[:,0]*1000), (TEdelta[:,2]*1000))
plt.axis([0,1692,-80,80])
plt.title("Trailing edge deflection in w-direction")
plt.xlabel("Spanwise location [mm]")
plt.ylabel("z-deflection [mm]")

#xle, y_defle, xte, y_defte, z_defle, z_defte

# =============================================================================
# x = x*(cos alpha)-y*sin(alpha)
# y' = x*sin (alpha) + y*cos (alpha)
# =============================================================================
#Deflection in V    ================
# #To Hinge 1
# #To act 1
# dact1V = (1/(-E*I)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6
# #To Hinge 2
# d2V = (1/(-E*I)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))
# #To P
# dPV = (1/(-E*I)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))**3/6 + F_2V*(x-x_2)**3/6
# #To Hinge 3
# d3V = (1/(-E*I)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))**3/6 + F_2V*(x-x_2)**3/6 - P*m.sin(rad)*(x-(x_2+x_a/2))**3/6
# #To end
# dend = (1/(-E*I)) * (q*m.cos(rad)*x**4/24 + F_1V*(x-x_1)**3/6 + F_act*m.sin(rad)*(x-(x_2-x_a/2))**3/6 + F_2V*(x-x_2)**3/6 - P*m.sin(rad)*(x-(x_2+x_a/2))**3/6 + F_3V*(x-x_3)**3/6
# 
# =============================================================================


#Deflection in W   ===========

#To Hinge 1
   #(1/(-E*I)) * (q*m.sin(rad)*x**4/24
#To act 1
   #(1/(-E*I)) * (q*m.sin(rad)*x**4/24 + F_1V*(x-x_1)**3/6
#To Hinge 2
#To P
#To Hinge 3