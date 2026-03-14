import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t',real=True)
a, T = sp.symbols('a T', positive=True)
a_val = 2
T_val = 3
assert T_val > 0, "T must be positive"
f_sym = sp.Piecewise(
    (a+a/T*t, sp.And(t >= -T, t < 0)),
    (a-a/T*t, sp.And(t >= 0, t <= T)),
    (0, sp.And(t < -T, t > T))
)
f = sp.lambdify((t,a,T), f_sym)
t_a = np.linspace(-T_val*2,T_val*2,101)
fig, (f_plt,F_plt) = plt.subplots(2,1)
f_plt.plot(t_a,f(t_a,a_val,T_val))
f_plt.set_xlabel("Harmonic $n$")
f_plt.set_ylabel("Harmonic Ampitude")
print(f(t_a,a_val,T_val))

fig.show()

w = sp.symbols('w',real=True)
F_sym = sp.integrate(
    f_sym*sp.exp(-1j*w*t),(t,-T,T)
).simplify().rewrite(sp.cos).trigsimp().simplify()

F = sp.lambdify((w,a,T),F_sym)
print(F_sym)

a_a = np.array([1,2,3])
T_a = np.array([1,2,3])
w_a = np.linspace(-5,5,11)
for i,a_i in enumerate(a_a):
    for j,T_j in enumerate(T_a):
        F_plt.plot(
            w_a,F(w_a,a_i,T_j),
            label=f"a = {a_i}, T = {T_j}"
        )
F_plt.legend()
F_plt.grid()
F_plt.set_xlabel(r"$\omega$ (rad/s)")
F_plt.set_ylabel(r"$F(\omega)$")

plt.show()