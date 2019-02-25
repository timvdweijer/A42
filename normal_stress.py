# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:54:27 2019

@author: timvd
"""
import coordinates
import bendingsheardiagrams
import MoI_non_idealized
import constants
import numpy as np

def normalstress(My, Mz, Iyy, Izz, y_coordinate, z_coordinate, centroid_y, centroid_z, n_stringers):
    stress_lst = []
    My.tolist()
    Mz.tolist()
    for i in range(0, len(My)):
        local_stresses = []
        for j in range(0, n_stringers + 2):
            y_tocentroid = centroid_y + y_coordinate[j]
            z_tocentroid = centroid_z + z_coordinate[j]
            stress_boom = ((Mz[i]*Iyy)*(y_tocentroid) + (My[i]*Izz)*(z_tocentroid))  \
                           / (Izz*Iyy)
            local_stresses.append(stress_boom)
        stress_lst.append(local_stresses)   
    return(stress_lst, yz)

a = normalstress(bendingsheardiagrams.My, bendingsheardiagrams.Mz,\
                 MoI_non_idealized.I_yy, MoI_non_idealized.I_zz, \
                 coordinates.a[0], coordinates.a[1], 
                 MoI_non_idealized.centroid_y, MoI_non_idealized.centroid_z,\
                 constants.n_st)    
