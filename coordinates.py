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
    mcoordinatesz = [0] * int(n_st +1)                                          #list for the coordinates of the middle of the skin segments
    mcoordinatesy = [0] * int(n_st +1)
    beta_lst = []                                                               #solely added for the calculation of the shear centre
    mbeta = []                                                                  #list for betalist of middle locations of skin for shear     
    
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
            if len(beta_lst) == 0:
                mbeta.append(beta/2)
            else:
                mbeta.append((beta - beta_lst[-1])/2 + beta_lst[-1])
            beta_lst.append(beta)
        elif (d_st* i-  d_st/2.) < (l_semi_circle + l_straight* 2.):
            coordinatesz[i + 1] = math.cos(alpha)* (l_straight - ((d_st * i - d_st/2) - (l_semi_circle + l_straight))) - (chord - radius)  #substract the (chord - radius semi-circle) of the aileron for z_coordinate with origin at hinge line
            coordinatesy[i + 1] = math.sin(alpha)* (l_straight - ((d_st * i - d_st/2) - (l_semi_circle + l_straight)))
    coordinatesy[5] = -1* radius
    coordinatesy[9] = radius
    
    distance_lst = []                                                           #empty list to store distances between 2 booms
    for i in range(0, len(coordinatesy)-1):
        if i < 5 or i >=8:                                                      #distance calculation between booms; needed for shear centre; straight part
            distance_lst.append(math.sqrt( (coordinatesy[i + 1] - coordinatesy[i])**2 +  (coordinatesz[i + 1] - coordinatesz[i])**2))
        elif i >= 5 and i < 8:                                                  #semi_circular part
            if i == 5:
                distance_lst.append((beta_lst[i-5]) * radius)
            else: 
                distance_lst.append(((beta_lst[i-5] - beta_lst[i - 6]) * radius))
    
    mbeta.append((math.radians(180) - beta_lst[-1])/2 + beta_lst[-1])      
    for i in range(0, len(coordinatesy)-1):
        if i <= 4 or i >= 9:
            mcoordinatesz[i] = coordinatesz[i] + (coordinatesz[i + 1] - coordinatesz[i])/2
            mcoordinatesy[i] = coordinatesy[i] + (coordinatesy[i + 1] - coordinatesy[i])/2           
        else:
            mcoordinatesz[i] = math.sin((mbeta[i - 5])) * radius
            mcoordinatesy[i] = - math.cos((mbeta[i - 5])) * radius
        
    return (coordinatesy, coordinatesz, l_straight, alpha, d_st, distance_lst, mcoordinatesy, mcoordinatesz)

a = coordinate(constants.C_a, constants.h/2, constants.n_st)
d = math.sqrt((a[1][5] - a[1][4])**2 + (a[0][5] - a[0][4])**2)

