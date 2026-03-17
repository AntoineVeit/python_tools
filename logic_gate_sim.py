"""
document doc string
"""




class and_gate:

    def __init__(self, A:bool, B:bool) -> None:
        self.A = A
        self.B = B
    
    def out(self) -> bool:
        return self.A and self.B
    
class or_gate:

    def __init__(self, A:bool, B:bool) -> None:
        self.A = A
        self.B = B
    
    def out(self) -> bool:
        return self.A or self.B
    
class nand_gate:

    def __init__(self, A:bool, B:bool) -> None:
        self.A = A
        self.B = B
    
    def out(self) -> bool:
        return not(self.A and self.B)
    
class nor_gate:

    def __init__(self, A:bool, B:bool) -> None:
        self.A = A
        self.B = B
    
    def out(self) -> bool:
        return not(self.A or self.B)
    
class not_gate:

    def __init__(self, A:bool) -> None:
        self.A = A
    
    def out(self) -> bool:
        return not(self.A)

a = False
b = True
c = False
d = True
y_1 = nand_gate(a, b)
print(y_1.out())
y_2 = and_gate(y_1.out(), c)
print(y_2.out())
y_3 = or_gate(c, d)
print(y_3.out())
y_4 = or_gate(y_1.out(), y_2.out())
print(y_4.out())
y_5 = not_gate(y_2.out())
print(y_5.out())
y_6 = and_gate(y_5.out(), y_3.out())
print(y_6.out())
s   = and_gate(y_4.out(), y_6.out())
print(s.out())
