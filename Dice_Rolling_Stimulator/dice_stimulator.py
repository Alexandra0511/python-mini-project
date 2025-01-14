""" dice simulator """
from random import SystemRandom

print("This is a dice stimulator")
X = "y"
CRYPTO_GEN = SystemRandom()
while X == "y":
    number = CRYPTO_GEN.randrange(1, 6)

    if number == 1:
        print("===========")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("===========")

    if number == 2:
        print("===========")
        print("|         |")
        print("| O     O |")
        print("|         |")
        print("===========")

    if number == 3:
        print("===========")
        print("|    O    |")
        print("|    O    |")
        print("|    O    |")
        print("===========")

    if number == 4:
        print("===========")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print("===========")

    if number == 5:
        print("===========")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print("===========")

    if number == 6:
        print("===========")
        print("| O     O |")
        print("| O     O |")
        print("| O     O |")
        print("===========")

    X = input("Press y to roll again ")
