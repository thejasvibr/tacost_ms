# -*- coding: utf-8 -*-
"""Calculate distances to points and compare how the simulated points match 
the obtained TOADSuite points. 

Notes
-----
1) Some coordinate system transformations need to be done between TOADSuite and 
simulated positions - check again. 
Created on Thu Jun 11 14:08:53 2020

Acknowledgements
---------------
Thanks to Lena De Framond for running the simulated audio files on TOADSuite.

@author: tbeleyur
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
import pandas as pd
import scipy.spatial

def calculate_euclidean_error(row_xyz):
    '''
    '''
    return np.sqrt(np.sum(row_xyz**2.0))


def draw_mic_array(mic_xyz, draw_axis):
    for i, each in enumerate(mic_xyz):
        for j,every in enumerate(mic_xyz):
            mic_line = np.row_stack((each,every))
            draw_axis.plot(mic_line[:,0],mic_line[:,1],mic_line[:,2],'k', linewidth=0.5)
    return draw_axis
        

#### Tristar points
# load the simulated points:
tristar_point = pd.read_csv('../tristar_source_positions.csv')
# load the obtained output
toadsuite_out = pd.read_excel('../toadsuite_results/RES_fig1_tristar.xlsx', sheet_name='0000001_001')
toadsuite_xyz = toadsuite_out.iloc[3:,[15,16,17]].copy()

##### Cave array points
cave_points = pd.read_csv('../cave_source_positions.csv')
toadsuite_cave = pd.read_excel('../toadsuite_results/RES_fig2_cave.xlsx', sheet_name='0000002_001')
toadsuite_cave_xyz = toadsuite_cave.iloc[3:,[15,16,17]].copy()

cave_diff = np.abs(cave_points.to_numpy() - toadsuite_cave_xyz.to_numpy())
cave_euclidean_error = np.apply_along_axis(calculate_euclidean_error, 1, cave_diff)

norm_error = cave_euclidean_error/np.min(cave_euclidean_error)

cave_mics = pd.read_csv('../cave_survey_without_mic_index.csv')
cave_mics_xyz = cave_mics.to_numpy()
cave_xyz = cave_points.to_numpy()


plt.figure()
ax2 = plt.subplot(111, projection='3d')
ax2.scatter(cave_xyz[:,0],cave_xyz[:,1],cave_xyz[:,2],'*', s=norm_error*25)
ax2.scatter(cave_mics_xyz[:,0], cave_mics_xyz[:,1],cave_mics_xyz[:,2],marker=11,)
ax2.view_init(elev=41., azim=166)
draw_mic_array(cave_mics_xyz[:4,:],ax2)
draw_mic_array(cave_mics_xyz[4:8,:],ax2)
draw_mic_array(cave_mics_xyz[7:,:],ax2)

