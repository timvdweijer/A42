#import everything
import numpy as np
import constants
import MoI_non_idealized
import coordinates
import normal_stress


def boomarea(A_stringer,t_skin,t_spar,d,l_spar,d_boom5spar,d_boom6spar,normalstress,n_step):        
    """  ( stringer area, skin thickness, spar thickness,
        distance between stringers, spar length, distance between
        stringer 5 and spar, distance between stringer 6 and spar,
        normalstress array, number of steps along x-axis aileron
        """
    j = 0
    B = np.zeros(normalstress.shape)
    '''
    while j < n_step:
        for i in range(4):
            if normalstress[j][i] != 0:
                B[j][i] = A_stringer + ((t_skin*d)/6) * (2 + normalstress[j][i+1]/normalstress[j][i]) + ((t_skin*d)/6) * (2 + normalstress[j][i-1]/normalstress[j][i])
            else:
                B[j][i] = A_stringer + ((t_skin * d) / 6) * (2) + ((t_skin * d) / 6) * (2)
        for i in range(11,14):
            if normalstress[j][i] != 0:
                B[j][i] = A_stringer + ((t_skin*d)/6) * (2 + normalstress[j][i+1]/normalstress[j][i]) + ((t_skin*d)/6) * (2 + normalstress[j][i-1]/normalstress[j][i])
            else:
                B[j][i] = A_stringer + ((t_skin * d) / 6) * (2) + ((t_skin * d) / 6) * (2)
        for i in range(14,15):
            if normalstress[j][i] != 0:
                B[j][i] = A_stringer + ((t_skin * d) / 6) * (2 + normalstress[j][0] / normalstress[j][i]) + ((t_skin * d) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
            else:
                B[j][i] = A_stringer + ((t_skin * d) / 6) * (2) + ((t_skin * d) / 6) * (2)
        for i in range(7,8):
            if normalstress[j][i] != 0:
                B[j][i] = A_stringer + ((t_skin*d)/6) * (2 + normalstress[j][i+1]/normalstress[j][i]) + ((t_skin*d)/6) * (2 + normalstress[j][i-1]/normalstress[j][i])
            else:
                B[j][i] = A_stringer + ((t_skin * d) / 6) * (2) + ((t_skin * d) / 6) * (2)
    # booms next to spar (short side)
        for i in range(4,5):
            if normalstress[j][i] != 0:
                B[j][i] = A_stringer + ((t_skin*d_boom5spar)/6) * (2 + normalstress[j][i+1]/normalstress[j][i]) + ((t_skin*d)/6) * (2 + normalstress[j][i-1]/normalstress[j][i])
            else:
                B[j][i] = A_stringer + ((t_skin * d_boom5spar) / 6) * (2) + ((t_skin * d) / 6) * (2)
        for i in range(10,11):
            if normalstress[j][i] != 0:
                B[j][i] = A_stringer + ((t_skin*d) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_skin * d_boom5spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
            else:
                B[j][i] = A_stringer + ((t_skin * d) / 6) * (2) + ((t_skin * d_boom5spar) / 6) * (2)
    #booms next to spar (long side)
        for i in range(6,7):
            if normalstress[j][i] != 0:
                B[j][i] = A_stringer + ((t_skin * d) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
            else:
                B[j][i] = A_stringer + ((t_skin * d) / 6) * (2) + ((t_skin * d_boom6spar) / 6) * (2)
        for i in range(8,9):
            if normalstress[j][i] != 0:
                B[j][i] = A_stringer + ((t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_skin * d) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
            else:
                B[j][i] = A_stringer + ((t_skin * d_boom6spar) / 6) * (2) + ((t_skin * d) / 6) * (2)
    #spar
        for i in range(5,6):
            if normalstress[j][i] != 0:
                B[j][i] = ((t_skin * d_boom5spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i]) + ((t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_spar * l_spar) / 6) * (2 + normalstress[j][9] / normalstress[j][5])
            else:
                B[j][i] = ((t_skin * d_boom5spar) / 6) * (2) + ((t_skin * d_boom6spar) / 6) * (2) + ((t_spar * l_spar) / 6) * (2)
        for i in range(9,10):
            if normalstress[j][i] != 0:
                B[j][i] = ((t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i]) + ((t_skin * d_boom5spar) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_spar * l_spar) / 6) * (2 + normalstress[j][5] / normalstress[j][9])
            else:
                B[j][i] = ((t_skin * d_boom6spar) / 6) * (2) + ((t_skin * d_boom5spar) / 6) * (2) + ((t_spar * l_spar) / 6) * (2)   '''

    while j < n_step:
        for i in range(4):
            B[j][i] = A_stringer + ((t_skin * d) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + (
                            (t_skin * d) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
        for i in range(11, 14):
            B[j][i] = A_stringer + ((t_skin * d) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + (
                            (t_skin * d) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
        for i in range(14, 15):
            B[j][i] = A_stringer + ((t_skin * d) / 6) * (2 + normalstress[j][0] / normalstress[j][i]) + (
                            (t_skin * d) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
        for i in range(7, 8):
            B[j][i] = A_stringer + ((t_skin * d) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + (
                            (t_skin * d) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
        # booms next to spar (short side)
        for i in range(4, 5):
            B[j][i] = A_stringer + ((t_skin * d_boom5spar) / 6) * (
                            2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_skin * d) / 6) * (
                                      2 + normalstress[j][i - 1] / normalstress[j][i])
        for i in range(10, 11):
            B[j][i] = A_stringer + ((t_skin * d) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + (
                            (t_skin * d_boom5spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
        # booms next to spar (long side)
        for i in range(6, 7):
            B[j][i] = A_stringer + ((t_skin * d) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + (
                            (t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i])
        for i in range(8, 9):
            B[j][i] = A_stringer + ((t_skin * d_boom6spar) / 6) * (
                            2 + normalstress[j][i + 1] / normalstress[j][i]) + ((t_skin * d) / 6) * (
                                      2 + normalstress[j][i - 1] / normalstress[j][i])
        # spar
        for i in range(5, 6):
            B[j][i] = ((t_skin * d_boom5spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i]) + (
                            (t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + (
                                      (t_spar * l_spar) / 6) * (2 + normalstress[j][9] / normalstress[j][5])
        for i in range(9, 10):
            B[j][i] = ((t_skin * d_boom6spar) / 6) * (2 + normalstress[j][i - 1] / normalstress[j][i]) + (
                            (t_skin * d_boom5spar) / 6) * (2 + normalstress[j][i + 1] / normalstress[j][i]) + (
                                      (t_spar * l_spar) / 6) * (2 + normalstress[j][5] / normalstress[j][9])
        j += 1
    return B


ppp = boomarea(MoI_non_idealized.A_st, constants.t_sk, constants.t_sp, coordinates.a[4], constants.h,coordinates.d, (coordinates.a[4]- coordinates.d), normal_stress.norm_stress, len(normal_stress.norm_stress))

#ppp = boomarea(MoI_non_idealized.A_st, constants.t_sk, constants.t_sp, coordinates.a[4], constants.h,coordinates.d, (coordinates.a[4]- coordinates.d), normal_stress.norm_stress, len(normal_stress.norm_stress))

print(ppp)
