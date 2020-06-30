# Naloga 5 
# Neka funkcija ki pove ali je deljivo z vsemi stevili od x do y 
# najdemo stevilo -> stop

def je_deljivo_s_stevili_ena_do_dvajset(n):
	for i in range(2, 21):
		if n % i != 0:
			return False
	return True

n = 20
while True:
	if je_deljivo_s_stevili_ena_do_dvajset(n):
		break
	n += 20
print(n)
232792560
# Opomba: Program je rabil nekaj sekund, da se je izvedel.