




a = ["R_1jc_1w"]
b = ["R_2jc_2w"]
common: list[str] = []
var_a: list[str] = []
var_b: list[str] = []

for i,e in enumerate(a[0]):
    if e == "_":
        var_a.append(a[0][i-1] + a[0][i] + a[0][i+1])
for i in var_a:
    a[0] = a[0].replace(i, "")
for i in a[0]:
    var_a.append(i)
print(var_a)


for i,e in enumerate(b[0]):
    if e == "_":
        var_b.append(b[0][i-1] + b[0][i] + b[0][i+1])
for i in var_b:
    b[0] = b[0].replace(i, "")
for i in b[0]:
    var_b.append(i)
print(var_b)




for i in var_a:
    if i in common:
        pass
    elif i in var_b:
        common.append(i)
print(common)

for i, e in enumerate(common):
    common[i] += '²'
    var_a.remove(e)
    var_b.remove(e)

result = ""

for i in common:
    result += i

for i in var_a:
    result += i

for i in var_b:
    result += i

print(result)

