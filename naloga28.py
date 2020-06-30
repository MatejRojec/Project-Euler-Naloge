# 28. naloga

def spirala():
    stevec = 0
    luknja = 1
    stevec_sterih = 4
    vsota = 0
    for n in range(1, 1001 ** 2 + 1): 
        if stevec == 0:
            vsota += n
            stevec = luknja
            stevec_sterih -= 1
        elif stevec != 0:
            stevec -= 1
        if stevec_sterih == 0:
            luknja += 2
            stevec_sterih = 4
    print(vsota)

spirala()
669171001
print('Matej')