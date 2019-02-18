# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:21:27 2019

@author: Harold
"""
import numpy as np
import boomarea
from constants import *
a = boomarea.coordinates

#Unkown Reaction Forces
#F_1Y
#F_1Z
#F_2X
#F_2X
#F_2Y
#F_3Z
#F_3Z
#F_act1



I = 0.00000001                  #Moment of Inertia [m^4]
#F_2X
F_2X = 0.

#F_1Y from eq 3.10
F_1Y = (d_1-(-q*(x_2-x_1)**4)/(8*E*I))*((3*E*I)/((x_2-x_1)**3))
print (F_1Y)

#F_3Y from eq 3.14
F_3Y = (d_3-(-q*(x_3-x_2)**4)/(8*E*I))*((3*E*I)/((x_3-x_2)**3))

#F_2Y from 3.2
F_2Y = -F_1Y-F_3Y+q*l_a
print (F_2Y)

b = -q*0.5*x_2**2+F_1Y*(x_1-x_2)+F_3Y*(x_3-x_2)+q*0.5*(l_a-x_2)**2
print (b)