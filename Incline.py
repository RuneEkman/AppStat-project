#!/usr/bin/env python
# coding: utf-8
ball = [15.9, 15.82, 16.08, 15.9] #mm
rail = [5.96, 6.2, 6.0,6.11] #mm

# SIDE 1angles [[person1 measurements], [person2 measurements], ..]
angles_1_gonyo = [[76.5, 77.5], [75.5, 78.5], [76, 77.5], [75.7, 77.5]]
angles_1_app = [[77.7, 76.8], [77.6, 77.5], [79.9, 76.87], [77.8, 76.7]]

# SIDE 2 angles
angles_2_gonyo = [[76.5, 77.0], [77.0, 76.0], [76.5, 76.5], [77.3, 76.5]]
angles_2_app = [[75.9, 76.7], [75.8, 76.9], [75.8, 76.7], [76.09, 75.93]]

# length to Gate 1, gate 2, ... 
gates_r_1 = [226, 386, 556, 722, 901] #mm
gates_a_1 = [215.5, 381, 558, 722, 900.5] #mm
gates_m_1 = [215.5, 381.5, 557.5, 722.5, 901] #mm
gates_s_1 = [215.5, 383.0, 557.5, 722.0, 901] #mm

#Put it together in a matrix
gates = [gates_r_1, gates_a_1, gates_m_1, gates_s_1]

#Trig
horizontal_length = [929, 927, 927, 918] #mm
vertical_length  = [254.5, 256, 259, 234] #mm