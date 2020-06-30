### Leksigografske permutacije
## Permutacije so zakon 
from itertools import*

def seznam_permutacij():
	return list(permutations(range(10)))[999999]

print(seznam_permutacij())
(2, 7, 8, 3, 9, 1, 5, 4, 6, 0)