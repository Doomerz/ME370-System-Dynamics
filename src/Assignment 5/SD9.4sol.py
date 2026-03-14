import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

t, omega_n, a, T, n = sp.var('t omega_n a T n', real=True)      # define variables
sym_dict = {omega_n: 2*sp.pi*n/T}                               # substitution dict
cn = sp.integrate(a*t*sp.exp(-1j*omega_n*t),(t,-T/2,T/2))       # c_n = 1/T*int_{-T/2}^{T/2} a*t*sp.exp(-1j*omega_n*t)\,dt \\ hint: a*(-t*e**(-jwt)/(jw) + e**(-jwt)/(w**2)) where w = 0 is a_0 therefore 0 or dc gain on other functions
#print(cn.rewrite(sp.cos).simplify())
cn_num = sp.lambdify((n,a,T),cn.subs(sym_dict))                 #create it into a calculable object when arguments are passed

a_num = 5
T_num = 1
n_terms = 10
n_array = np.concatenate(
    (np.arange(-n_terms,0,1),
     np.arange(1,n_terms+1,1))
)
cn_array = cn_num(n_array,a_num,T_num)
Mn_array = abs(cn_array)                                        #get the magnitude of a complex number
Pn_array = np.angle(cn_array)                                   #get the phase angle of a complex number

fig, (ax0,ax1,ax2) = plt.subplots(3,1)
ax0.stem(n_array,Mn_array)                                      #creates graphs coming up from the xaxis as opposed to plots or scatters
ax0.stem([0],[0]) # add n=0 harmonic
ax0.xaxis.set_major_locator(MaxNLocator(integer=True))          #adjusts the ticks along the axis
ax0.set_xlabel('harmonic $n$')
ax0.set_ylabel('harmonic amplitude')

#fig, ax = plt.subplots()
ax1.stem(n_array,Pn_array)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.set_xlabel('harmonic $n$')
ax1.set_ylabel('harmonic phase (rad)')

#plt.show() blocks until plot window is closed
#fig.show() non-blocking display of plot window

#this is the actual SD9.4 sol

n_sum = 50
a_num = 5
T_num = 1
t_array = np.linspace(-T_num, T_num, 500)
n_array = np.concatenate(
    (np.arange(-n_sum,0,1),
     np.arange(1,n_sum+1,1))
)
cn_array = cn_num(n_array,a_num,T_num)

en_sym = sp.exp(1j*omega_n*t).subs(sym_dict) # symbolic version
en_num = sp.lambdify((t,n,a,T),en_sym) # numerical version
# meshgrid so lamdified function can handle computing t and n
t_array_m, n_array_m = np.meshgrid(t_array,n_array)
en_array = en_num(t_array_m, n_array_m, a_num, T_num) # evaluate

f_sum = en_array.T.dot(cn_array) # transpose to match dimensions

#fig,ax = plt.subplots()
ax2.plot(t_array,f_sum)
ax2.set_xlabel('time(s)')
ax2.set_ylabel(f"partial sum of first ${n_sum}$ terms")

fig.show()
plt.show()