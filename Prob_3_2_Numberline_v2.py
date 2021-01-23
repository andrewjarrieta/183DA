#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

A = 1.5
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
        return reward,0,y,v
    
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
    
    plus,actplus,ytemp,vtemp = MDP_rec(y,v,1,horizon-1)
    neutral,actneutral,ytemp2,vtemp2 = MDP_rec(y,v,0,horizon-1)
    minus,actminus,ytemp3,vtemp3 = MDP_rec(y,v,-1,horizon-1)
    
    plus = plus + reward
    neutral = neutral + reward
    minus = minus + reward
    
    if neutral >= plus and neutral >= minus:
        return neutral,0,y,v
    elif plus >= minus:
        return plus,1,y,v
    else:
        return minus,-1,y,v

y = 3
v = -1
a = 0
horizon = 11
reward, action, yprint, vprint = MDP_rec(3,-1,0,11)
#print(reward)
#print(action)
#print(yprint)
#print(vprint)

y = 5
v = -2
a = 0
horizon = 12
ylist = []
vlist = []
alist = []
ylist.append(y)
vlist.append(v)
alist.append(a)
for i in range(3*horizon):
    reward,a,y,v = MDP_rec(y,v,a,horizon)
    ylist.append(y)
    vlist.append(v)
    alist.append(a)
#print(ylist)
#print(vlist)
#print(alist)

plt.plot(ylist)

#print(f_phi(4))

