"""
x(d/dt) = Ax + Bu
has single input u(t) and has initial values of all state variable equal to zero.
define response to each of the inputs:
u(t) = 1 for 0 <= t < T
u(t) = 1 for 0 <= t < T and u(t) = 1 - 1/T * t for T <= t < 2*T
"""
#is this the free response or the forced response?
#table 10.1
"""
x(t) = exp(At)*x(0) + exp(At)*A**-1*(I-exp(-At))BK = exp(At)*x(0) + A**-1*(exp(At)-I)Bu(t)

Wave1:
with x(0) = 0, u(t) = 1 ->
    x(t) = A**-1*exp(A*t)*B for 0 <= t < T

for t >= T, u(t) = 0 ->
    x(t) = exp(A*(t-T))*x(T) for t >= T

Wave2:
with x(0) = 0, u(t) = 1 ->
    x(t) = A**-1*exp(A*t)*B for 0 <= t < T

for T <= t < 2*T, u(t) = (1 - (t - T)) ->
    x(t) = exp(A*(t-T))*x(T) + A**-1*(exp(A*(t-T))-I)*B*(1 - (t - T)) for T <= t < 2*T << is this not simplified enough..? is it atleast correct?

for 2*T <= t, u(t) = 0 ->
    x(t) = exp(A*(t-2*T))*x(2*T) for 2*T <= t
"""