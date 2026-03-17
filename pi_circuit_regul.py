from math import sqrt, pow, pi, log10, ceil
from common import *


ligne_power = 3         # watt
VCmax = 12              # Volt
Ra = 50                 # Ohm (atenna side resistor)
Quality_factor = 5  
Freq = 100000000        #working freq
pulse = 2 * pi * Freq   # working pulse

Rc = pow(VCmax,2)/(2*ligne_power)
print(Rc)



#
#   Antenna side
#

Rv = Ra/(1+pow(Quality_factor,2))
print(Rv)

Cap_1 = Quality_factor/(Ra*pulse)
print(unit(Cap_1))

Ind_1 = 1/(Cap_1*pow(pulse,2)*(1+1/pow(Quality_factor,2)))
print(unit(Ind_1))

#
#   transistor side
#

Qc = sqrt((Rc/Rv)-1)
print(Qc)

Cap_2 = Qc/(Rc*pulse)
print(unit(Cap_2))

Ind_2 = 1/(Cap_2*pow(pulse,2)*(1+1/pow(Qc,2)))
print(unit(Ind_2))


