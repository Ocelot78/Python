dane = open("dane.txt", "r")
odp = open('zadanie4.txt','w')

def palindrom_jest(dane):
    return dane == dane[::-1]

def znajdz_palindromy(dane, odp):
    for linia in dane:
        tekst = linia.strip()
        if palindrom_jest(tekst):
            odp.write(tekst + '\n')

with open("dane.txt", "r") as dane, open("zadanie4.txt", "w") as odp:
    znajdz_palindromy(dane, odp)
