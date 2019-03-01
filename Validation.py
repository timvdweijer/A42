# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:01:22 2019

@author: Harold
"""

import numpy as np

# Read a file
f = open("CRJ700-19.inp","r") # Open file for reading
lines = f.readlines()
f.close()

a = []
c = []
d = np.zeros((3196,4))

# Check every line in the list lines

for line in lines:
    if not line[0] == '*':
        a.append(line)
        #print(line)
        if len(a) > 3195:       # make a list 'a' containing a string of the x,y and z coordinates for each node (3196 nodes)
            break
for j in range(len(a)):
    b = (a[j].split(','))
    for i in range(len(b)):
        d[j][i] = (float(b[i]))     # make an array with node number, x, y and z coordinate as a float
#print(d)

xlist = []                      #list with x-coordinates of the nodes

for k in range(3196):
    xlist.append(d[k][1])
#print(xlist)

ylist = []                      #list with y-coordinates of the nodes

for l in range(3196):
    ylist.append(d[l][2])
#print(ylist)

zlist = []                      #list with z-coordinates of the nodes

for m in range(3196):
    zlist.append(d[m][3])
#print(zlist)

#only for TE and LE

xte = []
yte = []
zte = []
# =============================================================================
# n_number = []
# =============================================================================

xle = []
yle = []
zle = []
le_number=[]
te_number=[]



for i in range(len(ylist)):
    if ylist[i]==0 and zlist[i]>0:
        le_number.append(i+1)
        xle.append(xlist[i])
        yle.append(ylist[i])
        zle.append(zlist[i])      
        
for i in range(len(ylist)):
    if ylist[i]==0 and zlist[i]<0:
        te_number.append(i+1)
        xte.append(xlist[i])
        yte.append(ylist[i])
        zte.append(zlist[i])      
# =============================================================================
# for z in range(len(ylist)):
#     if ylist[z] == 0 and not zlist[z] == 0:
#         n_number.append(z+1)
#         xte.append(xlist[z])
#         yte.append(ylist[z])
#         zte.append(zlist[z])
# =============================================================================
        


#plot

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)

s = ax.scatter(xte,yte,zte)

plt.show()



'''for line in lines:
# Make case-tolerant: make lower case
    txt = line.lower()
# Check for comment line or a blank line
    if txt[0] == '*' and not txt.strip()== "" :
        words = txt.split("=")
        label = words[0].strip() # remove spaces at the start
        value = words[1].strip() # and end of string
# Lots of checks for “[ ]” and “\n” at end of line
        i = value.find('[')
        if i>=0:
            value = value[:i]
        else:
            if value[-2:]=="\n":
                value = value[:-2]
# if a value is given: read it
        if value=="":
            x=float(value)
            print (label," = ",x)
            nlist.append([label,x])'''


