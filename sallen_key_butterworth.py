"""
TO IMPLEMENT : 
+ add band-pass and band-cut filter support
+ add quality factor, freq response (fn, Q, K) calculation
"""

from math import sqrt, pow, pi, log10, ceil
from common import *


#
# user Variables
#  
"""
0 -> low-pass
1 -> High-pass
2 -> band pass
"""
filter_type = 1
Fc = 750000 #frequence de coupure
c = 0.0000000001
r = 10000  # 10k
n = 6
#
# user Variables
#  

fn_array = []
m_array = []
K_array = []


Fc = float(input("enter a value for Fc \n ->"))
filter_type = int(input("\n\nchoose the filter type\n"
                    "0 -> low-pass\n"
                    "1 -> High-pass\n"
                    "2 -> band pass\n ->"))

n = int(input("enter a value for n \n ->"))

wc = 2 * pi * Fc # pulsation de coupure



if filter_type == 0:
    r = float(input("enter a value for R \n->"))

    print()
    print("         p")
    print("C2 = --------")
    print("      2*R*Wc")
    print()
    print("         1")
    print("C1 = --------")
    print("      R²*C2*Wc²")
    print()
    print()
    print("            1")
    print("R²C1C2 = --------")
    print("           Wn²")
    print()
    print()
    print("          2m")
    print("2RC1 = --------")
    print("          Wn")
    print()
    input("press enter to calculate...")
    for p in active_normalised_componant[n]:
        if p:
            var_c2 = p/(2*r*wc)
            var_c1 = 1/(pow(r,2)*var_c2*pow(wc,2))
            print("C1 = ", unit(var_c1, "F"))
            print("C2 = ", unit(var_c2, "F"), "\n")
            fn_array.append()
        else:   # RC filter
            var_1 = 1/(2*pi*r*Fc)
            print("C value in RC = ", unit(var_1, "F"), "\n")
    
elif filter_type == 1:
    c = float(input("enter a value for C \n->"))
    
    print()
    print("         p")
    print("R1 = --------")
    print("      2*C*Wc")
    print()
    print("         1")
    print("R2 = --------")
    print("      R1*C²*Wc²")
    print()
    input("press enter to calculate...")
    for p in active_normalised_componant[n]:
        if p:
            var_1 = p/(2*c*wc)
            var_2 = 1/(var_1*pow(c, 2)*pow(wc,2))
            print("R1 = ", unit(var_1, "W"))
            print("R2 = ", unit(var_2, "W"), "\n")
        else:   # RC filter
            var_1 = 1/(2*pi*c*Fc)
            print("R value in CR = ", unit(var_1, "W"), "\n")
else:
    print("filter type not implemented yet !!!")










