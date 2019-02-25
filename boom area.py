#import everything
import numpy as np



def boomarea(A_stringer,t_skin,t_spar,d,l_spar,d_boom5spar,d_boom6spar,normalstress,n_step):        # ( stringer area, skin thickness, spar thickness,
                                                                                                    # distance between stringers, spar length, distance between
                                                                                                    # stringer 5 and spar, distance between stringer 6 and spar,
                                                                                                    # normalstress array, number of steps along x-axis aileron

    j = 0
    B = np.zeros(normalstress.shape)
    while j < n_step:


        for i in range(4):
            B[j][i] = A_stringer + ((t_skin*d)/6) * (2 + normalstress[j][i+1]/normalstress[j][i]) + ((t_skin*d)/6) * (2 + normalstress[j][i-1]/normalstress[j][i])
        for i in range(11,14):
            B[j][i] = A_stringer + ((t_skin*d)/6) * (2 + normalstress[j][i+1]/normalstress[j][i]) + ((t_skin*d)/6) * (2 + normalstress[j][i-1]/normalstress[j][i])
        for i in range(14,15):
            B[j][i] = A_stringer + ((t_skin * d) / 6) * (2 + normalstress[j][0] / normalstress[j][i]) + ((t_skin * d) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
        for i in range(7,8):
            B[j][i] = A_stringer + ((t_skin*d)/6) * (2 + normalstress[j][i+1]/normalstress[j][i]) + ((t_skin*d)/6) * (2 + normalstress[j][i-1]/normalstress[j][i])
    # booms next to spar (short side)
        for i in range(4,5):
            B[j][i] = A_stringer + ((t_skin*d_boom5spar)/6) * (2 + normalstress[j][i+1]/normalstress[j][i]) + ((t_skin*d)/6) * (2 + normalstress[j][i-1]/normalstress[j][i])
        for i in range(10,11):
            B[j][i] = A_stringer + ((t_skin*d) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_skin * d_boom5spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
    #booms next to spar (long side)
        for i in range(6,7):
            B[j][i] = A_stringer + ((t_skin * d) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
        for i in range(8,9):
            B[j][i] = A_stringer + ((t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_skin * d) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
    #spar
        for i in range(7,8):
            B[j][i] = ((t_skin * d_boom5spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i]) + ((t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_spar * l_spar) / 6) * (2 + normalstress[j][9] / normalstress[j][5])
        for i in range(9,10):
            B[j][i] = ((t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i]) + ((t_skin * d_boom5spar) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_spar * l_spar) / 6) * (2 + normalstress[j][5] / normalstress[j][9])

        j += 1

    return B

print(boomarea(5,2,3,4,4.5,1,3,np.array([[1,7,3,4,5,6,7,8,-7,-6,-5,-4,-3,-2,-1],[6,5,4,3,2,1,0.5,6,7,8,-7,-6,-5,-4,-3]]),2))        #example for two spanwise steps and random properties

