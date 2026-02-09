"""
1. find the eigenvalue matrix LAMBDA and comment on the stability of the system
2. find eigenvectors and the modal matrix M
3. find state transition matrix Phi(t)
4. u(t) = [[4],[sin(2pi*t)]]; solve for forced state response
5. solve for the forced output response y_fo(t)
6. plot y_fo(t) for 0 <= t <= 7sec
"""

import numpy as np
import control
import matplotlib.pyplot as plt
import sympy as sp

def stability(eigenvalues):
    if any(v > 0 for v in eigenvalues):
        return "this is unstable as we have a positive eigenvalue"
    elif any(v == 0 for v in eigenvalues):
        return "this is marginally stable as we have eigenvalues <= 0 with atleast one == 0"
    else:
        return "this is asymptotically stable as all eigenvalues are < 0"

A = np.array([
    [-1, 0, 8],
    [ 0,-2, 0],
    [ 0, 0,-3]
])
B = np.array([
    [0,2],
    [3,0],
    [0,0]
])
C = np.array([
    [1,0,-1]
])
D = np.array([
    [0,0]
])

t = sp.symbols('t' ,real=True, nonnegative=True)
tau = sp.symbols('tau', real=True, nonnegative=True)
time = np.linspace(0,7,101)
"""def u(t):
    = np.array([
    [4],
    [np.sin(2*np.pi)]
])"""
# input function as a symbolic expression
u = sp.Matrix([
    [4],
    [sp.sin(2*sp.pi*t)]
])
#input function for plotting
def ufunc(t):
    return np.array([
        [4],
        [np.sin(2*np.pi*t)]
    ])

#1.
eigenvalues, eigenvectors = np.linalg.eig(A)
eigenvectors = eigenvectors[:, np.argsort(eigenvalues)[::-1]]
eigenvalues = np.sort(eigenvalues)[::-1]
print("Eigenvalue matrix:\n", np.diag(eigenvalues))
print(stability(eigenvalues))
#2.
print("Modal matrix:\n", eigenvectors)
#3.
Phi_prime = sp.exp(sp.Matrix(np.diag(eigenvalues)) * t)
print("diagonalized state transition matrix Phi_prime(t):\n", Phi_prime)
#Phi_prime = np.diag(np.exp(eigenvalues))
#Phi = eigenvectors @ Phi_prime @ np.linalginv(eigenvectors).
Phi = eigenvectors * Phi_prime * np.linalg.inv(eigenvectors)
print("state transition matrix Phi(t):\n", Phi)
#4.
Phi_t_tau = Phi.subs(t,-tau)
B_ = sp.Matrix(B)
u_tau = u.subs(t,tau)
x_fo = Phi * sp.integrate(Phi_t_tau * B_ * u_tau, (tau, 0, t)).simplify()
print("forced state response x_fo(t):", x_fo) #why is this coming out wrong???
#sp.pprint(x_fo)
#5.
C_ = sp.Matrix(C)
D_ = sp.Matrix(D)
y_fo = C_ * x_fo + D_ * u
#get lambdified functions
mods = [{'exp': np.emath.sqrt}, 'scipy'] #this was in class, not sure where this went.
n, d = sp.fraction(y_fo[0,0].ratsimp())
n, d = map(lambda x: sp.simplify(x*sp.exp(-t)),(n,d))
y_fo = n/d
print("forced output response y_fo(t):", y_fo)

y_fo_ = sp.lambdify(t,y_fo)#,modules=mods)

fig, ax = plt.subplots()
ax.plot(time, y_fo_(time), label="forced output response")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Output y_fo(t)")
ax.legend()
plt.grid()
plt.show()

"""
my work

def stability(eigenvalues):
    if any(v > 0 for v in eigenvalues):
        return "this is unstable as we have a positive eigenvalue"
    elif any(v == 0 for v in eigenvalues):
        return "this is marginally stable as we have eigenvalues <= 0 with atleast one == 0"
    else:
        return "this is asymptotically stable as all eigenvalues are < 0"

def conventional_eig(A):
    evals, evecs = np.linalg.eig(A)
    evecs = evecs[:, np.argsort(evals)][::-1]
    evals = np.sort(evals)[::-1]
    return evals, evecs

def Phi_prime(eigenvalues, time = np.array([])):
    if len(time) == 0:
        return np.diag(np.exp(eigenvalues))
    return np.array([np.diag(np.exp(eigenvalues * t)) for t in time])

def Phi(eigenvalues, eigenvectors, time = np.array([])):
    return eigenvectors @ Phi_prime(eigenvalues, time) @ np.linalg.inv(eigenvectors)

evals, evecs = conventional_eig(A)
print("Eigenvalue matrix:\n", np.diag(evals))
print(stability(evals))
print("Modal matrix:\n", evecs)
print("Phi (state transition matrix):\n", Phi(evals, evecs))
print("Forced state response:\n", Phi(evals, evecs) @ B @ u)
print("forced output response:\n", Phi(evals,evecs) @ D @ u)

y = Phi(evals,evecs,time) @ D @ u_of_t

fig, ax = plt.subplots()
ax.plot(time, y[:,0], label="output 1")
ax.plot(time, y[:,1], label="output 2")
ax.plot(time, y[:,2], label="output 3")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Output")
ax.legend()
plt.grid()
plt.show()"""