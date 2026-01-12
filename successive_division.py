from common import *
from math import sqrt

p_power = ["", "p", "p²", "p3", "p4"]

num: list[float] = []
den: list[float] = []
n_num = []
n_den = []

cnt = 0
results:list[float] = []
print_results:list[str] = []


user_num = input("enter numerator\n ->")
user_den = input("enter denumerator\n ->")

for i in user_num.split(","):
    num.append(float(i))

for i in user_den.split(","):
    den.append(float(i))

print(num)
print("------------")
print(den)

input("press enter to calculate...")
while 1:
    if not len(den):
        break
    results.append(num[0]/den[0])
    print_results.append(str(results[cnt]) + p_power[len(num) - len(den)])
    print()
    print(cnt)
    print()
    print(num)
    print("----------------------------")
    print(den)
    for i in range(len(num)):
        if i < len(den):
            res = num[i]-(den[i]*results[cnt])
        else:
            res = num[i]
        if res:
            n_num.append(res)
    
    num = den
    den = n_num
    n_num = []
    cnt += 1

print(print_results)

print("filter design")
input("press enter to calculate...")
for i, j in enumerate(print_results):
    if "p" in j:
        if i % 2:
            print("C= " + j)
        else:
            print("L= " + j)
    else:
        print("R= " + j)


