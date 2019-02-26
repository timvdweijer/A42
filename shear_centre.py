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
    

#redundantshearflow:
cellI=np.array([7,8,9,10,6])
cellII=np.array([0,1,2,3,4,5,6,10,11,12,13,14])

for i in range(3):
    q_bIforce[i]=q_bI[i]*distance_lstI[i]
    q_bIforcez[i]=q_bIforce[i]*np.abs((coordinatez(cellI(i+1))-coordinatez(cellI(i+1)))/distance_lstI(i))
    q_bIforcey[i]=q_bIforce[i]*np.abs((coordinatey(cellI(i+1))-coordinatey(cellI(i+1)))/distance_lstI(i))
    A11=q_bIforcez[i]*distance_midpointI_y[i]+q_bIforcey[i]*distance_midpointII_z[i]
    A21=q_bIforce[i]
for i in range(10):
    q_bIIforce[i]=q_bII[i]*distance_lstII[i]
    q_bIIforcez[i]=q_bIIforce[i]*np.abs((coordinatez(cellII(i+1))-coordinatez(cellII(i+1)))/distance_lstII(i))
    q_bIIforcey[i]=q_bIIforce[i]*np.abs((coordinatey(cellII(i+1))-coordinatey(cellII(i+1)))/distance_lstII(i)) 
    A12=q_bIIforcez[i]*distance_midpointII_y[i]+q_bIIforcey[i]*distance_midpointII_z[i]

    



# =============================================================================
# 
# =============================================================================

            
        