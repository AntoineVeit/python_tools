def parse_linear_factor(s: str):
    """
    Parse un facteur linéaire en x de la forme:
      "x", "(x+5)", "(x-2)", "(2x+1)", "(-3x-7)", "(-x+4)"
    Retourne (a, b) tel que a*x + b.
    """
    s = s.strip()
    if s.startswith("(") and s.endswith(")"):
        s = s[1:-1].strip()
    s = s.replace(" ", "")

    if "x" not in s:
        # facteur constant (a=0)
        return 0, float(s)

    left, right = s.split("x", 1)  # right peut être "", "+5", "-2", "+0", etc.

    # Coefficient de x (a)
    if left == "" or left == "+":
        a = 1
    elif left == "-":
        a = -1
    else:
        a = float(left)

    # Terme constant (b)
    if right == "":
        b = 0
    else:
        b = float(right)  # int gère "+5" et "-2"
    return a, b


def poly_mul(p, q):
    """Multiplie deux polynômes p et q (listes de coefficients [a0,a1,...])."""
    res = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            res[i + j] += a * b
    return res


def factors_to_polynomial(factors: list[str]):
    """
    factors: liste de str, on multiplie tous les facteurs.
    Retourne la liste des coefficients [a0,a1,...] du polynôme.
    """
    poly = [1]  # neutre multiplicatif
    for f in factors:
        a, b = parse_linear_factor(f)          # a*x + b
        poly = poly_mul(poly, [b, a])          # [b,a] représente b + a*x
    return poly


def poly_to_string(coeffs, var="x"):
    """Affiche un polynôme (coeffs=[a0,a1,...]) en string lisible."""
    terms = []
    for deg in range(len(coeffs) - 1, -1, -1):
        c = coeffs[deg]
        if c == 0:
            continue

        sign = " - " if c < 0 else " + "
        abs_c = -c if c < 0 else c

        if deg == 0:
            body = str(abs_c)
        elif deg == 1:
            body = var if abs_c == 1 else str(abs_c) + var
        else:
            body = var + "^" + str(deg) if abs_c == 1 else str(abs_c)+var+ "^" + str(deg)

        terms.append((sign, body))

    if not terms:
        return "0"

    # Premier terme sans "+" initial
    sign0, body0 = terms[0]
    out = ("-" + body0 if sign0 == "-" else body0)

    for sign, body in terms[1:]:
        out += sign + body
    return out



fact = []
user_input = input("enter ax*(x-b)*(cx+d) ...\n ->")
for i in user_input.split("*"):
    fact.append(i)
coeffs = factors_to_polynomial(fact)
print(poly_to_string(coeffs)) # x^3 + 7x^2 + 10x
