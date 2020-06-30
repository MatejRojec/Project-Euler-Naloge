# Naloga 23
# vsota deljiteljen > n  Abundent number
def faktorji(stevilo):
	faktorji = []
	for i in range(1, int((stevilo) ** (1 / 2)) + 1):
		if stevilo % i == 0:
			faktorji.append(i)
			faktorji.append(stevilo // i)
	return faktorji

def izracuna_ravno_to_kar_pise_v_navodilu():
    slovar_stevil = {}
    list_abundnih_stevil = []
    for i in range(1, 28124):
        slovar_stevil[i] = i
    for i in slovar_stevil:
        if i < sum(faktorji(i)):
            list_abundnih_stevil.append(i)
    
    for stevilo_1 in list_abundnih_stevil:
        for stevilo_2 in list_abundnih_stevil:
            vsota = stevilo_1 + stevilo_2
            if vsota in slovar_stevil:
                slovar_stevil.pop(vsota)
    print(slovar_stevil)
    print(sum(slovar_stevil))
    4179871

            


