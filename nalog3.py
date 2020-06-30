# 3. naloga 
# verzij 1 je spodaj(pocasnejsa)
def najdemo_prafaktrje_neuncikovit(stevilo):
	faktorji = []
	for i in range(1, stevilo + 1):
		if stevilo % i == 0:
			faktorji.append(i)
	return faktorji


def najdemo_prafaktrje_ucinkovit(stevilo):
	faktorji = []
	for i in range(1, int((stevilo) ** (1 / 2)) + 1):
		if stevilo % i == 0:
			faktorji.append(i)
			faktorji.append(stevilo // i)
	return faktorji

def ali_je_prafaktor_prastevilo(stevilo):
	return len(najdemo_prafaktrje_ucinkovit(stevilo)) == 2

def najvecji_prafaktor_ki_je_prastevilo(stevilo):
	najvecji_prafaktor = 0
	for faktor in najdemo_prafaktrje_ucinkovit(stevilo):
		if ali_je_prafaktor_prastevilo(faktor) == True:
			if faktor > najvecji_prafaktor:
				najvecji_prafaktor = faktor
	return najvecji_prafaktor 

print(najvecji_prafaktor_ki_je_prastevilo(600851475143))
6857