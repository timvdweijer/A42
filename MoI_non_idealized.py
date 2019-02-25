import constants
from coordinates import *
import math

a = coordinate(constants.C_a, constants.h/2, constants.n_st)

stringercoordsy = a[0]
stringercoordsz = a[1]
l_straight = a[2]
alpha = a[3]

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

den_lst.append(constants.t_sp*constants.h)

centroid_y = 0
centroid_z = sum(num_lst)/sum(den_lst)

#Moments of Inertia ABOUT CENTROID

I_yy_lst = []
for i in range(n_st):
    I_yy_lst.append(A_st*(stringers[i].zcoord-centroid_z)**2)   #only steiner term, ask
Iyy_stringers = sum(I_yy_lst)
Iyy_skin =   2*((constants.t_sk*l_straight**3 * (math.cos(math.radians(constants.theta) - alpha))**2 )/12 + 
                       constants.t_sk* l_straight* (-(math.cos(math.radians(constants.theta) - alpha)* l_straight/2)- centroid_z)**2) #moment of inertia of straights_skin (moment of inertia under angle + steiner)*2 as upper and lower are the exact same
Iyy_spar = constants.t_sp * constants.h * (0- centroid_z)**2 #spar only consists of steiner term due to thin walled assumption
Iyy_semicircle = math.pi * (constants.h /2)**3 *constants.t_sk / 2 + (math.pi*constants.h / 2 *constants.t_sk) * (constants.h/math.pi - centroid_z)**2 #circular section see page 489 for equation and ask tim   https://www.engineering.com/Library/ArticlesPage/tabid/85/ArticleID/109/Centroids-of-Common-Shapes.aspx
I_yy = Iyy_stringers + Iyy_skin + Iyy_spar + Iyy_semicircle

I_zz_lst = []
for i in range(n_st):
    I_zz_lst.append(A_st*(stringers[i].ycoord-centroid_y)**2)   #only steiner term, ask
Izz_stringers = sum(I_zz_lst)
Izz_skin = 2*((constants.t_sk*l_straight**3 * (math.sin(math.radians(constants.theta) - alpha))**2 )/12 + 
                       constants.t_sk* l_straight* (math.sin(math.radians(constants.theta) - alpha)* l_straight/2)**2) #moment of inertia of straights_skin (moment of inertia under angle + steiner)*2 as upper and lower are the exact same
Izz_spar= (constants.t_sp * constants.h**3) / 12 #spar
Izz_semicircle = math.pi * (constants.h /2)**3 *constants.t_sk / 2 #circular section see page 489 for equation
I_zz = Izz_stringers + Izz_skin + Izz_spar + Izz_semicircle

I_zy = 0

