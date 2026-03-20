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
        self.COout:list[int] = []

    def SCOAP(self) -> None:
        return (f"{   self.node_name.rjust(5)}   {str(self.CC0()).rjust(5)}   {str(self.CC1()).rjust(5)}")

    def fault_sim(self) -> None:
        pass

    def CO(self) -> int:
        if self.gate_type == PIN:
            return min(self.COout)
        
        elif self.gate_type == AND:
            self.A.COout.append(min(self.COout) + self.B.CC1() + 1)
            self.B.COout.append(min(self.COout) + self.A.CC1() + 1)
            return min(self.COout)
    
        elif self.gate_type == OR:
            self.A.COout.append(min(self.COout) + self.B.CC0() + 1)
            self.B.COout.append(min(self.COout) + self.A.CC0() + 1)
            return min(self.COout)
    
        elif self.gate_type == NAND:
            self.A.COout.append(min(self.COout) + self.B.CC1() + 1)
            self.B.COout.append(min(self.COout) + self.A.CC1() + 1)
            return min(self.COout)
    
        elif self.gate_type == NOR:
            self.A.COout.append(min(self.COout) + self.B.CC0() + 1)
            self.B.COout.append(min(self.COout) + self.A.CC0() + 1)
            return min(self.COout)
    
        elif self.gate_type == XOR:
            self.A.COout.append(min(self.COout) + min(self.B.CC0(), self.B.CC1()) + 1)
            self.B.COout.append(min(self.COout) + min(self.A.CC0(), self.A.CC1()) + 1)
            return min(self.COout)
    
        elif self.gate_type == NOT:
            self.A.COout.append(min(self.COout) + 1)
            return min(self.COout)

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



user_input = input("enter the pin names\n :")

input_dict:dict[str,gate] = {}
for pin in user_input.split(","):
    input_dict[pin] = (gate(pin, PIN))

a = input("enter the node names and gate type\n :")
user_input:list[str] = []
while a != "":
    user_input.append(a)
    a = input("enter the node names and gate type\n :")

for in_gate in user_input:
    if "_and_" in in_gate:
        input_dict[in_gate.split("_")[0]] = gate(in_gate.split("_")[0], AND, input_dict[in_gate.split("_")[2]], input_dict[in_gate.split("_")[3]])
    elif "_or_" in in_gate:
        input_dict[in_gate.split("_")[0]] = gate(in_gate.split("_")[0], OR, input_dict[in_gate.split("_")[2]], input_dict[in_gate.split("_")[3]])
    elif "_nand_" in in_gate:
        input_dict[in_gate.split("_")[0]] = gate(in_gate.split("_")[0], NAND, input_dict[in_gate.split("_")[2]], input_dict[in_gate.split("_")[3]])
    elif "_nor_" in in_gate:
        input_dict[in_gate.split("_")[0]] = gate(in_gate.split("_")[0], NOR, input_dict[in_gate.split("_")[2]], input_dict[in_gate.split("_")[3]])
    elif "_xor_" in in_gate:
        input_dict[in_gate.split("_")[0]] = gate(in_gate.split("_")[0], XOR, input_dict[in_gate.split("_")[2]], input_dict[in_gate.split("_")[3]])
    elif "_not_" in in_gate:
        input_dict[in_gate.split("_")[0]] = gate(in_gate.split("_")[0], NOT, input_dict[in_gate.split("_")[2]])


input_dict["s"].COout.append(0)
input_list:list[gate] = list(input_dict.values())

scoap_list = []
print(f"{"node".rjust(5)}   {"CC0".rjust(5)}   {"CC1".rjust(5)}   {"CO".rjust(5)}")
for i in input_list:
    scoap_list.append(i.SCOAP())
input_list.reverse()
scoap_list.reverse()
for i, j in enumerate(input_list):
    scoap_list[i] += f"   {str(j.CO()).rjust(5)}"
scoap_list.reverse()
for i in scoap_list:
    print(i)

# name_list:list[str] = []
# for i in input_list:
#     name_list.append(i.node_name)

# fault_bits = ["OK", "0y1", "1y1", "0y2", "1y3", "0y4", "1y5", "0y5", ]
# print()
# print()
# print("bits   0   1   2   3   4   5   6   7")
# print("------------------------------------")
# for i in range(len(fault_bits)):
#     if fault_bits[i] != "OK":
#         print(f"{fault_bits[i]}    {int(not(int(fault_bits[i][0])))}   {int(not(int(fault_bits[i][0])))if i != 1 else fault_bits[i][0]}   {int(not(int(fault_bits[i][0])))if i != 2 else fault_bits[i][0]}   {int(not(int(fault_bits[i][0])))if i != 3 else fault_bits[i][0]}   {int(not(int(fault_bits[i][0])))if i != 4 else fault_bits[i][0]}   {int(not(int(fault_bits[i][0])))if i != 5 else fault_bits[i][0]}   {int(not(int(fault_bits[i][0])))if i != 6 else fault_bits[i][0]}   {int(not(int(fault_bits[i][0])))if i != 7 else fault_bits[i][0]}")