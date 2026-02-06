"""
1. find eigenvalue matrix LAMBDA and modal matrix M
2. comment on the stability
3. find the diagonalized state transition matrix Phi_prime(t) (print the expression?)
    also find the state transition matrix Phi(t)
4. find state free response for initial conditions x(0) = [[0],[0],[1]] (don't print expression?)
5. plot the free response found for 0,4 seconds
"""
import numpy as np
import matplotlib.pyplot as plt

def stability(eigenvalues):
    if any(v > 0 for v in eigenvalues):
        return "this is unstable as we have a positive eigenvalue"
    elif any(v == 0 for v in eigenvalues):
        return "this is marginally stable as we have eigenvalues <= 0 with atleast one == 0"
    else:
        return "this is asymptotically stable as all eigenvalues are < 0"

A = np.array([
    [-2,2,0],
    [-1,-2,2],
    [0,-1,-2]
])
x0 = np.array([[0],[0],[1]])
t_ini = 0.
t_end = 4.
pts = 101

evals, evecs = np.linalg.eig(A)
evecs = evecs[:, np.argsort(evals)][::-1]
evals = np.sort(evals)[::-1]
emat = np.diag(evals)
print("Eigenvalue matrix:\n", emat)
print("Modal Matrix:\n", evecs)
print(stability(evals))
Phi_prime = np.diag(np.exp(evals))
Phi = evecs @ Phi_prime @ np.linalg.inv(evecs)
print("Phi_prime (diagonalized state transition matrix):\n", Phi_prime)
print("Phi (state transition matrix):\n", Phi)
x_fr = Phi @ x0
print("Free response for initial condition x(0) = [[0],[0],[1]]:\n", x_fr)
if pts < 2:
    raise ValueError("pts must be at least 2 to create a time vector")
time = np.linspace(t_ini,t_end,pts)
y = np.array([evecs @ np.diag(np.exp(evals * t)) @ np.linalg.inv(evecs) @ x0 for t in time])

fig, ax = plt.subplots()
ax.plot(time, y[:,0], label="output 1")
ax.plot(time, y[:,1], label="output 2")
ax.plot(time, y[:,2], label="output 3")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Output")
ax.legend()
plt.grid()
plt.show()