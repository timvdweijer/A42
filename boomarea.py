import numpy as np
import constants 
import math
import copy


"""
calculate location stringers with origin at hinge location
"""
l_straight = np.sqrt((constants.C_a - constants.h/2.)**2 + (.5*constants.h)**2)         #calculate length straight 
l_semi_circle = math.pi*constants.h/2.                                                       #aileron circumference of semi_circle
d_st = (2*l_straight + l_semi_circle )/(constants.n_st + 1)  #discussion with simon  if using 13 or 13+1, indien 13 verander the range
alpha = math.atan2(constants.h/2., constants.C_a - constants.h / 2.  )                       #calculate angle of straight parts aileron w.r.t. reference systems



coordinates = []
for i in range(1, constants.n_st + 1): #"check of deze plus 1 klopt"
    if d_st*i < l_straight:
        z_coordinate = math.cos(alpha)* d_st * i - (constants.C_a - constants.h/2)  #substract the (chord - radius semi-circle) of the aileron for z_coordinate with origin at hinge line
        
  #  elif d_st*i < (l_semi_circle + l_straight):
        
   # else:  
    print (i, z_coordinate, i* d_st)
    coordinates.append(z_coordinate)
    dist += d_st
