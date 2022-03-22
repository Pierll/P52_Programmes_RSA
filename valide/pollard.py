n = int(input("Saisissez n : "))
a = 2

#ne pas toucher a partir de la
def pgcd(a, b):
    r = a % b
    while r != 0:
        tmp = r
        r = a % b
        if (r == 0):
            return tmp
        q = int(a/b)
        print(a, "=", b, "*", q, "+", r)
        a = b
        b = r
    return r

k = 1
x = pgcd(a-1, n)

while x == 1 or x == n:
    tmp = a
    a = (a**(k+1)) % n
    print("a_", k, "=", "a", "^", k, "_", k-1, "=", tmp)
    print("pgcd(", a-1, ",", n, ") = ")
    x = pgcd(a-1, n)
    print("=", x)
    k = k + 1
    print("")
print("Résultat : a =", a, ", donc p = ", x)
print("q=", n,"/", a, "=", n/a)