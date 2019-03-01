# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:22:49 2019

@author: user
"""

from Validation import *
import numpy as np

table = np.genfromtxt("CRJ700_ULC1.rpt", skip_header= 19, skip_footer=30)
node_n = table[:,0]
d_mag = table[:,5]
d_x = table[:,6]
d_y = table[:,7]
d_z = table [:,8]

defl= np.column_stack((node_n,d_mag,d_x,d_y,d_z))

y_defle = []
y_defte=[]
# for i in range (len(defl)):
#     for j in range(len(le_number)):
#         if defl[i,0] == le_number[j]:
#             y_def.append(defl[i,3])
# =============================================================================
            

for i in range(len(le_number)):
    y_defle.append(defl[le_number[i],3])
for i in range(len(te_number)):
    y_defte.append(defl[te_number[i],3])
    
import matplotlib.pyplot as plt
plt.figure(2)
plt.scatter(xle, y_defle)
#ilist= []
#
#for i in range(len(defl)):
#    for j in range(len(n_number)):
#        if defl[i,0] == n_number[j]:
#            ilist.append(defl[i,:])
#            
