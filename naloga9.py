# naloga 9
# a < b < c 
# a ** 2 + b ** 2 + c ** 2 == 
#

def pythagoran_triplet(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False 

def najdi_vsoto():
    a = 3 
    b = 4
    c = 5
    vsota = 1000 
    for c in range(vsota):
        for b in range(c):
            for a in range(b):
                if a + b + c == vsota:
                    if pythagoran_triplet(a, b, c):
                        print(a, b, c)
                        print(a * b * c)
najdi_vsoto()
31875000
   