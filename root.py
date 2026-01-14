from math import sqrt

def roots_poly(coeffs):
    # copie + supprime les zéros de plus haut degré
    c = coeffs[:]
    while len(c) > 1 and abs(c[-1]) == 0:
        c.pop()

    deg = len(c) - 1

    if deg < 0:
        return []
    if deg == 0:
        # a0 = 0 -> "infinité de solutions", sinon aucune racine
        return ["inf"] if c[0] == 0 else []
    if deg == 1:
        # a1*x + a0 = 0
        a0, a1 = c[0], c[1]
        if a1 == 0:
            return ["inf"] if a0 == 0 else []
        return [(-a0) / a1]

    # deg == 2: a2*x^2 + a1*x + a0 = 0
    a0, a1, a2 = c[0], c[1], c[2]
    if a2 == 0:
        # retombe sur degré 1
        return roots_poly([a0, a1])

    disc = a1*a1 - 4*a2*a0
    r1 = (-a1 - sqrt(disc)) / (2*a2)
    r2 = (-a1 + sqrt(disc)) / (2*a2)
    return [r1, r2]

coeffs = []
user_input = input("enter aX^n + bX^n-1 ... + z\n ->")
for i in user_input.split(","):
    coeffs.append(float(i))
coeffs.reverse()
print(roots_poly(coeffs))
