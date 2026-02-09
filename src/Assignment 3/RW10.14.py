"""
determine the state transition matrix and response of the system
dx1 = -4*x1
dx2 = -x2
dx3 = -7*x3
y = 2*x1+3*x2-x3
x1(0) = 5
x2(0) = 15
x3(0) = 2
"""
import numpy as np

#not sure how to solve this yet.
A = np.array([
    [-4,0,0],
    [0,-1,0],
    [0,0,-7]
])
B = np.array([
    [0],
    [0],
    [0]
])
C = np.array([
    [2,3,-1]
])
D = np.array([
    [0]
])
x0 = np.array([[5],[15],[2]])
evals, evecs = np.linalg.eig(A)
evecs = evecs[:, np.argsort(evals)[::-1]]
evals = np.sort(evals)[::-1]
Phi_prime = np.diag(np.exp(evals))
Phi = evecs @ Phi_prime @ np.linalg.inv(evecs)
print("State transition matrix:\n", Phi)
print("Free response for initial condition x(0) = [[5],[15],[2]]:\n", Phi @ x0)