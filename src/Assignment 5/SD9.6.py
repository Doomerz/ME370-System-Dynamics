#f(t) for -T<=t<=T = a-a|t|/T, zero otherwise
#use fourier transform analysis on f and plot for various a and T

#old
#F(w) = a - a/T*(2T*sin(2Tw/2)/(Tw)) = a - a/T*(2*sin(Tw)/w) = a*(1-2*sin(Tw)/T/w)

# 1 for abs(t) < Q/2, else 0 == Qsin(Qw/2)/(Qw/2)
# 1 == 2pi*dirac(w)
# a == 2*pi*a*dirac(w)
# -a*abs(t)/T == -a/T*((2*T)*sin(2*T*w/2)/(2*T*w/2)) == -2*a*sin(T*w)/T/w
#therefore
# 2*a*(pi*dirac(w)-sin(T*w)/T/w)
#^this is also misguided..

#Fourier transform analysis is F(y(t)) = Y(w) = \int_{-oo}^{oo} y(t)*exp(-1j*w*t) dt
#therefore Y(w) = integral of: (a-a|t|/T)*exp(-1jwt) dt
#Y(w) = a * ( integral(0,t,-oo,-T) + integral(exp(-1jwt)) - 1/T*integral(-t*exp(-1jwt), t, -T,0) + integral(exp(-1jwt)) - 1/T*integral(t*exp(-1jwt), t, 0,T) + integral(0,t,T,oo) )
# integral of 0 is 0
#aside u dv = uv - v du; u = t, dv = exp(-1jwt), du = 1 dt, v = exp(-1jwt)/(-1jwt)
#Y(w) = a * ( exp(-1jwt)/(-1jw) + 1/T*(t*exp(-1jwt) - exp(-1jwt)/(-1jwt)/(-1jwt)) over -T to 0
# + exp(-1jwt)/(-1jw) - (1/T*(t*exp(-1jwt) - exp(-1jwt)/(-1jwt)/(-1jwt))) over 0 to T)
#Y(w) = a * ( 1/(-1jw) + 0 - ) //hmmm we can't divide by 0...

#if we realize that the form is even we can re-evaluate the form as: Y(w) = int_{-oo}^{oo} y(t)*(cos(wt)-1j*sin(wt)) dt where sin(wt) is 0 because it is even thus:
#Y(w) = int_{-oo}^{oo} y(t)cos(wt) dt
#Y(w) = integral(0,t,-oo,-T) + a*( integral((1+t/T)*cos(wt),t,-T,0) + integral((1-t/T)*cos(wt),t,0,T) ) + integral(0,t,T,oo) with ends being = 0
#integral of (1+t/T)*cos(wt) dt :: u dv = uv- v du; u = 1+t/T, dv = cos(wt), du = 1/T, v = -1/w*sin(wt) == (1+t/T)*(-1/w)*sin(wt)-(1/T)*(-1/w)*integral(sin(wt),t) == (1+t/T)*(-1/w)*sin(wt)-(-1/Tw)*(1/w)*cos(wt)
#(1+t/T)*(-1/w)*sin(wt)-(-1/Tw**2)*cos(wt) for -T,0 and (1-t/T)*(-1/w)*sin(wt)-(1/Tw**2)*cos(wt) for 0,T
#Y(w) = a*( eval((1+t/T)*(-1/w)*sin(wt)-(-1/Tw**2)*cos(wt),t,-T,0) + eval((1-t/T)*(-1/w)*sin(wt)-(1/Tw**2)*cos(wt),t,0,T) )
#Y(w) = a*( 0 + (1/Tw**2) - (0 + (1/Tw**2)*cos(-Tw)) + 0 - (1/Tw**2)*cos(Tw) - (0 - (1/Tw**2)) )
#Y(w) = a*( (1/Tw**2) - (1/Tw**2)*cos(-Tw) - (1/Tw**2)*cos(Tw) + (1/Tw**2) ) since cos(-x) == cos(x):
#Y(w) = (2a/Tw**2)*(1-cos(wT)) where T must be positive and w doesn't equal 0
#for w = 0
#Y(0) = int_{-T}^{T} a-a|t|/T dt - > eval from -oo to -T is 0 and T to oo is 0: eval(at+at**2/2T,t,-T,0) + eval(at-at**2/2T)
#0 - (-aT+aT**2/2T) + (aT-aT**2/2T) - 0 = 2aT-aT**2/T = 2aT-aT = aT

import numpy as np
import matplotlib.pyplot as plt

#consts
a_rng = 3
T_rng = 3
assert T_rng > 0, "T must be positive"
pts = 200
a = np.arange(-a_rng*0,a_rng+1,1)
T = np.arange(T_rng,0,-1)[::-1]
#plot prep
fig, ax = plt.subplots()

#plotting
for i in a:
    for k in T:
        w = np.linspace(-5,5,pts)
        res = np.empty(len(w))
        for n,v in enumerate(w):
            if v == 0:
                res[n] = i*k
            else:
                res[n] = 2*i/k/v**2*(1-np.cos(v*k))
        ax.plot(w, res, label=f"a={i}, T={k}")

ax.set_xlabel("Frequency (w)")
ax.set_ylabel("Amplitude")
ax.legend()
plt.grid()
plt.show()