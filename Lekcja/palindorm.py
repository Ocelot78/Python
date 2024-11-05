with open ('C:/Users/sala22/Desktop/Lekcja/dane.txt','r') as file:
    dane = file.read().split()
counter_add = 0
for slowo in dane:
    if len(slowo) % 2 == 1:
        counter_add += 1
print(f"Liczba słów o nieparzystej długości, {counter_add}")
