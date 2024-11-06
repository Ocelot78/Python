from time import sleep
import random
nazwa = input("Name of the lootbox (small text i space = _): ")
steamid = int(input("Enter your steam id: "))
los = random.randint(0,1)
for i in range(2):
    print("Analizing box.")
    sleep(1)
    print("Analizing box..")
    sleep(1)
    print("Analizing box...")
win = random.randint(0,10)
win2 = random.randint(80,100)
if los == 1:
    print(str(win) +"% chance of winning")
else:
    print(str(win2) +"% chance of winning")
    