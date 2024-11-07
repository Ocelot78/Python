
hasla = open("hasla.txt", "r")
odpa = open("wynik4a.txt", "w")
odpb = open("wynik4b.txt", "w")
odpc = open("wynik4c.txt", "w")


liczba_parzyste = 0
liczba_nieparzyste = 0
palindromy = []
hasla_z_suma_ascii = []

for haslo in hasla:
    haslo = haslo.strip()  


    if len(haslo) % 2 == 0:
        liczba_parzyste += 1
    else:
        liczba_nieparzyste += 1

    if haslo == haslo[::-1]: 
        palindromy.append(haslo)

    znaleziono_pare = False
    for i in range(len(haslo) - 1):
        if ord(haslo[i]) + ord(haslo[i + 1]) == 220:
            hasla_z_suma_ascii.append(haslo)
            znaleziono_pare = True
            break  

odpa.write(f"Liczba parzystych: {liczba_parzyste}\n")
odpa.write(f"Liczba nieparzystych: {liczba_nieparzyste}\n")


for palindrom in palindromy:
    odpb.write(palindrom + "\n")

for haslo in hasla_z_suma_ascii:
    odpc.write(haslo + "\n")


