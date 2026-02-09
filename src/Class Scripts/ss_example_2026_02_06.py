import numpy as np
import control
import matplotlib.pyplot as plt

t0 = 0
tf = 5
dt = 0.05
A = np.array([
    [-3,4,5],
    [0,-2,3],
    [0,-6,1]
])
B = np.array([
    [1],
    [0],
    [1]
])
C = np.array([
    [1,0,0],
    [0,-1,0]
])
D = np.array([
    [0],
    [0]
])
x_0 = np.array([1,2,3]) # initial state

u = lambda t: 3*np.ones_like(t) # step input: u(t) = 3
t_a = np.arange(t0,tf+dt,dt) # time from 0 to 5 seconds with 0.05s intervals

sys = control.ss(A,B,C,D)
y_num = control.forced_response(sys, T=t_a, U=u(t_a), X0=x_0).outputs

fig, ax = plt.subplots()
ax.plot(t_a, y_num[0, :], label=r"$y_1$")
ax.plot(t_a, y_num[1, :], label=r"$y_2$")
ax.set_xlabel("Time (s)")
ax.set_ylabel(r"$y(t)$")
ax.legend()
plt.show()