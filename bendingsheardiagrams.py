# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#shear forces and moment diagrams along x-axis

import numpy as np
from constants import * 
import matplotlib.pyplot as plt



step=0.001
x = np.arange(0, l_a+step, step)
# =============================================================================
# R1v=1
# R1w=1
# R2v=1
# R2w=1
# R3v=1
# R3w=1
# Ract1=1
# 
# #Shear Forces
# Sy=q*np.cos(theta)*x-R1v*np.heaviside(x-x_1)-Ract1*np.heaviside(x-(x_2-(X_a/2)))-R2y*np.heaviside(x-x_2)+P*np.heaviside(x-(x_2+(X_a/2)))-R3y*np.heaviside(x-x_3)
# 
# Sz=-q*np.sin(theta)*x+R1w*np.heaviside(x-x_1)-Ract1*np.cos(theta)*np.heaviside(x-(x_2-x_a/2))+P*np.cos(theta)*np.heaviside(x-(x_2+x_a/2)+R2w*np.heaviside(x-x_2)+R3w*np.heaviside(x-x_3)
# 
# #Moments
# #Mz=((-q*np.cos(theta))**2)*(x/2)+R1v*np.heaviside(x-x_1)*(x-x_1)+R2v*np.heaviside(x-x_2)*(x-x_2)+R3v*np.heaviside(x-x_3)*(x-x_3)+Ract1*np.sin(theta)*np.heaviside(x-(x_2-X_a/2))*(x-(x_2-X_a/2))-P*np.sin(theta)*np.heaviside(x-(x_2+X_a/2))*(x-(x_2+X_a/2))
# 
# My=-((q*np.sin(theta))**2)*(x/2)+R1w*(x-x_1)*np.heaviside(x-x_1)+R2w*(x-x_2)*np.heaviside(x-x_2)+R3w*(x-x_3)*np.heaviside(x-x_3)+P*np.cos(theta)*(x-x_2+x_a/2)*np.heaviside(x-x_2+x_a/2)-React1*np.cos(theta)*(x-(x_2-x_a/2))*heaviside(x-(x_2-x_a/2))
# 
# #Torque
# 
# #Deflections
# 
# #plots
# plt.figure(1)
# plt.subplot(211)
# plt.plot(x, Sy, 'S-y', x, Sz, 'S-z')
# 
# plt.subplot(212)
# plt.plot(x, My , 'M-y', x, Mz, 'S-z')
# plt.show()
# 
# 
# #Force equilibrium
# #eqn1= R1x + R2x +R3x==0;
# #eqn2= R1y + R2y +R3y-q*l_a ==0;
# #eqn3= R1z+ R2z +P+Ract1==0;
# 
# #moment equilibrium about hinge 2
# #Mz
# #eqn4=-R3y*(x_3-x_2)+R1y*(x2-x1)+q*l_a*(l_a/2-x_2)==0;
# 
# #My
# #eqn5=R1z*d_1+R3z*d_3+Fact1*(h_a/sqrt(2))*sin(45-theta)-P*(h_a/sqrt(2))*sin(45-theta)-q*0.25*C_a*cos(theta)
# #Start moment curvature integration
# #ycurvature=-1/(E*(Izz*Iyy-Izy^2))*[My*Iyy-Mz*Izy]
# #zcurvature=-1/(E*(Izz*Iyy-Izy^2))*[Mz*Izz-My*Izy]
# 
# #Solve equation for y
# #yslope=simplify(integrate(ycurvature,x));
# #ydeflection=simplify(integrate(yslope,x));
# 
# #eqn7=ydeflection.subs(x:x_1)+K1*x_1+K2==d_1
# #eqn8=ydeflection.subs(x:x_2)+K1*x_2+K2==d_2
# #eqn9=ydeflection.subs(x:x_3)+K1*x_3+K2==d_3
# 
# #9 unknowns: Ry1, Ry2, Ry3, Rz1, Rz2, Rz3, Ract1, K1, K2
# #9 equations: SumFy, SumFz, SumMz, SumMy, Eqn7, Eqn8, Eqn9
#       
#       
# =============================================================================
