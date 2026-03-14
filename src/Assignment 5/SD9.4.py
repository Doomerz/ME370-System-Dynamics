#f(t) = at for -T/2 < t <= T/2
# a=5
# T =1
# plot f along with partial sum of the fourier series synthesis, the first 50 nonzero components over -T<=t<=T
# a_0 = 2/T int(y(t)) = should be 0 over the period #2(a*t**2/2 + c)/T, c = 0 therefore: a_0 = a*t**2/T
# a_n = 0 since the function is odd over the period
# b_n = (2/T)*(a*(1/w**2*sin(wt)-t/w*cos(wt))) < this has to be evaluated from -T/2 to T/2!!!
# now with corrections!
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#consts
a = 5
T = 1
pts = 1000
partials = 50
time = np.linspace(-T,T,pts)
#plot prep
fig, ax = plt.subplots()

#calc
n = 1
count = 0
y = np.empty(((len(time),partials)))
res = np.empty(len(time))
while True:
    w = 2*np.pi*n/T
    b_n = (2/T)*(a*(2/w**2*np.sin(w*T/2)-T/w*np.cos(w*T/2)))
    #old value: (2/T)*(a*(1/w**2*np.sin(w*t)-t/w*np.cos(w*t)))*np.sin(w*t)
    if count >= partials:
        break
    if b_n == 0:
        print(f"skipping n={n} since b_n is zero")
        n += 1
        continue
    for i, t in enumerate(time):
        y[i,count] = b_n*np.sin(w*t)
    count += 1
    n += 1
for i, x in enumerate(y):
    res[i] = np.sum(x)
ax.plot(time, res, label="sum of first 50 nonzero components")
for i in range(partials):
    ax.plot(time, y[:,i], label=f"partial {i+1}")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Output")
ax.legend()
plt.grid()
plt.show()