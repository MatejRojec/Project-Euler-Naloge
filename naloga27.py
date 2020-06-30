# 27. Naloga

def je_prastevilo(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True

def kvadratna_funkcija():
    najvecje_stevilo_prastevil = 0
    a_b = False
    for a in range(- 997, 1000, 2):
        for b in range(2, 1000): 
            if not je_prastevilo(b):
                continue
            n = 0
            trenutno_stevilo_prastevil = 0
            while True:
                if je_prastevilo(n ** 2 + a * n + b) < 0:
                    break
                if je_prastevilo(n ** 2 + a * n + b):
                    trenutno_stevilo_prastevil += 1
                else:
                    if trenutno_stevilo_prastevil > najvecje_stevilo_prastevil:
                        najvecje_stevilo_prastevil = trenutno_stevilo_prastevil
                        a_b = a * b
                    break
            n += 1
    print(a_b)

print(kvadratna_funkcija())
-59231