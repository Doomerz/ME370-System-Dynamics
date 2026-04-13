import numpy as np
import control
import matplotlib.pyplot as plt

z = 0.01
wn = 3

H = control.tf([2*z*wn,wn*wn],[1,2*z*wn,wn*wn])
#print(H.poles())
control.bode_plot(H)

fig, [ax1,ax2] = plt.subplots(1,2)

omega = np.array([1,5,25])
amp = np.array([1,3,2])

Hfq = control.freqresp(H, omega) #not clearly taught in course
mag = np.abs(Hfq.frdata[0,0,:]) #further research needed
outamp = amp*mag

ax1.set_title("Input u(t)")
ax1.set_xlabel("rad/s")
ax1.set_ylabel("Amp")
ax1.stem(omega, amp)

ax2.set_title("output y(t)")
ax2.set_xlabel("rad/s")
ax2.set_ylabel("Amp")
ax2.stem(omega,outamp)

plt.show()