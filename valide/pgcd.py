from math import *

def pgcd(a, b):
    diviseurs = []
    
    x = 2

    while(x > 1):
        if(b == 0):
            return
        diviseurs.append(floor(a/b))
        x = a - (floor(a/b)*b)
        print(int(a),  '=', int(floor(a/b)), '*', int(b) , '+' , int(x), sep=' ')
        a = b
        b = x

a = int(input("Saisissez a : "))
b = int(input("Saisissez b : "))
pgcd(a, b)