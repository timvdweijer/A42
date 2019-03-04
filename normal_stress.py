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

def normalstress(My, Mz, Iyy, Izz, y_coordinate, z_coordinate, centroid_y, centroid_z, n_stringers, C_a, h):
    stress_lst = np.zeros((len(My),15))
    for i in range(0, len(My)):
        #local_stresses = []
        vMTE = []
        for j in range(0, n_stringers + 2):
            y_tocentroid = y_coordinate[j]- centroid_y  
            z_tocentroid = z_coordinate[j] - centroid_z  
            stress_boom = ((Mz[i]*Iyy)*(y_tocentroid) + (My[i]*Izz)*(z_tocentroid))/ (Izz*Iyy)
            #local_stresses.append(stress_boom)
            stress_lst[i][j] = stress_boom
            vMTE.append(float(((Mz[i]*Iyy)*(0 - centroid_y) + (My[i]*Izz)*(-1*(C_a - h/2) - centroid_z))/ (Izz*Iyy)))
        #stress_lst.append(local_stresses)
    return stress_lst, vMTE   #, My

norm_stress = normalstress(bendingsheardiagrams.My, bendingsheardiagrams.Mz,\
                 MoI_non_idealized.I_yy, MoI_non_idealized.I_zz, \
                 coordinates.a[0], coordinates.a[1], 
                 MoI_non_idealized.centroid_y, MoI_non_idealized.centroid_z,\
                 constants.n_st, constants.C_a, constants.h /2.)    
