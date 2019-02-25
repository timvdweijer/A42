# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:25:35 2019

@author: peter
"""
import numpy as np
from constants import * 
from bendingsheardiagrams import *
from boomarea import * 
import matplotlib.pyplot as plt


#13 stringers +2 spars = 15 booms
#For a cross section
#q_b = -Sy/Izz*(sum(B_r*y_r))-Sz/Iyy*(sum(B_r*z_r))
#q_s0 = -integral(q_b*ds)/(integral(ds))
#qs = q_b+q_s0



# =============================================================================
# #Calculate the open section shear flow q_B by the traditional method: make an imaginary cut along axis of symmetry for each cell.
# inertialterm_z = - (Sz * Izz - Sy * Izy) / (Izz * Iyy - Izy ** 2)
# inertialterm_y = - (Sy * Iyy - Sz * Izy) / (Izz * Iyy - Izy ** 2)
# 
# #boomclassification:
# class boomclass:
#      def __init__(self, classification):
#          self.boomclass = classification
#          
#          boom_number[0] = boomclass('noncircular')
#          boom_number[1] = boomclass('noncircular')
#          boom_number[2] = boomclass('noncircular')
#          boom_number[3] = boomclass('noncircular')
#          boom_number[4] = boomclass('noncircular')
#          boom_number[5] = boomclass('noncircular')
#          boom_number[6] = boomclass('noncircular')
#          boom_number[7] = boomclass('noncircular')
#          boom_number[8] = boomclass('noncircular')
#          boom_number[9] = boomclass('noncircular')
#          boom_number[10] = boomclass('noncircular')
#          boom_number[11] = boomclass('noncircular')
#          boom_number[12] = boomclass('noncircular')
#          boom_number[13] = boomclass('noncircular')
#          boom_number[14] = boomclass('noncircular')
#          
# 
# 
# 
# q_bI=[]
# q_bII=[]
# q_b0=0 
# q_bI.append(q_b0)
# q_bII.append(q_b0)
# for i in range (15):
#     if boom_number[i+1].boomclass=='circular':
#         q_bI.append(q_bI[-1]+inertialterm_z*boom_area(i)*coordinatez(i)+inertialterm_y*boom_area(i)*coordinatey(i))
#     else:
#         q_bII.append(q_bII[-1]+inertialterm_z*boom_area(i)*coordinatez(i)+inertialterm_y*boom_area(i)*coordinatey(i))
#         
#         
# #finding redundant shear flow:
# directionvector=[]
# totaldirection=[]
# force_in_zI=[]
# force_in_zII=[]
# force_in_yI=[]
# force_in_yII=[]
# # =============================================================================
# # for i in range(14)
# #         directionvector.append([(coordinatez(i)-coordinatez(i-1),coordinatez(i)-coordinatez(i-1)))
# #         totaldirection.append(math.sqrt((directionvector[i][0])**2+(directionvector[i][1])**2))
# #         
# # =============================================================================
# =============================================================================

        




        
        
        