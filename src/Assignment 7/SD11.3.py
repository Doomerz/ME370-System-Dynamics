import numpy as np
import control
import matplotlib.pyplot as plt

m = 10
B = 500
K = 100000
pts = 300
x = np.linspace(0,.3,pts)

t, y = control.step_response(control.tf([1],[m,B,K]), x)

plt.plot(t,y)
plt.title(f"my'' + By' + Ky = u_step, with m = {m}, B = {B}, K = {K}")
plt.xlabel("time (s)")
plt.ylabel("output y(t)")
plt.show()