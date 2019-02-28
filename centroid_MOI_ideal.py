import numpy as np
import boom_area
import coordinates
import bendingsheardiagrams as bsd
import MoI_non_idealized as Mni

def centroid(boomarea, y_pos, z_pos ,n_step):                   #for centroid of idealized structure, we assume the same centroid as for the non-idealized structure

    centroid_z_pos = np.ones(n_step) 
    centroid_y_pos = np.ones(n_step)

    i = 1
    while i < n_step:
        numlst_z = []
        numlst_y = []
        j = 0
        while j < len(boomarea[i]):
            numlst_z.append((boomarea[i][j]) * (z_pos[j]))
            numlst_y.append((boomarea[i][j]) * (y_pos[j]))
            j += 1
        den = sum(boomarea[i])
        centroid_z_pos[i] = sum(numlst_z) / den
        centroid_y_pos[i] = sum(numlst_y) / den
        i += 1


    return centroid_y_pos, centroid_z_pos

c = centroid(boom_area.boomareas, coordinates.a[0], coordinates.a[1],  len(bsd.Sy))


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

iyy = i_yy(15,boom_area.boomareas,c[1],coordinates.a[1],len(bsd.Sy))


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

izz = i_zz(15,boom_area.boomareas,c[0],coordinates.a[0],len(bsd.Sy))

# =============================================================================
# import numpy as np
# import boom_area
# import coordinates
# import bendingsheardiagrams as bsd
# 
# def centroid(boomarea, z_pos, y_pos, n_step):
# 
#     '''boomarea is an array with dimensions(n_steps,n_booms)
#        z_pos is an array with dimensions(n_booms)
#        n_step is the number of iterations along the x-axis of the aileron'''
# 
# 
#     numlst_z = []
#     numlst_y = []
#     i = 0
#     B = boomarea
#     centroid_z_pos = np.zeros(n_step)
#     centroid_y_pos = np.zeros(n_step)
#     while i < n_step:
#         j = 0
#         while j < len(boomarea[i]):
#             numlst_z.append((B[i][j]) * (z_pos[j]))
#             numlst_y.append((B[i][j]) * (y_pos[j]))
#             den = sum(B[i])
#             j += 1
#         centroid_z_pos[i] = sum(numlst_z) / den
#         centroid_y_pos[i] = sum(numlst_y) / den
#         i += 1
#     return centroid_y_pos, centroid_z_pos
# 
# c = centroid(boom_area.boomareas,coordinates.a[1], coordinates.a[0], len(bsd.Sy))
# 
# 
# def i_yy(n_booms, boomarea, centroid_z_pos, boom_z_pos, n_step):
# 
#     '''n_booms is the number of booms
#        boomarea is an array with dimensions(n_steps,n_booms)
#        centroid_z_pos is an array with dimensions(n_steps)
#        boom_z_pos is an array with dimensions(n_booms)
#        n_step is the number of iterations along the x-axis of the aileron'''
# 
#     j = 0
#     i_yy_lst = np.zeros((n_step, n_booms))
#     i_yy = np.zeros(n_step)
# 
#     while j < n_step:
# 
#         for i in range(n_booms):
#             i_yy_lst[j][i] = (boomarea[j][i]) * ((boom_z_pos[i] - centroid_z_pos[j]) ** 2)
# 
#         i_yy[j] = sum(i_yy_lst[j])
#         j += 1
# 
#     return i_yy
# 
# iyy = i_yy(15,boom_area.boomareas,c[1],coordinates.a[1],len(bsd.Sy))
# 
# 
# def i_zz(n_booms, boomarea, centroid_y_pos, boom_y_pos, n_step):
# 
#     '''n_booms is the number of booms
#        boomarea is an array with dimensions(n_steps,n_booms)
#        centroid_z_pos is an array with dimensions(n_steps)
#        boom_z_pos is an array with dimensions(n_booms)
#        n_step is the number of iterations along the x-axis of the aileron'''
# 
#     j = 0
#     i_zz_lst = np.zeros((n_step, n_booms))
#     i_zz = np.zeros(n_step)
# 
#     while j < n_step:
# 
#         for i in range(n_booms):
#             i_zz_lst[j][i] = (boomarea[j][i]) * ((boom_y_pos[i] - centroid_y_pos[j]) ** 2)
# 
#         i_zz[j] = sum(i_zz_lst[j])
#         j += 1
# 
#     return i_zz
# 
# izz = i_zz(15,boom_area.boomareas,c[0],coordinates.a[0],len(bsd.Sy))
# =============================================================================

