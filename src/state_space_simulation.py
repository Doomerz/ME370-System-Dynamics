import numpy as np
import control
import matplotlib.pyplot as plt

# Define the state-space representation of the system
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

sys = control.ss(A,B,C,D)
time = np.linspace(0,5,101)
# Simulate the system response to a 3*unit step input and with initial condition x0 = [1,2,3]
x0 = [1,2,3]
u = 3 * np.ones_like(time)
y = control.forced_response(sys, T=time, U=u, X0=x0).outputs

# Plot the results
fig, ax = plt.subplots()
ax.plot(time, y[0,:], label='Output 1')
ax.plot(time, y[1,:], label='Output 2')
ax.set_title('State-Space System Response')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Outputs')
ax.legend()
plt.grid()
plt.show()