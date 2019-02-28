# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:36:28 2019

@author: timvd
"""
from coordinates import (cellI_z, cellII_z,  cellI_y, cellII_y, dst_I, dst_II, a)
import numpy as np
import boom_area
from constants import *
import centroid_MOI_ideal as cmi
import itertools as it
import bendingsheardiagrams
from math import *
from Torsion import (q_T)
def base_shear(coordinatesy, coordinatesz, Izz, Iyy, centroidy, centroidz, boomarea, Sy, Sz):
    """
    cell II compute base shear flow (straight part)
    """ 
    q_cellI = [0]
    q_cellII = [0]

    for j in range(0,len(Sy)):
        q_ij_lst_cellII = []
        for i in range(0,11 ):                                                   #horizontal and vertical shear force contributions; split up as right beams has to be used
            if i <=5:
                d_q_ij =   - Sy[j] * boomarea[j][i] / Izz[j] * (coordinatesy[i] - centroidy[j]) \
                - Sz[j] * boomarea[j][i] / Iyy[j] * (coordinatesz[i] - centroidz[j])                       
            else: 
                d_q_ij =   - Sy[j] * boomarea[j][i + 3] / Izz[j] * (coordinatesy[i + 3] - centroidy[j]) \
                - Sz[j] * boomarea[j][i + 3] / Iyy[j] * (coordinatesz[i + 3] - centroidz[j])                   
            
            if i == 0:                                                              #make list for the q's of the skin of that particular locations
                q_ij_lst_cellII.append(d_q_ij)
            else:
                q_ij_lst_cellII.append(d_q_ij + q_ij_lst_cellII[-1])
        
        """
        Cell I compute base shear flow (semi_circle)
        """
        q_ij_lst_cellI = [0]
        for i in range(0,4):
            if i <=2:                                                               
                d_q_ij =   - Sy[j] * boomarea[j][i + 6] / Izz[j] * (coordinatesy[i + 6] - centroidy[j]) \
                - Sz[j] * boomarea[j][i + 6] / Iyy[j] * (coordinatesz[i + 6] - centroidz[j])                        
            else: 
                d_q_ij =   - Sy[j] * boomarea[j][5] / Izz[j] * (coordinatesy[5] - centroidy[j]) \
                - Sz[j] * boomarea[j][5] / Iyy[j] * (coordinatesz[5] - centroidz[j])                
            
            if i == 0:                                                              #make list for the q's of the skin of that particular locations
                q_ij_lst_cellI.append(d_q_ij)
            else:
                q_ij_lst_cellI.append(d_q_ij + q_ij_lst_cellI[-1]) 
        
        q_cellI.append(q_ij_lst_cellI)
        q_cellII.append(q_ij_lst_cellII)
        
    return (q_cellI, q_cellII )
        
baseshear = base_shear(coordinates.a[0], coordinates.a[1], cmi.izz , cmi.iyy ,cmi.c[0] ,cmi.c[1] , boom_area.boomareas, bendingsheardiagrams.Sy, bendingsheardiagrams.Sz)
shearcentre =  base_shear(coordinates.a[0], coordinates.a[1], cmi.izz , cmi.iyy ,cmi.c[0] ,cmi.c[1] , boom_area.boomareas, bendingsheardiagrams.Sy, np.zeros(np.shape(bendingsheardiagrams.Sz)))



#redundantshearflow:
cellI=np.array([7,8,9,10,6])
cellII=np.array([0,1,2,3,4,5,6,10,11,12,13,14])

#edge thickness list in each cell
thickI=[0]*5
thickII=[0]*12
for i in range(4):
    thickI[i]=t_sk
thickI[4]=t_sp

for i in np.nditer(np.array([0,1,2,3,4,5, 7,8,9,10,11])):
    thickII[i]=t_sk
thickII[6]=t_sp


enclosed_area_1 = (np.pi * (h/2)**2) /2                                     #enclosed areas of cell 1 
enclosed_area_2 = ((C_a- h/2) * h)/2                                         #enclosed areas of cell 2 


    #system of equations for qs0
for j in range(len(bendingsheardiagrams.Sy)):
    q_bIforce=[]
    q_bIforcez=[]
    q_bIforcey=[]
    C11I=[]
    C21I=[]
    A21I=[]
    q_bIIforce=[]
    q_bIIforcez=[]
    q_bIIforcey=[]
    C12II=[]
    C22II=[]
    A21II=[]
    A22II=[]
    for i in range(5): #iteration in cell 1
        q_bIforce.append(q_cellI[j][i]*dst_I[i]) 
        q_bIforcez.append(q_bIforce[i]*np.absolute(coordinatesz[cellI[i]]-coordinatesz[cellI[i-1]]) / dst_I[i])  #decomposed zforces
        q_bIforcey.append(q_bIforce[i]*np.absolute(coordinatesy[cellI[i]]-coordinatesy[cellI[i-1]])/dst_I[i])  #decomposed yforces   
        C11I.append(q_bIforcez[i]*cellI_y[i]+q_bIforcey[i]*cellI_z[i])#moment of base shear flow
        C21I.append(q_bIforce[i]/thickI[i])                                       
        A21I.append((1/(2*enclosed_area_1*G))*(dst_I[i]/thickI[i]))
    
    for i in range(11):
        q_bIIforce.append(q_cellII[j][i]*dst_II[i])
        q_bIIforcez.append(q_bIIforce[i]*np.absolute(coordinatesz[cellII[i]]-coordinatesz[cellII[i-1]])/dst_II[i])
        q_bIIforcey.append(q_bIIforce[i]*np.absolute(coordinatesy[cellII[i]]-coordinatesy[cellII[i-1]])/dst_II[i])
        C12II.append(q_bIIforcez[i]*cellII_y[i]+q_bIIforcey[i]*cellII_z[i])
        C22II.append(q_bIIforce[i]/thickII[i])
        A22II.append(1/(2*enclosed_area_2*G)*(dst_II[i]/thickII[i]))

    A=  [[2* enclosed_area_1   , 2*enclosed_area_2] ,[sum(A21I) + (1/(2*enclosed_area_2*G)*(dst_II[6]/thickII[6])) ,-1*(sum(A22II)+ (1/(2*enclosed_area_1*G)*dst_I[4]/thickI[4]))]]
    C=  [[-1*(sum(C11I)+sum(C12II))], [-1*sum(C12II)/(2*enclosed_area_1*G)+sum(A22II)/(2*enclosed_area_2*G)]]

        

    redundant[j]= np.linalg.solve(A,C)
    redundant[j][0]=qs_0I[j]
    redundant[j][1]=qs_0II[j] 
    
    qtotI[j]=[]
    qtotII[j]=[]
    for i in q_cellI[j][i]:
        qtotI[j].append(q_cellI[j][i]+redundant[j][[0]]+q_T[0])
    for i in q_cellII[j][i]:
        qtotII[j].append(q_cellI[j][i]+redundant[j][[0]]+q_T[0])
        qtotII[j][6]=qtotI[j][6]-qtotII[j][4]
        
        
        
#shear stress
    qstress_skin[j]=[]
    
    for i in (0,1,2,3,4,5):
        qstress_skin[j].append(qtotII[j][i]/t_sk)
    for i in (0,1,2,3):
        qstress_skin[j].append(qtotI[j][i]/t_sk)
    for i in (7,8,9,10,11):
        qstress_skin[j].append(qtotII[j][i]/t_sk)
    
    qstress_stiffener[j]=qtotII[j][6]/t_sp
    

# =============================================================================
#     q_totI[j]=[]
#     q_totII[j]=[]
#     for i in range 5:     
#         q_totI[j].append(q_cellI[i]+qs0I[j])
#     for i in range 11:
#         q_totII[j].append(q_cellII[i]+qs0II[j])
# 
# =============================================================================

