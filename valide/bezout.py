from math import *

def pgcd(a, b):
    diviseurs = []
    
    x = 0

    while(x != 1):
        if(b == 0):
            return diviseurs
        diviseurs.append(floor(a/b))
        x = a - (floor(a/b)*b)
        print(int(a),  '=', int(floor(a/b)), '*', int(b) , '+' , int(x), sep=' ')
        a = b
        b = x
    
    return diviseurs

def multiply(A,B):

    result = [[0, 0]]
    
    for i in range(len(A)):
 
        # iterating by column by B
        for j in range(len(B[0])):
    
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
 
    return result

def bezout(a, b):
    matrice = [[0,1]]

    tab = pgcd(a,b)[::-1]

    for i in range(len(tab)):
        matrice = multiply(matrice, [[0,1],[1,-tab[i]]])
        print(matrice)
        if(i == len(tab) - 1):
            if(a*int(matrice[0][0])+b*int(matrice[0][1]) == 1):
                print(a , '*' , int(matrice[0][0]) , '+' , b , '*' , int(matrice[0][1]), '= 1')
            else:
                print(a , '*' , int(matrice[0][1]) , '+' , b , '*' , int(matrice[0][0]), '= 1')

a = int(input("Saisissez a : "))
b = int(input("Saisissez b : "))

bezout(a,b)