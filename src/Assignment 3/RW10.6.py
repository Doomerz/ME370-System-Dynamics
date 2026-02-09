"""
x(d/dt) = Ax + Bu
has single input u(t) and has initial values of all state variable equal to zero.
define response to each of the inputs:
u(t) = 1 for 0 <= t < tau
u(t) = 1 for 0 <= t < tau and u(t) = 1 - 1/tau * t for tau <= t < 2*tau
"""
#is this the free response or the forced response?