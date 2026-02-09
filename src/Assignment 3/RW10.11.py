"""
an overhead suspension system that is subjected to vibration from the support structure
1. determine the system eigen values and eigen vectors for the parameter values
    comment the modal response components and on the frequencies of vibration associated with the system
2. determine the system eigen values and eigen vectors when B is increated to 20
    comment on the influence of damping on the frequencies and modes of vibration
"""
import numpy as np

b1 = 0
m1 = 0.1
m2 = 1
k1 = 9
k2 = k1
b2 = 20

A1 = np.array([
    [-b1/m1, -1/m1, b1/m1,0],
    [k1,0,-k1,0],
    [b1/m2,1/m2,-b1/m2,-1/m2],
    [0,0,k2/m2,0]
])
A2 = np.array([
    [-b2/m1, -1/m1, b2/m1,0],
    [k1,0,-k1,0],
    [b2/m2,1/m2,-b2/m2,-1/m2],
    [0,0,k2/m2,0]
])

evals1, evecs1 = np.linalg.eig(A1)
evals2, evecs2 = np.linalg.eig(A2)
evecs1 = evecs1[:, np.argsort(evals1)[::-1]]
evecs2 = evecs2[:, np.argsort(evals2)[::-1]]
evals1 = np.sort(evals1)[::-1]
evals2 = np.sort(evals2)[::-1]

print("Eigenvalues for b = 0:\n", evals1)
print("Eigenvectors for b = 0:\n", evecs1)
print("Eigenvalues for b = 20:\n", evals2)
print("Eigenvectors for b = 20:\n", evecs2)
print("In evaluating the results I see that the frequencies of vibration are far more common in the undampened system and damping seems to reduce this. I am not sure I fully understand this yet, but this is interesting")