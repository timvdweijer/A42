# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#shear forces and moment diagrams along x-axis

import numpy as np
from constants import * 
import matplotlib.pyplot as plt
import reactionforces


def heaviside(x1):
    if x1 < 0:
        return 0
    elif x1 >= 0:
        return 1

step=0.001
x = np.arange(1, l_a+step, step)


R1v= reactionforces.F_1V
R1w=reactionforces.F_1W
R2v=reactionforces.F_2V
R2w=reactionforces.F_2W
R3v=reactionforces.F_3V
R3w=reactionforces.F_3W
Ract1=reactionforces.F_act


Sy=[]
Sx=[]
Sz=[]
Mz=[]
My=[]

rad = np.radians(theta)
step=0.001
for x in np.arange(0, l_a+step, step):
#Shear Forces
    Sy.append(q*np.cos(rad)*x-R1v*heaviside(x-x_1)-Ract1*np.sin(rad)*heaviside(x-(x_2-(x_a/2)))-R2v*heaviside(x-x_2)+P*np.sin(rad)*heaviside(x-(x_2+(x_a/2)))-R3v*heaviside(x-x_3))

    Sz.append(-q*np.sin(rad)*x-R1w*heaviside(x-x_1)-Ract1*np.cos(rad)*heaviside(x-(x_2-x_a/2))+P*np.cos(rad)*heaviside(x-(x_2+x_a/2))-R2w*heaviside(x-x_2)-R3w*heaviside(x-x_3))

#Moments
    My.append((q*np.sin(rad))*((x**2)/2)+R1w*(x-x_1)*heaviside(x-x_1)+Ract1*np.cos(rad)*(x-(x_2-x_a/2))*heaviside(x-(x_2-x_a/2))+R2w*(x-x_2)*heaviside(x-x_2)-P*np.cos(rad)*(x-(x_2+x_a/2))*heaviside(x-(x_2+x_a/2))+R3w*(x-x_3)*heaviside(x-x_3))
    
    Mz.append(-1*(q * np.cos(rad))*((x**2)/2)+R1v*heaviside(x-x_1)*(x-x_1)+R2v*heaviside(x-x_2)*(x-x_2)+R3v*heaviside(x-x_3)*(x-x_3)+Ract1*np.sin(rad)*heaviside(x-(x_2-x_a/2))*(x-(x_2-x_a/2))-P*np.sin(rad)*heaviside(x-(x_2+x_a/2))*(x-(x_2+x_a/2)))


x = np.arange(0, l_a+step, step)


#plots
plt.figure(1)
plt.subplot(211)
plt.plot(x, Sy, x, Sz)

plt.subplot(212)
plt.axis()
plt.plot(x, My, x, Mz)
plt.show()

