# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:36:28 2019

@author: timvd
"""
import coordinates
import numpy as np


def shearcentre(coordinatesy, boomarea, Izz):
    """
    cell II compute base shear flow
    """ 
    d_q_ij_lst_cellI = []
    for i in range(0,11 ): 
        if i <=5:
            d_q_ij =   -1* boomarea / Izz * coordinatesy[i]           #add Sy          #as centroid of y_location is on y axis, it's just the coordinates
        else: 
            d_q_ij =   -1* boomarea / Izz * coordinatesy[i + 3]
        
        if i == 0:                                                              #make list for the q's between all booms, symmetric which is supposed to be symmetric
            d_q_ij_lst_cellI.append(d_q_ij)
        else:
            d_q_ij_lst_cellI.append(d_q_ij + d_q_ij_lst[-1])

    """
    Cell I compute base shear flow
    """
    d_q_ij_lst_cellII = []
    for i in range(0,5):
        if i <=3:
            d_q_ij =   -1* boomarea / Izz * coordinatesy[i + 6]             #add Sy        #as centroid of y_location is on y axis, it's just the coordinates  
            print (coordinatesy[i + 6])
        else: 
            d_q_ij =   -1* boomarea / Izz * coordinatesy[i + 3]
            print (coordinatesy[i + 1])
        
        if i == 0:                                                              #make list for the q's between all booms, symmetric which is supposed to be symmetric
            d_q_ij_lst_cellII.append(d_q_ij)
        else:
            d_q_ij_lst_cellII.append(d_q_ij + d_q_ij_lst[-1])   


shearcentre(coordinates.a[0], 1, 1)
    
    
# =============================================================================
#         if i <=5:
#             d_q_ij =   boomarea[i] / Izz * coordinatesy[i]
#         else: 
#             d_q_ij =   boomarea[i + 4] / Izz * coordinatesy[i + 3]
#         d_q_ij_lst.append(d_q_ij)
# =============================================================================            
        