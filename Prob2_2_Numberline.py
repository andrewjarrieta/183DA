#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

def f_phi(r):
    return 0

def f_i(t):
    #return 0.5*np.sin(t) + 1.5
    return 1

m = 1
r0 = 0
v0 = 0
t0 = 0
o0 = 0

r = [r0]
v = [v0]
t = [t0]
o = [o0]

for i in range(40):
    prob_crash = (np.abs(v[i]) - 10)/10
    prob_crash = max(0,prob_crash)
    prob_crash = min(1,prob_crash)
    
    r_next = r[i]+v[i]
    if np.random.uniform() < prob_crash:
        v_next = 0
    else:
        v_next = v[i]+np.random.normal(0,np.abs(0.1*v[i]))+(f_i(t[i]) + f_phi(r[i]))/m
    t_next = t[i]+1
    o_next = r[i]+np.random.normal(0,np.abs(0.5*v[i]))
    
    r.append(r_next)
    v.append(v_next)
    t.append(t_next)
    o.append(o_next)

plt.figure(1)
plt.plot(t,r)
plt.xlabel('Time')
plt.ylabel('Actual Position')
plt.figure(2)
plt.plot(t,o)
plt.xlabel('Time')
plt.ylabel('Measured Position')
plt.figure(3)
plt.plot(t,v)
plt.xlabel('Time')
plt.ylabel('Velocity');


# In[ ]:




