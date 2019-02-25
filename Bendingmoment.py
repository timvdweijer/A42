# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import constants 
import matplotlib.pyplot as plt

step=0.001
x = np.arange(0, constants.l_a+step, step)
Mz= np.zeros(int(constants.l_a/step))

Ry1=1
Ry2=2
Ry3=3

Rz1=1
Rz2=2
Rz3=3

Mz=(-(constants.q**2)*(x)/2)+Ry1*np.heaviside(x,constants.x_1)*(x-constants.x_1)
+Ry2*np.heaviside(x,constants.x_2)*(x-constants.x_2)+Ry3*np.heaviside(x,constants.x_3)*(x-constants.x_3)

print  ("Mz is", Mz)

My=(-(constants.q**2)*(x)/2)+Ry1*np.heaviside(x,constants.x_1)*(x-constants.x_1)
+Ry2*np.heaviside(x,constants.x_2)*(x-constants.x_2)+Ry3*np.heaviside(x,constants.x_3)*(x-constants.x_3)

print  ("My is", My)

plt.plot(x, Mz)
plt.show()