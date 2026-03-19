

def to_dec(val:str):
    if "0x" in val:
        print("value converted from Hex to Dec")
        print(int(val.strip("0x"), 16))
    elif "0b" in val:
        print("value converted from Bin to Dec")
        print(int(val.strip("0b"), 2))
    elif "0a" in val:
        print("value converted from ASCII to Dec")
        val = val.strip("0a")
        for v in val:
            print(ord(v))

def to_bin(val:str):
    if "0x" in val:
        print("value converted from Hex to Bin")
        print(bin(int(val.strip("0x"), 16)))
    elif "0d" in val:
        print("value converted from Dec to Bin")
        print(bin(int(val.strip("0d"))))
    elif "0a" in val:
        print("value converted from ASCII to Bin")
        val = val.strip("0a")
        for v in val:
            print(f"{bin(ord(v))} - {len(bin(ord(v))) - 2} bits")

def to_hex(val:str):
    if "0d" in val:
        print("value converted from Dec to Hex")
        print(hex(int(val.strip("0d"), 10)))
    elif "0b" in val:
        print("value converted from Bin to Hex")
        print(hex(int(val.strip("0b"), 2)))
    elif "0a" in val:
        print("value converted from ASCII to Dec")
        val = val.strip("0a")
        for v in val:
            print(hex(ord(v)))

def to_ascii(val:str):
    if "0x" in val:
        print("value converted from Hex to ASCII")
        print(chr(int(val.strip("0x"), 16)))
    elif "0b" in val:
        print("value converted from Bin to ASCII")
        print(chr(int(val.strip("0b"), 2)))
    elif "0d" in val:
        print("value converted from Dec to ASCII")
        print(chr(int(val.strip("0d"), 10)))


