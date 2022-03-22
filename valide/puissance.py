from math import *

def toBinary(num):

    rest = []

    while num > 0:
        rest.append(ceil(num%2))
        num = floor(num/2)

    return rest

def toPower(bin):

    res = []

    for i in range(len(bin)):
        if(bin[i] == 1):
            res.append(2**i)

    return res

def calc(num, puissance, modulo):

    res = num, "^(", puissance, ")="
    p2 = "=",
    tot = 1

    puissances = toPower(toBinary(puissance))
    for i in range(len(puissances)):
        if(i == len(puissances)-1):
            res += num, "^(", puissances[i], ")"
            p2 += (num**puissances[i])%modulo,
        else :
            res += num, "^(", puissances[i], ")*"
            p2 += (num**puissances[i])%modulo, "*"
        tot = tot * (num**puissances[i])%modulo

    res += p2
    res += "=", tot%modulo

    print(*res, sep='')

num = int(input("Numero : "))
puissance = int(input("Puissance : "))
modulo = int(input("Modulo n : "))

calc(num, puissance, modulo)
