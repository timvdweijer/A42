import constants
import coordinates
import math

a = coordinate(constants.C_a, constants.h/2, constants.n_st)

stringercoordsy = a[0]
stringercoordsz = a[1]

class stringer:

    def __init__(self, zcoord, ycoord):
        self.zcoord = zcoord
        self.ycoord = ycoord

stringers = []

for i in range(len(stringercoordsz)):
    stringers.append(stringer(stringercoordsz[i],stringercoordsy[i]))

A_st = constants.w_st * constants.t_st + constants.h_st * constants.t_st
n_st = 15
num_lst = []
den_lst = []

for i in range(n_st):                                   #centroid of aileron
    num_lst.append(stringers[i].zcoord * A_st)
    den_lst.append(A_st)

num_lst.append(2*(constants.h/math.pi)*constants.t_sk*math.pi*0.5*constants.h*0.5)  #contribution of 2 quarter circles
den_lst.append(math.pi*constants.h*0.5*constants.t_sk)

num_lst.append(2*constants.t_sk*math.sqrt((constants.h*0.5)**2+(constants.C_a-constants.h*0.5)**2)*
               math.sqrt((constants.h*0.5)**2+(constants.C_a-constants.h*0.5)**2)*0.5*(-1)*math.cos(math.atan2(constants.h*0.5,constants.C_a-constants.h*0.5))) #contribution of straight parts
den_lst.append(constants.t_sk*math.sqrt((constants.h*0.5)**2+(constants.C_a-constants.h*0.5)**2))

centroid_y = 0
centroid_z = sum(num_lst)/sum(den_lst)

#Moments of Inertia ABOUT CENTROID

I_yy_lst = []
for i in range(n_st):
    I_yy_lst.append(A_st*(stringers[i].zcoord-centroid_z)**2)
I_yy = sum(I_yy_lst)

I_zz_lst = []
for i in range(n_st):
    I_zz_lst.append(A_st*(stringers[i].ycoord-centroid_y)**2)
I_zz = sum(I_zz_lst)

#### ADD terms for semicircle, spar and thin plates

print(I_yy)
print(I_zz)




