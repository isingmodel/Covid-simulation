# parameters
N = 2000  # total population
I = 5  # initial infectious, the number of infectious
m = 0.1  # 감염률 in group (should this parameter decreases as group size get larger?)

# sub status:

import numpy as np
import matplotlib.pyplot as plt

"""
0: S
1: I
2: Q-S
3: Q-I
4: R
S can be I
S can be Q-S
I can be Q-I
"""
total_sub_num = 2000
# init sub status
sub_status = np.zeros((total_sub_num))

# initial infectious
infectious_count = int(total_sub_num / 100)
infectious_idx = np.random.choice(total_sub_num,
                                  infectious_count)
sub_status[infectious_idx] = 1

# everyday algorithm
# 
