# Naloga 10

def najdemo_prafaktrje_ucinkovit(stevilo):
	faktorji = []
	for i in range(1, int((stevilo) ** (1 / 2)) + 1):
		if stevilo % i == 0:
			faktorji.append(i)
			faktorji.append(stevilo // i)
	return faktorji

def ali_je_prafaktor_prastevilo(stevilo):
	return len(najdemo_prafaktrje_ucinkovit(stevilo)) == 2

def seznam_prastevil(stevilo):
    n = []
    m = 0
    while len(n) <= stevilo:
        if ali_je_prafaktor_prastevilo(m) == True:
            n += [m]
        m += 1 
    return sum(n)
print(seznam_prastevil(2000000))
142913828922
# trajalo je zelo dologo casa za resitev, če bi bila se ena nicla verjetno bi trajalo zeelo dolgo casa