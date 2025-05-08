#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        resultat = 1
        for i in range(b):
            resultat *= a
        return resultat
    else:
        resultat = 1
        for i in range(abs(b)):
            resultat *= (a)
    return 1/resultat
