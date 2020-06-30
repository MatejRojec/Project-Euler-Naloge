# Naloga 15 
# Se izkaže, da se za to nalogo skriva, kar nekaj lepe matematike
# Če si ogledamo 2 x 2 primer
# Za vsako pot moramo narediti 4 poteze 
# 2x gremo v desno in 2x dol
# Torej imamo 4 poteze, 2 pa lahko dejansko izberemo 
# enako velja za primer 20 x 20

def fakulteta(n):
    if n == 1:
        return 1
    else:
        return fakulteta(n - 1) * n

def binomski_simbol(n, k):
    return fakulteta(n) // (fakulteta(k) * fakulteta(n - k) )


def stevilo_poti(stevilo):
    a = 2 * stevilo
    return binomski_simbol(a, stevilo)
print(stevilo_poti(20))
137846528820
