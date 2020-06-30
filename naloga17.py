# Naloga 17 

def sesteje_vse_crke_stevil_v_angleski_abecedi():
	vsota = sum(len(v_angleskem(i)) for i in range(1, 1001))
	return vsota


def v_angleskem(n):
	if 0 <= n < 20:
		return enke[n]
	elif 20 <= n < 100:
		return desetice[n // 10] + (enke[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return enke[n // 100] + "hundred" + (("and" + v_angleskem(n % 100)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return v_angleskem(n // 1000) + "thousand" + (v_angleskem(n % 1000) if (n % 1000 != 0) else "")
	else:
		pass


enke = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
desetice = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

print(sesteje_vse_crke_stevil_v_angleski_abecedi())
21124