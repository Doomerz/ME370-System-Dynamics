import numpy as np
import control
import matplotlib.pyplot as plt

wn = 10
z = [0.1,0.3,0.5,0.7]
for Z in z:
    mag = 1 / (2*Z*np.sqrt(1-Z**2))
    wp = wn * np.sqrt(max(1 - 2*Z**2, 0))
    print(f"zeta = {Z}: |H(j*wp)| = {mag}, wp = {wp} rad/s")

w = np.logspace(-1,2,500)
fig, ax = plt.subplots()
for Z in z:
    mag = wn**2 / np.sqrt((wn**2 - w**2)**2 + (2*Z*wn*w)**2)
    ax.semilogx(w,20*np.log10(mag),label=rf"$\zeta={Z}$") #wasn't a clear tool, more research needed
ax.set_xlabel("rad/s")
ax.set_ylabel("mag (dB)")
ax.legend()

plt.show()