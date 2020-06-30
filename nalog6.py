#Naloga 6 
def razlika_med_kvadrati_stevil_in_vsoto_kvadratov_stevil(n):
	return vsota_stevil_stevil_in_potem_kvadriramo(n) - vsota_kvadratov_stevil(n)

def vsota_kvadratov_stevil(n):
	vsota = 0
	for i in range(n + 1):
		vsota += i ** 2
	return vsota 

def vsota_stevil_stevil_in_potem_kvadriramo(n):
	vsota = 0
	for i in range(n + 1):
		vsota += i 
	return vsota ** 2

print(razlika_med_kvadrati_stevil_in_vsoto_kvadratov_stevil(100))
25164150