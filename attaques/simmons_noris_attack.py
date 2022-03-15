import math
#declarations
n = 1633
e = 153
C=205
#M=5
def multiply(liste, nbr, mod):
    s = pow(nbr, liste[0]) % mod
    print(s, end='*')
    for i in range(1, len(liste)):
        print(pow(nbr, liste[i]) % mod, end='*')
        s = s * pow(nbr, liste[i]) % mod
    return s
def decomp2(n):
    d = n
    b = []
    r = []
    while d > 0:
        if d%2 != 0:
            b.append(1)
        else:
            b.append(0)
        d = math.floor(d / 2)
    for i in range(len(b)-1, -1, -1):
        if b[i]:
             r.append(pow(2,i))
    return r

i = 0
Ct = C
while (True):
    d = decomp2(e)

    for y in d:
        print(Ct , "^", y, "* ", end='')
    print("=",end='')
    c = multiply(d, Ct, n)
    print("=",end='')
    print(c)
    Ct = c
    i+=1
    if (i > 10 or c == C):
        break