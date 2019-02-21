# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from constants import * 


step=0.001
x = np.arange(0, constants.l_a+step, step)

#Shear Forces
Sy=q*x-R1y*heaviside(x-x_1)+R2y*heaviside(x-x_2)+R3y*heaviside(x-x_3))

Sz=R1z*heaviside(x-x1)+Fh*heaviside(x-x_2-x_a/2)+R2z*heaviside(x-x_2)+P*heaviside(x-x_2+x_a/2)

#Moments
Mz=-(q**2)*(x)/2+R1y*np.heaviside(x-x_1)*(x-x_1)+
R2y*np.heaviside(x-x_2)*(x-x_2)+R3y*np.heaviside(x-x_3)*(x-x_3)

My=R1z*(x-x_1)*heaviside(x-x1)+R2z*(x-x2)*heaviside(x-x_2)+R3z*(x-x3)*heaviside(x-x_3)+
P*(x-x_2+x_a/2)*heaviside(x-x_2+x_a/2)+Fh*(x-x_2-x_a/2)*heaviside(x-x_2-x_a/2)

#Force equilibrium
eqn1= R1x + R2x +R3x==0;
eqn2= R1y + R2y +R3y-q*l_a ==0;
eqn3= R1z+ R2z +P+Fh==0;

#moment equilibrium about hinge 2
#Mz
eqn4=-R3y*(x_3-x_2)+R1y*(x2-x1)+q*l_a*(l_a/2-x_2)==0;

#My
eqn4=R1z*d_1
#Start moment curvature integration
ycurvature=-1/(E*(Izz*Iyy-Izy^2))*[My*Iyy-Mz*Iyy];

#Solve equation for y
yslope=int(ycurvature,x);
ydeflection=int(yslope,x);
=
