#import sympy as sp
#import numpy as np

#t, n, a = sp.symbols('t n a', real=True)
#t_arr = np.array([0,1,2])
#n_arr = np.array([3,5,7])
#calc = sp.lambdify((n,t,a), a*t*n+n*11)
#mt, mn = np.meshgrid(t_arr,n_arr)
#mt[[0,1,2]  mn[[3,3,3]
#   [0,1,2]     [5,5,5]
#   [0,1,2]]    [7,7,7]]
#print("mt\n", str(mt))
#print("mn\n", str(mn))
#res = calc(mn,mt,1)
#res[[0, 3, 6]  //t_arr row0 and n_arr col0
#    [0, 5,10]  //t_arr row1 and n_arr col1
#    [0, 7,14]] //t_arr row2 and n_arr col2
#print("res\n" + str(res))

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#consts
a = 5
T = 1
pts = 1000
partials = np.concatenate(
    (np.arange(-50,0),
    np.arange(1,50+1))
)
time = np.linspace(-T,T,pts)
#plot prep
fig, ax = plt.subplots()

#calc
y = np.empty(((len(time),len(partials))))
res = np.empty(len(time))
for count,n in enumerate(partials):
    w = 2*np.pi*n/T
    b_n = (2/T)*(a*(2/w**2*np.sin(w*T/2)-T/w*np.cos(w*T/2)))
    #old value: (2/T)*(a*(1/w**2*np.sin(w*t)-t/w*np.cos(w*t)))*np.sin(w*t)
    for i, t in enumerate(time):
        y[i,count] = b_n*np.sin(w*t)
for i, x in enumerate(y):
    res[i] = np.sum(x)
ax.plot(time, res, label="sum of first 50 nonzero components")
for i,v in enumerate(partials):
    ax.plot(time, y[:,i], label=f"partial {v}")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Output")
ax.legend()
plt.grid()
plt.show()