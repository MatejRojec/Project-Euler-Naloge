# Naloga 22

def tocke_imena(ime):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    tocke = 0
    for i in ime:
        stevec = 1
        for j in alphabet:
            if j == i:
                tocke += stevec
            else:
                stevec += 1 
    return tocke

def izracuna_ravno_to_kar_pise_v_navodilu_naloge():
    with open("names.txt") as file:
        names_file = file
        names_list = []
        for i in names_file:
            names_list.append(i)
    
    new_list = names_list[0].split(',')
    sorted_list = sorted(new_list)
    sum_of_scores = 0
    stevec = 1
    for i in sorted_list: 
        sum_of_scores += stevec * tocke_imena(i)
        stevec += 1
    return sum_of_scores
   
print(izracuna_ravno_to_kar_pise_v_navodilu_naloge())   
871198282
