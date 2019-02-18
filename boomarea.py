import numpy as np
from constants import *


"""
calculate location stringers with origin at hinge location
"""
coord_stringers = np.zeros((13,13))
l_straight = np.sqrt((C_a - h/2.)**2 + (.5*h)**2)
circumference = 2*l_straight + np.pi*h/2.
d_st = circumference/(n_st + 1) #discussion with simon  if using 13 or 13+1
for i in range(n_st):
    di


