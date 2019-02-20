import numpy as np
#import constants

stringercoordsz = [-1.,2.,2.,-1.]
stringercoordsy = [2.,1.,-1.,-2.]

class stringer:

    def __init__(self, zcoord, ycoord):
        self.zcoord = zcoord
        self.ycoord = ycoord

stringers = []

for i in range(len(stringercoordsz)):
    stringers.append(stringer(stringercoordsz[i],stringercoordsy[i]))

A_st = 5
n_st = 4
num_lst = []
den_lst = []

for i in range(n_st):
    num_lst.append(stringers[i].zcoord * A_st)
    den_lst.append(A_st)

centroid_y = 0
centroid_z = sum(num_lst)/sum(den_lst)

#Moments of Inertia about Centroid

I_yy_lst = []
for i in range(n_st):
    I_yy_lst.append(A_st*(stringers[i].zcoord-centroid_z)**2)
I_yy = sum(I_yy_lst)

I_zz_lst = []
for i in range(n_st):
    I_zz_lst.append(A_st*(stringers[i].ycoord-centroid_y)**2)
I_zz = sum(I_zz_lst)

print(I_yy)
print(I_zz)




