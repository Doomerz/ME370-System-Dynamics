import numpy as np
import control
import matplotlib.pyplot as plt

A = [
    [0,1,0],
    [0,0,1],
    [-6,-11,-6]
]
B = [
    0,
    0,
    1
]
C = [1,0,0]
D = [0]

pts = 100

ss = control.ss(A,B,C,D)
tf = ss.to_tf()
eigv = np.linalg.eigvals(A)
print("poles:", tf.poles())
print("eigenvalues:", eigv)
print("zeros", tf.zeros())
assert tf.poles().all() == eigv.all(), "poles != eigv"

fig, (pzplt,us) = plt.subplots(2,1)

pzplt.set_title("Poles and Zeros")
pzplt.set_xlabel("Real axis")
pzplt.set_ylabel("Imaginary axis")
pzplt.plot(np.real(tf.zeros()),np.imag(tf.zeros()),"o")
pzplt.plot(np.real(tf.poles()),np.imag(tf.poles()),"x")

fig.show()

t, y = tf.step_response(np.linspace(0,8,pts))
us.set_title("Unit Step Response")
us.set_xlabel("time (s)")
us.set_ylabel("output y(t)")
us.plot(t, y)

plt.show()