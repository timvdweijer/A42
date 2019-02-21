import numpy as np
import constants 
import math
import matplotlib.pyplot as plt
import copy


"""
calculate location stringers with origin at hinge location
"""
#chord = constants.C_a
#radius = constants.h/2.
#n_st = number of stringers = constants.n_st
def coordinate(chord, radius, n_st):
    l_straight = math.sqrt((chord - radius)**2 + (radius)**2)                   #calculate length straight 
    l_semi_circle = math.pi * radius                                            #aileron circumference of semi_circle
    d_st = (2*l_straight + l_semi_circle )/(constants.n_st )                    #calculate length between 2 stringers
    alpha = math.atan2(radius, chord - radius  )                                #calculate angle of straight line of aileron
    coordinatesz = [0] * int(n_st +2)                                           #add 2 for rib booms
    coordinatesy = [0] * int(n_st +2)
       
    for i in range(1, constants.n_st + 1):                                      #start at stringer number 1
        if (d_st* i-  d_st/2.) < l_straight:
            coordinatesz[i - 1] = math.cos(alpha)* (d_st * i -  d_st/2.) - (chord - radius)  #substract the (chord - radius semi-circle) of the aileron for z_coordinate with origin at hinge line
            coordinatesy[i - 1] = - math.sin(alpha)* (d_st* i-  d_st/2.)
            end_straight_length = d_st* i-  d_st/2.
            j = copy.deepcopy(i)  
        elif (d_st* i-  d_st/2.) < (l_semi_circle + l_straight):
            beta = (d_st*i - d_st* j - (l_straight - end_straight_length)) / (radius) 
            coordinatesz[i ] = math.sin((beta)) * radius
            coordinatesy[i ] = - math.cos((beta)) * radius
        elif (d_st* i-  d_st/2.) < (l_semi_circle + l_straight* 2.):
            coordinatesz[i + 1] = math.cos(alpha)* (l_straight - ((d_st * i - d_st/2) - (l_semi_circle + l_straight))) - (chord - radius)  #substract the (chord - radius semi-circle) of the aileron for z_coordinate with origin at hinge line
            coordinatesy[i + 1] = math.sin(alpha)* (l_straight - ((d_st * i - d_st/2) - (l_semi_circle + l_straight)))
    coordinatesy[5] = radius
    coordinatesy[9] = -1* radius
    
    
# =============================================================================
#     """ only plotting below except for return
#     """ 
#     plt.plot(coordinatesz, coordinatesy, 'ro')
#     plt.axis([max(coordinatesz)+.02, -.484 , -.2, .2])
#     plt.show()
#    
# =============================================================================
    return (coordinatesy, coordinatesz, l_straight, alpha)

coordinate(constants.C_a, constants.h/2, constants.n_st)
    