# -*- coding: utf-8 -*-
#%%Import packages
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

#%% Build model
m = GEKKO()
m.time = np.linspace(0,8,81)
#Vars
t = m.Var(0)
x = m.Var(1)
u = m.Var(1,0,5)
#periodic constraints
m.periodic(u)
m.periodic(x)
#Equations
m.Equation(t.dt() == 1)
m.Equation(x.dt() == -x + m.cos(t) + u)
#Objective
m.Obj((x-3)**2)
#options
m.options.IMODE = 6
#solve
m.solve()

#plot
plt.figure()
plt.plot(m.time,x.value,label='x')
plt.plot(m.time,u.value,label='u')
plt.legend()