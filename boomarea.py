import numpy as np
import constants 
import math
import matplotlib.pyplot as plt
import copy


"""
calculate location stringers with origin at hinge location
"""
l_straight = np.sqrt((constants.C_a - constants.h/2.)**2 + (.5*constants.h)**2)         #calculate length straight 
l_semi_circle = math.pi*constants.h/2.                                                       #aileron circumference of semi_circle
d_st = (2*l_straight + l_semi_circle )/(constants.n_st )  #discussion with simon  if using 13 or 13+1, indien 13 verander the range
alpha = math.atan2(constants.h/2., constants.C_a - constants.h / 2.  )                       #calculate angle of straight parts aileron w.r.t. reference systems



coordinatesz = [0] * int(constants.n_st )
coordinatesy = [0] * int(constants.n_st )

for i in range(1, constants.n_st + 1):#""""check of deze plus 1 klopt"""
    if (d_st* i-  d_st/2.)< l_straight:
        coordinatesz[i - 1] = math.cos(alpha)* (d_st * i -  d_st/2.) - (constants.C_a - constants.h/2)  #substract the (chord - radius semi-circle) of the aileron for z_coordinate with origin at hinge line
        coordinatesy[i - 1] = - math.sin(alpha)* (d_st* i-  d_st/2.)
        end_straight_length = d_st* i-  d_st/2.
        j = copy.deepcopy(i)  
        print (l_straight - (d_st * i -  d_st/2.))
    elif (d_st* i-  d_st/2.) < (l_semi_circle + l_straight):
        print ("i am here")
        beta = (d_st*i - d_st* j - (l_straight - end_straight_length)) / (constants.h/2) 
        coordinatesz[i - 1] = math.sin((beta)) * constants.h/2. 
        coordinatesy[i - 1] = - math.cos((beta)) * constants.h/2.
        b = copy.deepcopy(i)
    elif (d_st* i-  d_st/2.) < (l_semi_circle + l_straight* 2.):
        print (i, (((d_st * i - d_st/2) - (l_semi_circle + l_straight))))
# =============================================================================
#         coordinatesz[i - 1] =  math.cos(alpha)* (l_straight - ((d_st * i - d_st/2) - (l_semi_circle + l_straight)))  - (constants.C_a - constants.h/2)
#         coordinatesy[i - 1] = - math.sin(alpha)* (l_straight - (d_st * i - d_st/2 - (l_semi_circle + l_straight))) 
# =============================================================================
coordinatesz.append(0)
coordinatesy.append(constants.h /2. )
coordinatesz.append(0)
coordinatesy.append(- 1.* constants.h /2. )


plt.plot(coordinatesz, coordinatesy, 'ro')
plt.axis([-.484 + 0.173/2, max(coordinates), -constants.h /2., max(coordinatesy) ])
plt.show()