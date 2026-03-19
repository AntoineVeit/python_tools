"""
document doc string
"""


class input_pin:

    def __init__(self, name:str, value:bool=False) -> None:
        self.name = name
        self.value = value
    
    def out(self) -> bool:
        return self.value

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
    
class xor_gate:

    def __init__(self, A:bool, B:bool) -> None:
        self.A = A
        self.B = B
    
    def out(self) -> bool:
        return (self.A and not self.B) or (not self.A and self.B)
    
class not_gate:

    def __init__(self, A:bool) -> None:
        self.A = A
    
    def out(self) -> bool:
        return not(self.A)

a = input_pin("a")
b = input_pin("b")
c = input_pin("c")
d = input_pin("d")
y_1 = nand_gate(a.out(), b.out())
print(y_1.out())
y_2 = and_gate(y_1.out(), c.out())
print(y_2.out())
y_3 = or_gate(c.out(), d.out())
print(y_3.out())
y_4 = or_gate(y_1.out(), y_2.out())
print(y_4.out())
y_5 = not_gate(y_2.out())
print(y_5.out())
y_6 = and_gate(y_5.out(), y_3.out())
print(y_6.out())
s   = and_gate(y_4.out(), y_6.out())
print(s.out())


