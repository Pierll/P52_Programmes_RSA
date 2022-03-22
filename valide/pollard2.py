def pgcd(a, b):
    r = a % b
    while r != 0:
        tmp = r
        r = a % b
        if (r == 0):
            return tmp
        q = int(a/b)
        a = b
        b = r
    return r

x = int(input("Saisissez x : "))
y = int(input("Saisissez y : "))
n = int(input("Saisissez n : "))
b = int(input("Saisissez b : "))

pgcd_xy = pgcd((x-y), n)

while pgcd_xy == 1 or pgcd_xy == n:
    x = ((x**2) + b) % n
    print("x=", x)
    y = (((((y**2) + b) % n)**2) + b) % n
    print("y=", y)
    pgcd_xy = pgcd((x-y), n)
    print("pgcd((x-y),n)=", pgcd_xy)