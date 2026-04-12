import matplotlib.pyplot as plt
import control

a = 1
b = 1

sys = control.tf([b],[1,a,b])
control.bode_plot(sys)
plt.show()