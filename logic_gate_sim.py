"""
document doc string
"""




AND     = 0
OR      = 1
NAND    = 2
NOR     = 3
XOR     = 4
NOT     = 5
PIN     = 6

class gate:
    def __init__(self, node_name:str ,gate_type:int, A:bool  | gate= False, B:bool | gate = False) -> None:
        self.node_name = node_name
        self.A = A
        self.B = B
        self.gate_type = gate_type

    def SCOAP(self) -> None:
        print(f"{   self.node_name.rjust(5)}   {str(self.CC0()).rjust(5)}   {str(self.CC1()).rjust(5)}")

    def fault_sim(self) -> None:
        pass

    def CC0(self) -> int:
        if self.gate_type == PIN:
            return 1
        
        elif self.gate_type == AND:
            return min(self.A.CC0(), self.B.CC0()) + 1
    
        elif self.gate_type == OR:
            return self.A.CC0() + self.B.CC0() + 1
    
        elif self.gate_type == NAND:
            return self.A.CC1() + self.B.CC1() + 1
    
        elif self.gate_type == NOR:
            min(self.A.CC1(), self.B.CC1()) + 1
    
        elif self.gate_type == XOR:
            return min(self.A.CC0()+self.B.CC0(), self.A.CC1()+self.B.CC1()) +1
    
        elif self.gate_type == NOT:
            return self.A.CC1() + 1

    def CC1(self) -> int:
        if self.gate_type == PIN:
            return 1
        
        elif self.gate_type == AND:
            return self.A.CC1() + self.B.CC1() + 1
    
        elif self.gate_type == OR:
            return min(self.A.CC1(), self.B.CC1()) + 1
    
        elif self.gate_type == NAND:
            return min(self.A.CC0(), self.B.CC0()) + 1
    
        elif self.gate_type == NOR:
            return self.A.CC0() + self.B.CC0() + 1
    
        elif self.gate_type == XOR:
            return min(self.A.CC1()+self.B.CC0(), self.A.CC0()+self.B.CC1()) +1
    
        elif self.gate_type == NOT:
            return self.A.CC0() + 1

    def out(self) -> bool:
        if self.gate_type == PIN:
            return self.A
        
        elif self.gate_type == AND:
            return self.A.out() and self.B.out() # type: ignore
    
        elif self.gate_type == OR:
            return self.A.out() or self.B.out() # type: ignore
    
        elif self.gate_type == NAND:
            return not(self.A and self.B)
    
        elif self.gate_type == NOR:
            return not(self.A or self.B)
    
        elif self.gate_type == XOR:
            return (self.A and not self.B) or (not self.A and self.B)
    
        elif self.gate_type == NOT:
            return not(self.A)

    def in1(self) -> gate|None:
        if type(self.A) == gate:
            return self.A
        return None
    
    def in2(self) -> gate|None:
        if type(self.B) == gate:
            return self.B
        return None



# while type(prev_gate) == gate:
#     prev_gate = prev_gate.in1()
#     if prev_gate:
#         print(prev_gate.gate_type)


pin_a = gate("a",PIN)
pin_b = gate("b",PIN)
pin_c = gate("c",PIN)
pin_d = gate("d",PIN)


y1 = gate("y1", NAND, pin_a, pin_b)
y2 = gate("y2",AND, y1, pin_c)
y3 = gate("y3",OR, pin_c, pin_d)
y4 = gate("y4",OR, y1, y2)
y5 = gate("y5",NOT, y2)
y6 = gate("y6",AND, y5, y3)
S  = gate("y7",AND, y4, y6)

input_list = [pin_a, pin_b, pin_c, pin_d, y1, y2, y3, y4, y5, y6, S]


print(f"{"node".rjust(5)}   {"CC0".rjust(5)}   {"CC1".rjust(5)}")
for i in input_list:
    i.SCOAP()

