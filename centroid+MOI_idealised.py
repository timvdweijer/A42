import numpy as np
#import rest


def centroid(boomarea, z_pos, n_step):

    '''boomarea is an array with dimensions(n_steps,n_booms)
       z_pos is an array with dimensions(n_booms)
       n_step is the number of iterations along the x-axis of the aileron'''


    numlst = []
    i = 0
    B = boomarea
    centroid_z_pos = np.zeros(n_step)
    centroid_y_pos = 0
    while i < n_step:
        j = 0
        while j < len(boomarea[i]):
            numlst.append((B[i][j]) * (z_pos[j]))
            den = sum(B[i])
            j += 1
        centroid_z_pos[i] = sum(numlst) / den
        i += 1
    return centroid_y_pos, centroid_z_pos


def i_yy(n_booms, boomarea, centroid_z_pos, boom_z_pos, n_step):

    '''n_booms is the number of booms
       boomarea is an array with dimensions(n_steps,n_booms)
       centroid_z_pos is an array with dimensions(n_steps)
       boom_z_pos is an array with dimensions(n_booms)
       n_step is the number of iterations along the x-axis of the aileron'''

    j = 0
    i_yy_lst = np.zeros((n_step, n_booms))
    i_yy = np.zeros(n_step)

    while j < n_step:

        for i in range(n_booms):
            i_yy_lst[j][i] = (boomarea[j][i]) * ((boom_z_pos[i] - centroid_z_pos[j]) ** 2)

        i_yy[j] = sum(i_yy_lst[j])
        j += 1

    return i_yy


def i_zz(n_booms, boomarea, centroid_y_pos, boom_y_pos, n_step):

    '''n_booms is the number of booms
       boomarea is an array with dimensions(n_steps,n_booms)
       centroid_z_pos is an array with dimensions(n_steps)
       boom_z_pos is an array with dimensions(n_booms)
       n_step is the number of iterations along the x-axis of the aileron'''

    j = 0
    i_zz_lst = np.zeros((n_step, n_booms))
    i_zz = np.zeros(n_step)

    while j < n_step:

        for i in range(n_booms):
            i_zz_lst[j][i] = (boomarea[j][i]) * ((boom_y_pos[i] - centroid_y_pos[j]) ** 2)

        i_zz[j] = sum(i_zz_lst[j])
        j += 1

    return i_zz


