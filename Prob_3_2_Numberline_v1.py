#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

A = 0
ymax = 30
vmax = 30
pc = 0.1
pw = 0.1

def f_phi(y):
    return int(A*np.sin(2*np.pi*y/ymax))

def MDP_rec(y,v,action,horizon):
    reward = 0
    if y == 0:
        reward = 1
    if horizon == 0:
        return reward,0
    
    y = y + v
    v = v + action + f_phi(y)
    
    if y > ymax:
        y = ymax
    if y < -ymax:
        y = -ymax
        
    if v > vmax:
        v = vmax
    if v < -vmax:
        v = -vmax
        
    '''rand_wobble = np.random.uniform()
    if rand_wobble < (v/vmax)*(pw/2):
        v = v + 1
        if v > vmax:
            v = vmax
    elif rand_wobble > 1 - (v/vmax)*(pw/2):
        v = v - 1
        if v < -vmax:
            v = -vmax'''
    
    plus,actplus = MDP_rec(y,v,1,horizon-1)
    neutral,actneutral = MDP_rec(y,v,0,horizon-1)
    minus,actminus = MDP_rec(y,v,-1,horizon-1)
    
    plus = plus + reward
    neutral = neutral + reward
    minus = minus + reward
    
    if neutral >= plus and neutral >= minus:
        return neutral,0
    elif plus >= minus:
        return plus,1
    else:
        return minus,-1

print(MDP_rec(3,-1,0,11))

