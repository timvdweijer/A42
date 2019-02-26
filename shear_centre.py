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
    d_q_ij_lst = []
    for i in range(0,11 ): 
        if i <=5:
            d_q_ij =   -1* boomarea / Izz * coordinatesy[i]
        else: 
            d_q_ij =   -1* boomarea / Izz * coordinatesy[i + 3]
        
        if i == 0:                                                              #make list for the q's between all booms, symmetric which is supposed to be symmetric
            d_q_ij_lst.append(d_q_ij)
        else:
            d_q_ij_lst.append(d_q_ij + d_q_ij_lst[-1])
    print (len(d_q_ij_lst))
# =============================================================================
#         if i <=5:
#             d_q_ij =   boomarea[i] / Izz * coordinatesy[i]
#         else: 
#             d_q_ij =   boomarea[i + 4] / Izz * coordinatesy[i + 3]
#         d_q_ij_lst.append(d_q_ij)
# =============================================================================
"""
Cell I compute base shear flow
"""
        
        
shearcentre(coordinates.a[0], 1, 1)
    
    
            
        