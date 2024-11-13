plik = open('cyfry.txt', 'r')
liczby = []
for linia in plik:
    liczby.append(int(linia.strip()))
plik.close()

wynik = open('zadanie4.txt', 'w')

licznik_parzystych = 0
for liczba in liczby:
    if liczba % 2 == 0:
        licznik_parzystych += 1

wynik.write("a) Liczba parzystych liczb: " + str(licznik_parzystych) + "\n")

najwieksza_suma = -1
najmniejsza_suma = float('inf')
liczba_max_suma = None
liczba_min_suma = None

for liczba in liczby:
    suma_cyfr = 0
    for cyfra in str(liczba):
        suma_cyfr += int(cyfra)
    
    if suma_cyfr > najwieksza_suma:
        najwieksza_suma = suma_cyfr
        liczba_max_suma = liczba
    
    if suma_cyfr < najmniejsza_suma:
        najmniejsza_suma = suma_cyfr
        liczba_min_suma = liczba

wynik.write("b) Liczba z największą sumą cyfr: " + str(liczba_max_suma) + "\n")
wynik.write("   Liczba z najmniejszą sumą cyfr: " + str(liczba_min_suma) + "\n")

wynik.write("c) Liczby, których cyfry tworzą ciąg rosnący:\n")

for liczba in liczby:
    cyfry_rosnace = True
    cyfry = str(liczba)
    
    for i in range(len(cyfry) - 1):
        if cyfry[i] >= cyfry[i + 1]:
            cyfry_rosnace = False
            break

    if cyfry_rosnace:
        wynik.write(str(liczba) + "\n")

wynik.close()
