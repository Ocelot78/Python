import math

with open("PARY_LICZB.TXT", "r") as file:
    pairs = [line.strip().split() for line in file]
    pairs = [(int(liczba1), int(liczba2)) for liczba1, liczba2 in pairs]

odpa = 0
odpb = 0 
odpc = 0  
for liczba1, liczba2 in pairs:
    if liczba1 % liczba2 == 0 or liczba2 % liczba1 == 0:
        odpa += 1
    if math.gcd(liczba1, liczba2) == 1:
        odpb += 1
    suma_cyfr1 = sum(int(cyfra) for cyfra in str(liczba1))
    suma_cyfr2 = sum(int(cyfra) for cyfra in str(liczba2))
    if suma_cyfr1 == suma_cyfr2:
       odpc += 1
with open("ZADANIE5.TXT", "w") as odp:
    odp.write(f"a)Wielokrotności:  {odpa}\n")
    odp.write(f"b)Wzglednie pierwsze i nww =1: {odpb}\n")
    odp.write(f"c)Suma cyfr: {odpc}\n")