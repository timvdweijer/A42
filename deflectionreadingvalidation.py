# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:22:49 2019

@author: user
"""

from Validation import *
import numpy as np

table = np.genfromtxt("CRJ700_ULC1.rpt", skip_header= 19, skip_footer=30)
node_n = table[:,0]
d_mag = table[:,5]
d_x = table[:,6]
d_y = table[:,7]
d_z = table [:,8]


