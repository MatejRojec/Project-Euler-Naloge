#4. naloga
# iščemo palindrom, ki je simetricen glede smeri torej 91 * 99 = 9009 (simetrija, enako kot za besede)
# to je najvecje za dvomestna
# kaj pa za vecmestna 
# ideja
# za vsa stevila v range(100) pogledamo 


def je_palindorm(i):
	return str(i) == str(i)[::-1]

def najde_palindrom(n, m):
	najvecji = 0
	for i in range(n, m):
		for j in range(n, m):
			p = i * j
			if je_palindorm(p) == True and p > najvecji:
				najvecji = p
	return(najvecji) 

print(najde_palindrom(100,1000))
906609
