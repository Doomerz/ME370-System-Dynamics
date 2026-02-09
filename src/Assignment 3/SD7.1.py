"""
Let a system have the following state and output equation
matrices:
A = [
[-3,0],
[1,-2]
]
B = [
[0],
[1]
]
C = [
[0,1]
]
D = [
[0]
]
For this system, answer the following imperatives.
1. Find the eigenvalue matrix LAMBDA and comment on the stability of the system (justify your comment).
Use the convention that Eigval1 ≥ Eigval2 and order 
accordingly.
2. Find the eigenvectors and the modal matrix M.
3. Find the state transition matrix Phi(t). Hint: first find the “diagonalized” state
transition matrix Phi_prime(t).
4. Using the state transition matrix, find the output free response for initial
condition
X(0) = [
[1],
[0]
]
"""
import numpy as np
import sympy as sp
from pprint import pprint

def stability(eigenvalues):
    if any(v > 0 for v in eigenvalues):
        return "this is unstable as we have a positive eigenvalue"
    elif any(v == 0 for v in eigenvalues):
        return "this is marginally stable as we have eigenvalues <= 0 with atleast one == 0"
    else:
        return "this is asymptotically stable as all eigenvalues are < 0"

A = np.array([
    [-3,0],
    [1,-2]
])
B = np.array([
    [0],
    [1]
])
C = np.array([
    [0,1]
])
D = np.array([
    [0]
])

evals, evecs = np.linalg.eig(A)
evecs = evecs[:, np.argsort(evals)[::-1]] # sort the eigenvectors according to the sorted eigenvalues and reverse
evals = np.sort(evals)[::-1] # sort ascending and reverse
print("Eigenvalue matrix:\n", np.diag(evals))
print(stability(evals))
print("Eigenvectors/modal matrix:\n", evecs)
t = sp.symbols('t' ,real=True, nonnegative=True)
Phi_prime = sp.exp(sp.Matrix(np.diag(evals)) * t)
print("Phi_prime (diagonalized state transition matrix):\n", Phi_prime)
Phi = evecs * Phi_prime * np.linalg.inv(evecs)
print("Phi (state transition matrix):\n", Phi)
X0 = np.array([[1], [0]])
x_fr = Phi * X0
print("state free response for initial condition X(0) = [[1], [0]]:\n", x_fr)
y_fr = C * x_fr
print("output free response for initial condition X(0) = [[1], [0]]:\n", y_fr)
pprint(y_fr)
"""
evals, evecs = np.linalg.eig(A)
evecs = evecs[:, np.argsort(evals)[::-1]] # sort the eigenvectors according to the sorted eigenvalues and reverse
evals = np.sort(evals)[::-1] # sort ascending and reverse
emat = np.zeros((len(evals), len(evals)), dtype=complex)
for i in range(len(evals)):
    emat[i][i] = evals[i]
print("Eigenvalue matrix:\n", emat)
print(stability(evals))
print("Eigenvectors/modal matrix:\n", evecs)
Phi_prime = np.diag(np.exp(evals))
print("Phi_prime (diagonalized state transition matrix):\n", Phi_prime)
Phi = evecs @ Phi_prime @ np.linalg.inv(evecs)
#Phi = evecs * Phi_prime * np.linalg.inv(evecs) < --- this is wrong as we need to do matrix multiplication not elementwise multiplication
print("Phi (state transition matrix):\n", Phi)
X0 = np.array([[1], [0]])
x_fr = evecs @ Phi_prime @ np.linalg.inv(evecs) @ X0
print("Output free response for initial condition X(0) = [[1], [0]]:\n", x_fr)
"""
"""
Eigenvalue matrix emat (or LAMBDA) is:
asymptotically stabe if all eigen values have negative real parts
unstable if any eigen value has a positive real part
is marginally stable if any eigen value has a zero real part and none of them have a postitive real part
"""