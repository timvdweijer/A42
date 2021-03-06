
from coordinates import (cellI_z, cellII_z,  cellI_y, cellII_y, dst_I, dst_II, a)
import numpy as np
import boom_area
from constants import *
import centroid_MOI_ideal as cmi
import itertools as it
import bendingsheardiagrams
from math import *
from Torsion import (q_T)
import normal_stress
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def base_shear(coordinatesy, coordinatesz, Izz, Iyy, centroidy, centroidz, boomarea, Sy, Sz):
    """
    cell II compute base shear flow (straight part)
    """ 

    q_cellI = [(np.zeros(5)).tolist()]
    q_cellII = [(np.zeros(12)).tolist()]

    for j in range(1, len(Sy)):
        q_ij_lst_cellII = []
        for i in range(0,11 ):                                                   #horizontal and vertical shear force contributions; split up as right beams has to be used
            if i <=5:
                d_q_ij =   - Sy[j] * boomarea[j][i] / Izz[j] * (coordinatesy[i] - centroidy[j]) \
                - Sz[j] * boomarea[j][i] / Iyy[j] * (coordinatesz[i] - centroidz[j])                       
            else: 
                d_q_ij =   - Sy[j] * boomarea[j][i + 3] / Izz[j] * (coordinatesy[i + 3] - centroidy[j]) \
                - Sz[j] * boomarea[j][i + 3] / Iyy[j] * (coordinatesz[i + 3] - centroidz[j])                   
            
            if i == 0:
                q_ij_lst_cellII.append(0)                                                              #make list for the q's of the skin of that particular locations
                q_ij_lst_cellII.append(d_q_ij[0])
            else:
                q_ij_lst_cellII.append(d_q_ij[0] + q_ij_lst_cellII[-1])
        """
        Cell I compute base shear flow (semi_circle)
        """
        q_ij_lst_cellI = []
        for i in range(0,4):
            if i <=2:                                                               
                d_q_ij =   - Sy[j] * boomarea[j][i + 6] / Izz[j] * (coordinatesy[i + 6] - centroidy[j]) \
                - Sz[j] * boomarea[j][i + 6] / Iyy[j] * (coordinatesz[i + 6] - centroidz[j])                        
            else: 
                d_q_ij =   - Sy[j] * boomarea[j][5] / Izz[j] * (coordinatesy[5] - centroidy[j]) \
                - Sz[j] * boomarea[j][5] / Iyy[j] * (coordinatesz[5] - centroidz[j]) 
            
            if i == 0:
                q_ij_lst_cellI.append(0)                                                                #make list for the q's of the skin of that particular locations
                q_ij_lst_cellI.append(d_q_ij[0])
            else:
                q_ij_lst_cellI.append((d_q_ij[0] + q_ij_lst_cellI[-1]).tolist()) 
        q_cellI.append(q_ij_lst_cellI)
        q_cellII.append(q_ij_lst_cellII)
        
    return (q_cellI, q_cellII )
        
baseshear = base_shear(a[0], a[1], (cmi.izz).tolist() , (cmi.iyy).tolist() ,(cmi.c[0]).tolist() ,(cmi.c[1]).tolist() , (boom_area.boomareas).tolist(), bendingsheardiagrams.Sy, bendingsheardiagrams.Sz)
#shearcentre =  base_shear(a[0], a[1], cmi.izz , cmi.iyy ,cmi.c[0] ,cmi.c[1] , boom_area.boomareas, bendingsheardiagrams.Sy, np.zeros(np.shape(bendingsheardiagrams.Sz)))

def redundantshearflow(q_I, q_cellII, coordinatesy, coordinatesz, mcoordinatesy, mcoordinatesz, Sy, dst_I, dst_II ):
    #redundantshearflow:
    cellI=[7,8,9,10,6]
    cellII=[0,1,2,3,4,5,6,10,11,12,13,14]
    
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
    enclosed_area_2 = (C_a- h/2) * h                                         #enclosed areas of cell 2 
    redundant = []
        #system of equations for qs0
    for j in range(0, len(Sy)):
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
        A22II=[]       
        for i in range(5): #iteration in cell 1
            q_bIforce.append(q_cellII[j][i]*dst_I[i]) 
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
    
        A=  [[2* enclosed_area_1   , 2*enclosed_area_2] ,[np.sum(A21I) + (1/(2*enclosed_area_2*G)*(dst_II[6]/thickII[6])) ,-1*(np.sum(A22II)+ (1/(2*enclosed_area_1*G)*(dst_I[4]/thickI[4])))]]
        C=  [[-1*(np.sum(C11I) + np.sum(C12II))], [-1*np.sum(C12II)/(2*enclosed_area_1*G)+np.sum(A22II)/(2*enclosed_area_2*G)]]
        redundant.append(np.linalg.solve(A,C).tolist()) 
        redundant2 = []
        for j in range(len(redundant)):
            redundant2.append([float(redundant[j][0][0]), float(redundant[j][1][0])])
    return redundant2
redundantshear = redundantshearflow(baseshear[0], baseshear[1], a[0], a[1], a[-2], a[-1], bendingsheardiagrams.Sy, dst_I, dst_II)

def totalshearflow(q_cellI,q_cellII, Sy, q_T, redundantshear):
    qtotI=[]
    qtotII=[]
    for j in range(0, len(Sy)):
        qtotI_lst = []
        qtotII_lst = []
        for i in range(len(q_cellI[j])):
            qtotI_lst.append(q_cellI[j][i]+ redundantshear[j][0]-q_T[j][0])
        for i in range(len(q_cellII[j])):
            qtotII_lst.append(q_cellII[j][i]+redundantshear[j][1]-q_T[j][1])
        qtotII_lst[6]=qtotII_lst[6]-qtotI_lst[4]
        qtotI.append(qtotI_lst)
        qtotII.append(qtotII_lst)
    return [qtotI, qtotII]
totalshears=totalshearflow(baseshear[0], baseshear[1], bendingsheardiagrams.Sy, q_T, redundantshear)

def shearstress(qtotI, qtotII, t_sk, t_sp, Sy):
    shear_stress = []
    shear_spar = []
    for j in range(0, len(Sy)):
        qstress_skin=[]        
        for i in (0,1,2,3,4,5):
            qstress_skin.append(qtotII[j][i]/t_sk)
        for i in (0,1,2,3):
            qstress_skin.append(qtotI[j][i]/t_sk)
        for i in (7,8,9,10,11):
            qstress_skin.append(qtotII[j][i]/t_sk)
        shear_stress.append(qstress_skin)
        shear_spar.append(qtotII[j][6]/t_sp)
        
    return [shear_stress, shear_spar]
shear_stress=shearstress(totalshears[0], totalshears[1], t_sk, t_sp, bendingsheardiagrams.Sy )           


def vMises(normalstress, shear_stress, coordinatesy, coordinatesz):
    mises_lst = []
    x = []
    for i in range(0,len(normalstress)):
        mises = []
        for j in range(0, len(coordinatesy)):
            if j == 14:
                mises.append( sqrt((normalstress[i][j])**2 + 3*((shear_stress[0][i][j]/(1*10**6) + shear_stress[0][i][0]/(1*10**6))/2)**2))
            elif j == 5 or j == 9:
                mises.append(sqrt((normalstress[i][j])**2 + 3*((shear_stress[0][i][j]/(1*10**6) + shear_stress[0][i][j + 1]/(1*10**6) + shear_stress[1][i]/(1*10**6))/3)**2))
            else:
                mises.append(sqrt((normalstress[i][j])**2 + 3*((shear_stress[0][i][j]/(1*10**6) + shear_stress[0][i][j + 1]/(1*10**6))/2)**2))
        x.append(i/1000)
        mises_lst.append(mises)
    return [mises_lst, x, coordinatesy, coordinatesz]
mises = vMises(normal_stress.norm_stress[0]/(1*10**6), shear_stress, a[0], a[1])
  
