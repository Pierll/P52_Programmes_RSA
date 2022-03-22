from math import *

def mod_inverse(x,m):
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break

        elif n == m - 1:
            return "Null"
        else:
            continue


p = int(input("Saisissez p : "))
P = int(input("Saisissez P : "))
alpha = int(input("Saisissez alpha : "))

def shanks(P, alpha, p):
    f1 = []
    f2 = []

    m = floor(sqrt(p-1))
    print("Sachant que P=alpha^(s), P*(alpha^(-a))^r = (alpha^(m))^(q)")
    print(P, "*(", mod_inverse(alpha,p), ")^(r)=(",(alpha**m)%p,")^q")

    for q in range((ceil(sqrt(p-1)))+1):
        f1.append(((alpha**m)**q)%p)

    for r in range(m):
        f2.append((P*(mod_inverse(alpha,p))**r)%p)

    print(f1)
    print(f2)
    
    for i in range((ceil(sqrt(p-1)))+1):
        for j in range(m):
            if f1[i] == f2[j]:
                q = i
                r = j

    print("Donc nous avons q = ", q, " et r = ", r)
    print("Soit s = ", q, "*", m, "+", r, "=", (q*m+r)%p)

shanks(P, alpha, p)