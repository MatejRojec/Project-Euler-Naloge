# 2. naloga
def izracuna_vse_sode_clene_fibbonacija_do_nekega_stevila(n):
	vsota = 0  
	x = 1   # privzeta pogoja 
	y = 2   # fibonnacija
	while x <= n:
		if x % 2 == 0:
			vsota += x
		x, y = y, x + y  # dobimo naslednji clen fibbonaccija
	return vsota
print(izracuna_vse_sode_clene_fibbonacija_do_nekega_stevila(4000000))
4613732