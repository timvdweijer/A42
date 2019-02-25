# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#shear forces and moment diagrams along x-axis

import numpy as np
from constants import * 
import matplotlib.pyplot as plt
import reactionforces


def heaviside(x1):
    if x1 < 0:
        return 0
    elif x1 >= 0:
        return 1
        
    


step=0.001

R1v= reactionforces.F_1V
R1w=reactionforces.F_1W
R2v=reactionforces.F_2V
R2w=reactionforces.F_2W
R3v=reactionforces.F_3V
R3w=reactionforces.F_3W
Ract1=reactionforces.F_act

Sy=[]
Sx=[]
Sz=[]
Mz=[]
My=[]
rad = np.radians(theta)

for x in np.arange(0, l_a+step, step):
#Shear Forces
    Sy.append(q*np.cos(rad)*x-R1v*heaviside(x-x_1)-Ract1*np.sin(rad)*heaviside(x-(x_2-(x_a/2)))-R2v*heaviside(x-x_2)+P*np.sin(rad)*heaviside(x-(x_2+(x_a/2)))-R3v*heaviside(x-x_3))

    Sz.append(-q*np.sin(rad)*x-R1w*heaviside(x-x_1)-Ract1*np.cos(rad)*heaviside(x-(x_2-x_a/2))+P*np.cos(rad)*heaviside(x-(x_2+x_a/2))-R2w*heaviside(x-x_2)-R3w*heaviside(x-x_3))

#Moments
    My.append((q*np.sin(rad))*((x**2)/2)+R1w*(x-x_1)*heaviside(x-x_1)+R2w*(x-x_2)*heaviside(x-x_2)+R3w*(x-x_3)*heaviside(x-x_3)-P*np.cos(rad)*(x-x_2+x_a/2)*heaviside(x-x_2+x_a/2)+Ract1*np.cos(rad)*(x-(x_2-x_a/2))*heaviside(x-(x_2-x_a/2)))
    
    Mz.append(-1*(q * np.cos(rad))*((x**2)/2)+R1v*heaviside(x-x_1)*(x-x_1)+R2v*heaviside(x-x_2)*(x-x_2)+R3v*heaviside(x-x_3)*(x-x_3)+Ract1*np.sin(rad)*heaviside(x-(x_2-x_a/2))*(x-(x_2-x_a/2))-P*np.sin(rad)*heaviside(x-(x_2+x_a/2))*(x-(x_2+x_a/2)))


x = np.arange(0, l_a+step, step)
#Torque

#Deflections

#plots
plt.figure(1)
plt.subplot(211)
plt.plot(x, Sy, x, Sz)

plt.subplot(212)
plt.axis()
plt.plot(x, My, x, Mz)
plt.show()


#Force equilibrium
#eqn1= R1x + R2x +R3x==0;
#eqn2= R1y + R2y +R3y-q*l_a ==0;
#eqn3= R1z+ R2z +P+Ract1==0;

#moment equilibrium about hinge 2
#Mz
#eqn4=-R3y*(x_3-x_2)+R1y*(x2-x1)+q*l_a*(l_a/2-x_2)==0;

#My
#eqn5=R1z*d_1+R3z*d_3+Fact1*(h_a/sqrt(2))*sin(45-theta)-P*(h_a/sqrt(2))*sin(45-theta)-q*0.25*C_a*cos(theta)
#Start moment curvature integration
#ycurvature=-1/(E*(Izz*Iyy-Izy^2))*[My*Iyy-Mz*Izy]
#zcurvature=-1/(E*(Izz*Iyy-Izy^2))*[Mz*Izz-My*Izy]

#Solve equation for y
#yslope=simplify(integrate(ycurvature,x));
#ydeflection=simplify(integrate(yslope,x));

#eqn7=ydeflection.subs(x:x_1)+K1*x_1+K2==d_1
#eqn8=ydeflection.subs(x:x_2)+K1*x_2+K2==d_2
#eqn9=ydeflection.subs(x:x_3)+K1*x_3+K2==d_3

#9 unknowns: Ry1, Ry2, Ry3, Rz1, Rz2, Rz3, Ract1, K1, K2
#9 equations: SumFy, SumFz, SumMz, SumMy, Eqn7, Eqn8, Eqn9

