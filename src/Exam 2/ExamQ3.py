# H(s) = 50 * (s+10) / (s+5) / (s+100)
#+++part a: What are the poles and zeros of H? What is the stability
#+++part b: Write the frequency response function H(jw)
#+++part c: Write H(s) as a product of standard-form transfer function factors
#+++part d: At w = 50 rad/s, compute the exact magnitude |H(j50)| and express it in dB. Also compute the exact phase <H(j50)
#+++part e: sketch Bode Plots, label break frequencies

# H(s) = (50*s+500) / (s**2 + 105*s + 500)
# H(jw) = 50*(1j*w+10) / (1j*w+5) / (1j*w+100)
# H(s) = 1 * (s/10 + 1) / (s/5 + 1) / (s/100 + 1)

import numpy as np
import control
import matplotlib.pyplot as plt

H = control.tf([50,500],[1,105,500])
print("Part A:\nPoles =", H.poles(), "\nZeros =", H.zeros(), "\nAll poles are negative, so the system is stable.")
print("Part B:", "H(jw) = 50*(1j*w+10) / (1j*w+5) / (1j*w+100)")
print("Part C:", "H(s) = 1 * (s/10 + 1) / (s/5 + 1) / (s/100 + 1)")
mag, phase, omega = H.frequency_response(50)
print("Part D:\nMagnitude in dB:", 20*np.log10(mag), "\nPhase (radians):", phase)

#part e:
H1 = control.tf([1/10,1],[1])
H2 = control.tf([1],[1/5,1])
H3 = control.tf([1],[1/100,1])
control.bode_plot([H, H1, H2, H3], label=["Total", "first product (break@10**1)", "second product(break@5)", "third product(break@10**2)"], wrap_phase=True) # The first system was starting at -360 degrees so we need wrap_phase=True to make sure it starts at 0 deg.
print("Part E: BEHOLD, THE PLOTS!!!")
plt.show()