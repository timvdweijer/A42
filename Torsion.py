from math import *
from constants import *
import numpy as np
import coordinates
import matplotlib.pyplot as plt
from reactionforces import *

"""
Calculation of the torsion due to Fact, P and q around hinge 2 check if that's okay
these are split up in the u,v,w components of the'new' reference frame
"""
def heaviside(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1
F_act = 39.72774618*1000 
theta_r = radians(theta)                                    #convert degrees to radians
q_w = 0#sin(theta_r) * q                                      #z_component of q
q_v = cos(theta_r) * q                                      #y_component of q
P_w = cos(theta_r) * P                                  #z_component of P
P_v = sin(theta_r) * P                                      #y_component of P
Fact_w =  cos(theta_r) *  F_act                            #z_component of jammed actuator
Fact_v = sin(theta_r) * F_act                                #y_component of jammed actuator


lstep = .001                                                #define spanwise step
x = np.arange(0, l_a + lstep, lstep)                        #create array of x points spanwise
T = []
T2 = []
xx = []
for x in np.arange(0, l_a + lstep, lstep):
    T.append(-1*Fact_v * (h/2) * (heaviside(x-(x_2 - x_a / 2.))) + Fact_w * (h/2) * (heaviside(x-(x_2 - x_a / 2.))) + P_v * (h/2) * (heaviside(x-(x_2 + x_a / 2.))) - P_w * (h/2) * (heaviside(x-(x_2 + x_a / 2.))) +  q_v * x* (-1 * (0.25*C_a - h/2.)))
    xx.append(x*1000)
    T2.append(( Fact_w * (h/2) * (heaviside(x-(x_2 - x_a / 2.))) - P_w * (h/2) * (heaviside(x-(x_2 + x_a / 2.))) +  q_v * x* (-1 * (0.25*C_a - h/2.))))
    
plt.plot(xx ,T, label= "Y and Z components ")
plt.plot(xx, T2, label = "Only Y components")
plt.ylabel("Torsion [Nm]")
plt.xlabel("Span wise location with origin at wingtip close to hinge 1")
plt.legend()
plt.show()

area_1 = pi * (h/2)**2 /2                                   #enclosed areas of cell 1 and two
area_2 = (C_a- h/2) * h
s_semi = pi* h/2 / t_sk                                     #integral parts of formula of semi circle 
s_rib = h / t_sp                                            #integral parts of formula of rib 
s_TE =  coordinates.coordinate(C_a, h/2, n_st)[2]*2 / t_sk  #integral parts of formula of part with straight lines 

def shear_torque(T, s_semi, s_rib, s_TE, area_1, area_2):
    """
    find shear flow due to torsion; cell 1 is semicircular part, cell2 is TE
    deflection cell 1 = deflection cell 2 
    and T = Tcell_1 + Tcell_2 
    now you can solve #see page 613 of Megson aircraft structures
    matrix [qcell_1, qcell_2]
    s_.. = distance of element / thickness
    """
    q_T = []
    for i in range(0, len(T)):                                  #for all x as before calculate shear 1 and two
        A = np.array([[(s_semi + s_rib)/(2*area_1*G)+ (s_rib)/(2*area_2*G), -1*((s_TE + s_rib)/(2*area_2*G) + (s_rib)/(2*area_1*G))], [2*area_1, 2*area_2]])
        B = np.array([0, T[i]])
        q1_T, q2_T = np.linalg.solve(A,B)
        q_T.append([q1_T, q2_T]) 
    return q_T
q_T = shear_torque(T, s_semi, s_rib, s_TE, area_1, area_2)

def theta(q_T, lstep): #gives the angle at all location
    """split up as twist at actuator 1 is zero"""
    theta1 = [0]* (419)
    for i in range(417, -1, -1 ):
        d_theta_torque = (q_T[i][0]* (s_semi+s_rib) - q_T[i][1]*s_rib)/(2*area_1*G) * lstep
        theta1[i] = (d_theta_torque + theta1[i+1] )
    theta1.remove(0)
    theta2 = [0] 
    for i in range(419 , len(q_T[:])):
        d_theta_torque = (q_T[i][0]* (s_semi+s_rib) - q_T[i][1]*s_rib)/(2*area_1*G) * lstep #p.613 formula megson where lstep = dz
        theta2.append(d_theta_torque + theta2[i-419])
    finaltheta = theta1 +  theta2
    return (finaltheta)

theta_corrected = theta(q_T, lstep)
plt.plot(xx, theta_corrected)#, xx, T)

def displacement_calc(theta, radius, dis_TE):
    displacementLE = []
    displacementTE = []
    for j in range(0, len(theta)):
        displacementLE.append( -1*theta[j]*radius)
        displacementTE.append(theta[j]* dis_TE)
    return [displacementLE, displacementTE]
displacement = displacement_calc(theta_corrected, h/2, C_a -h/2)

#plt.plot(xx, displacement[0], xx,displacement[1])
        


