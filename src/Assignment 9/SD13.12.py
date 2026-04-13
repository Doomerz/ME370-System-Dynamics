import numpy as np
import control
import matplotlib.pyplot as plt

rads = np.array([0.1,10,100])
amps = np.array([3,1,.5])

H = control.tf([100],[1,101,100])

outamps = np.empty(len(amps))
for i, w in enumerate(rads):
    resp = control.freqresp(H,[w])
    outamps[i] = amps[i] * np.abs(resp.fresp[0,0,0])

fig, (ax1, ax2) = plt.subplots(1,2)

ax1.bar(range(len(rads)),amps)
ax1.set_xticks(range(len(rads)))
ax1.set_xticklabels([f"{w}" for w in rads])
ax1.set_xlabel("rad/s")
ax1.set_ylabel("amp")
ax1.set_title("input spectrum")

ax2.bar(range(len(rads)),outamps)
ax2.set_xticks(range(len(rads)))
ax2.set_xticklabels([f"{w}" for w in rads])
ax2.set_xlabel("rad/s")
ax2.set_ylabel("amp")
ax2.set_title("input spectrum")

plt.show()