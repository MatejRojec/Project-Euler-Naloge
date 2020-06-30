# Naloga 7
def najdemo_prafaktrje_ucinkovit(stevilo):
	faktorji = []
	for i in range(1, int((stevilo) ** (1 / 2)) + 1):
		if stevilo % i == 0:
			faktorji.append(i)
			faktorji.append(stevilo // i)
	return faktorji

def ali_je_prafaktor_prastevilo(stevilo):
	return len(najdemo_prafaktrje_ucinkovit(stevilo)) == 2

def najveje_prastevilo(stevilo):
    n = []
    m = 0
    while len(n) <= stevilo:
        if ali_je_prafaktor_prastevilo(m) == True:
            n += [m]
        m += 1 
    return n[-1]
print(najveje_prastevilo(10001)) 
104743