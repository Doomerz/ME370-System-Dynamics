import sympy as sp

#laplace s
S = sp.symbols("S", complex=True)
#positive impedence coefficients
R1, C1, R2, I, C2, R3 = sp.symbols("R1, C1, R2, I, C2, R3", postive=True)
#a-type and t-type values across elements
Pr1, Pc1, Pr2, Pi, Pc2, Pr3, Qr1, Qc1, Qr2, Qi, Qc2, Qr3 = sp.symbols("Pr1, Pc1, Pr2, Pi, Pc2, Pr3, Qr1, Qc1, Qr2, Qi, Qc2, Qr3", complex=True)
#Source  elements
Ps, Qs = sp.symbols("Ps, Qs", complex=True)
#impedence across elements
Zr1, Zc1, Zr2, Zi, Zc2, Zr3 = sp.symbols("Zr1, Zc1, Zr2, Zi, Zc2, Zr3", complex=True)

#define list of input and output variables
inputs = [Ps, Qs]
outputs = [
    Pr1, Pc1, Pr2, Pi, Pc2, Pr3,
    Qr1, Qc1, Qr2, Qi, Qc2, Qr3
]
input_indices = [0,1] # Ps, Qs
output_indices = [1,9] # PC1, QI

#elemental equations
elems = [
    Pr1 - Qr1*Zr1,
    Pc1 - Qc1*Zc1,
    Pr2 - Qr2*Zr2,
    Pi - Qi*Zi,
    Pc2 - Qc2*Zc2,
    Pr3 - Qr3*Zr3
]

#continuity equations
conts = [
    Qr1-Qc1-Qr2,
    Qr2-Qi,
    Qi-Qc2-Qr3+Qs, 
]

#compatibility equations
comps = [
    Pr1+Pc1-Ps,
    Pr2+Pi+Pc2-Pc1,
    Pc2-Pr3
]

#dictionary of impedence substitutions
impedence_dict = {
    Zr1: R1,
    Zc1: 1/(C1*S),
    Zr2: R2,
    Zi: I*S,
    Zc2: 1/(C2*S),
    Zr3: R3
}

#solve the linear algebraic system of equations
eqs = elems + conts + comps
sol = sp.solve(eqs, outputs, dict=True)

#create dicts to isolate all other sources to 0
iso_Ps = {src: 0 for src in inputs if src != Ps}
iso_Qs = {src: 0 for src in inputs if src != Qs}

#build transfer functions
H1 = sol[0][Pc1].subs(iso_Ps).subs(impedence_dict)
H1 = H1.subs(Ps, 1).simplify() # input to 1
H1 = H1.expand(numer=True).expand(denom=True)
H1 = sp.rcollect(H1, S) # collect terms in s

H2 = sol[0][Pc1].subs(iso_Qs).subs(impedence_dict)
H2 = H2.subs(Qs, 1).simplify() # input to 1
H2 = H2.expand(numer=True).expand(denom=True)
H2 = sp.rcollect(H2, S) # collect terms in s

H3 = sol[0][Qi].subs(iso_Ps).subs(impedence_dict)
H3 = H3.subs(Ps, 1).simplify() # input to 1
H3 = H3.expand(numer=True).expand(denom=True)
H3 = sp.rcollect(H3, S) # collect terms in s

H4 = sol[0][Qi].subs(iso_Qs).subs(impedence_dict)
H4 = H4.subs(Qs, 1).simplify() # input to 1
H4 = H4.expand(numer=True).expand(denom=True)
H4 = sp.rcollect(H4, S) # collect terms in s

print("H1 = ", H1)
print("H2 = ", H2)
print("H3 = ", H3)
print("H4 = ", H4)