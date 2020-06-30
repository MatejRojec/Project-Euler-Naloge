# Naloga 29
def main():
    list_stevil = []
    for a in range(2, 101):
        for b in range(2, 101):
            stevilo = a ** b
            list_stevil.append(stevilo)
    nov_list = []
    for i in list_stevil:
        if i not in nov_list:
            nov_list.append(i)
    return len(nov_list)
