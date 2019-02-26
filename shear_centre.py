# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:36:28 2019

@author: timvd
"""
import coordinates
import numpy as np
import boom_area


def base_shear(coordinatesy, coordiantesz, Izz, Iyy, centroidy, centroidz, boomarea, Sy, Sz):
    """
    cell II compute base shear flow
    """ 
    q_cellII = []
    for j in range(0, len(Sy)):
        q_ij_lst_cellII = []
        for i in range(0,11 ): 
            if i <=5:
                d_q_ij =   - Sy[j] * boomarea[j][i] / Izz[j] * (coordinatesy[i] - centroidy[j]) \          #vertical shearforce contribution
                - Sz[j] * boomarea[j][i] / Iyy[j] * (coordinatesz[i] - centroidz[j])                        #horizotal shearforce contribution
            else: 
                d_q_ij =   - Sy[j] * boomarea[j][i + 3] / Izz[j] * (coordinatesy[i + 3] - centroidy[j]) \          #vertical shearforce contribution
                - Sz[j] * boomarea[j][i + 3] / Iyy[j] * (coordinatesz[i + 3] - centroidz[j])                        #horizotal shearforce contribution
            
            if i == 0:                                                              #make list for the q's between all booms
                q_ij_lst_cellII.append(d_q_ij)
            else:
                q_ij_lst_cellII.append(d_q_ij + q_ij_lst_cellII[-1])

    
        """
        Cell I compute base shear flow
        """
        q_ij_lst_cellI = []
        for i in range(0,5):
            if i <=3:
                d_q_ij =   - Sy[j] * boomarea[j][i + 6] / Izz[j] * (coordinatesy[i + 6] - centroidy[j]) \          #vertical shearforce contribution
                - Sz[j] * boomarea[j][i + 6] / Iyy[j] * (coordinatesz[i + 6] - centroidz[j])                        #horizotal shearforce contribution
            else: 
                d_q_ij =   - Sy[j] * boomarea[j][i + 3] / Izz[j] * (coordinatesy[i + 3] - centroidy[j]) \          #vertical shearforce contribution
                - Sz[j] * boomarea[j][i + 3] / Iyy[j] * (coordinatesz[i + 3] - centroidz[j])
            
            if i == 0:                                                              #make list for the q's between all booms, symmetric which is supposed to be symmetric
                q_ij_lst_cellI.append(d_q_ij)
            else:
                q_ij_lst_cellI.append(d_q_ij + q_ij_lst_cellI[-1])
        
        q_cellI.append(q_ij_lst_cellI)
        q_cellII.append(q_ij_lst_cellII)
        
    return (q_cellI, q_cellII )

baseshear = base_shear(coordinates.a[0], coordinates.a[1], , , , , boom_area.boomareas, bendingsheardiagrams.Sy, bendingsheardiagrams.Sz)