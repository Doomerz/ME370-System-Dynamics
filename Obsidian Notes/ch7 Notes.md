x(d/dt) = Ax + Bu
y = Cx + Du

x = Px' -> x' = P^-1 \*x

x(d/dt)' = P^-1 \* A\*P\*x' + P^-1 \*B\*u
A' = P^-1 \* A\*P
B' = P^-1 \*B
C' = C\*P
D' = D

lam_i = eigenvalues
m_i = eigenvectors

LAM = eigenvalue matrix = eigenvalues in the diagonal but zero elsewhere in the matrix (emat)

Modal matrix = M = a composition of eigen vectors into one matrix

n = number of eigenvalues (eigenvalues/vectors are 1:1)

M is the transformation matrix
x' = M^-1 \*x
thus the state eq.:
x(d/dt)' = M^-1 \*A\*M\*x' + M^-1 \*B\*u
A\[m_1,m_2,m_3,...,m_n] = LAM\[m_1,m_2,m_3,...,m_n]
AM = M(LAM) -> LAM = M^-1 \*A \*M
therefore A' = LAM (diagonal, therefore diagonalized the state-space model)
x(d/dt)' = LAM\*x' +M^-1 \*B\*u

Phi(t) = e^(A\*t)
Phi'(t) = e^(LAM\*t) = diagonal of eigenvalues where (i,i) = e^(lam_i\*t)

x_fr'(t) = Phi'(t)x'(0) = sum(x_i'(0)\*e^(lam_i\*t))
where initial conditions are x'(0) = M^-1\*x(0)

now we can solve for x'(t) and convert the solution to the original basis with: x(t) = Mx'(t)

x_fr'(t) = Phi'(t)x'(0) -> M^-1 \*x_fr(t) = Phi'(t) \* M^-1 \*x(0)
x_fr = M\*Phi'(t)\*M^-1 \*x(0)
therefore Phi(t) = M\*Phi'(t)\*M^-1

if (REAL(lam_i) < 0) {
asymptotically stable
}
else if (!(REAL(lam_i) > 0) && any lam_i == 0) {
marginally stable
}
else {
some lam_i has a positive real and is thus unstable
}