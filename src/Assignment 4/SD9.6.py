#f(t) for -T<=t<=T = a-a|t|/T, zero otherwise
#use fourier transform analysis on f and plot for various a and T

#F(w) = a - a/T*(2T*sin(2Tw/2)/(Tw)) = a - a/T*(2*sin(Tw)/w) = a*(1-2*sin(Tw)/T/w)

import numpy as np
import matplotlib.pyplot as plt

#consts
a_rng = 2
T_rng = 2
w_rng = 10
pts = 100
a = np.arange(-a_rng,a_rng+1,1)
T = np.arange(T_rng,0,-1)[::-1]
#plot prep
fig, ax = plt.subplots()

#plotting
for i in a:
    for k in T:
        w = np.linspace(-w_rng,w_rng,pts)
        ax.plot(w, i*(1-2*np.sin(k*w)/k/w), label=f"a={i}, T={k}")

ax.set_xlabel("Frequency (w)")
ax.set_ylabel("Amplitude")
ax.legend()
plt.grid()
plt.show()