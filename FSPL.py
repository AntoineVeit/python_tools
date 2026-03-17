from math import log10, pi


Fc = 27000000   # Hz
dF = 50000      # Hz
Fm = 10000      # Hz
n = 3.5
d = 100         # m
Ge = 2
Gr = 2
FSPL = 20*n*log10(d) + 20*log10(Fc) + 20*log10((4*pi)/300000000) - Ge - Gr
print(FSPL)

BP = 2 * (Fm + dF)

print(BP)

Pn = 10*log10(BP) - 174 # dBm

print(Pn)

