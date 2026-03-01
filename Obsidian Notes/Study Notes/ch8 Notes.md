# Fluid Intro
Q = volumetric flowrate
P = pressure drop
$\mathscr{P}(x)$ = power into the element
$\mathscr{P}(t) = Q(t)P(t)$

typical to use the pressure reference as ground.

work done on a system thus:
$W = \int_{0}^{T} Q(\tau)P(\tau) \ d\tau$

Pressure momentum:
$\Gamma(t) = \int_{0}^{t}P(\tau)\ d\tau + \Gamma(0)$

thus volume is:
$V(t) = \int_{0}^{t}Q(\tau)\ d\tau + V(0)$

# Fluid Inductors
as fluid flows through a pipe it has a momentum associated with it. this is stored kinetic energy. 

I = inertance (fluid inductor)
$\Gamma(t) = IQ(t)$
thus $dQ/dt = P/I$

for a linear inertance the ..?
$\varepsilon(t) = IQ(t)^2/2$

$F = m(dv/dt)$
$F/A = m/A(dv/dt)$
F/A = Pressure
$m = \rho AL$ because mass is cross-sectional area * Length * density
average velocity through the pipe is Q/A. (volumetric flowrate per area)
$Pressure = \rho L(d/dt) (Q/A)$
thus:
$P = \rho L/A (dQ/dt)$
$dQ/dt = (A/\rho L) P$
thus: $1/I = A/\rho L$
$I = \rho L/A$

Thus: Long thin pipes have more inertance
(generally ignored unless a pipe is relatively long and thin)
# Fluid Capacitors
when fluid is stored in tanks or pressure vessels it stores potential energy via its pressure drop P. a column of fluid will have P associated with the height of the column of the contained fluid.

for a linear fluid capacitor of capacitance C:
$V = CP$

$dV/dt = C(dP/dt)$
$dP/dt = (1/C)(dV/dt)$ = Q/C
^ remember that V != v, Volume d-time *IS* volumetric flowrate

$\varepsilon(t)=CP^2/2$

# Fluid Resistors
$Q = P/R$
where R = fluid resistance
fluid resistors dissipate energy from the system (to heat), making them energy dissipative elements
Al a: orifices, valves, pipes (typically long ones)
:
# Sources
- ideal volumetric flowrate source provides arbitrary energy to a system via, independent of the system, volumetric flowrate. pressure drop then depends on the system
- ideal pressure drop source provides arbitrary energy to a system via pressure drop. volumetric flowrate depends on the system
real sources, like pumps, cannot be ideal sources; but can approximate them.

# Variable types
P is like voltage = through
Q is like current = across
fluid capacitor is considered an A-type
fluid resistor is a D-type
and fluid inertance is a T-type

# Thermal Intro
heat transfer through Conduction, convection and radiation
q = heat flow rate
T = temperature
$\mathscr{P}(t)=q(t)$ = Power at the given element
$H(t)=\int_{0}^{t}\mathscr{P}(\tau)\ d\tau + H(0)$ = heat energy of a system with initial heat H(0)
Enthalpy is typically represented by H and heat by Q in heat class.

# Thermal Capacitors
C = Joules/Kelvin
$H = CT$
$dH/dt=C(dT/dt) \Rightarrow dT/dt=q/C$
thermal capacitance is an extensive property and thus depends on the amount of its substance. Specific heat capacity (c = J/K/kg) is an intensive property. These quantities are related for an object of mass m by the equation: $C = mc$

# Thermal Resistors
$q=T/R$
R = Thermal resistance
this does not dissipate heat, rather it simply resists the flow of heat.

## Conduction
Conduction is transfer through particle interaction, characterized by thermal resistance:
$R=L/\rho A$
L = length of the object in the direction of heat transfer
A = transverse cross-sectional area
$\rho$ = the materials thermal conductivity (W/K/m)

## Convection
Convection is heat transfer via fluid advection, characterized by thermal resistance:
$R = 1/hA$
h = the convection heat transfer coefficient (W/m^2/K)
^this is highly and nonlinearly dependent on the velocity of the fluid, geometry of the object and the fluid composition affect h as well.
A= area of fluid-object contact

## Radiation
Radiation is electromagnetic radiation emitted from one body and absorbed by another.
T_1 of a hot body
T_2 of a cold body
$\varepsilon$ = effective emissivity/absorptivity
A is the area of the exposed surfaces
thus characterized by:
$q=\varepsilon\theta A(T_1^4-T_2^4)$

where $\theta=5.67*10^-8*W/m^2K^4$ = stefan-boltzmann constant
this heat transfer is highly nonlinear. This is typically considered negligible, but is less suitable to ignore where high operating temperatures are anticipated.

## Sources
ideal heat flow rate source is an element that provides arbitrary heat flow rate Q_s to a system, independent of the temperature across it, which depends on the system.
example: resistive heater, microprocessor motor

ideal temperature source is an element that provides arbitrary temperature T_s to a system independent of the heat flow rate through it, which depends on the system