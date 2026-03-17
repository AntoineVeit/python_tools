from math import sqrt, pow, pi, log10, ceil
from common import *



Rin = 2000
Rout = 500

Freq = 100000000        # working freq (Hz)
pulse = 2 * pi * Freq   # working pulse





#
# case with LC (Low-pass)
#

quality_factor = sqrt((Rin/Rout)-1)
print(unit(quality_factor))

Cap = quality_factor / (Rin*pulse)
print(unit(Cap, "F"))

Ind = 1 / ((Cap*pulse**2)*(1+1/quality_factor**2))
print(unit(Ind, "H"))


