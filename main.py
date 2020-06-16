import random

print("This is a Dice Rolling Simulator ")
Answer = input("Press 'y' to toll the dice and 'n' to exit \n ")


while Answer == "y":
    Number = random.randint(1, 6)
    if Number == 1:
        print("----------")
        print("|        |")
        print("|    0   |")
        print("|        |")
        print("----------")
    if Number == 2:
        print("----------")
        print("|        |")
        print("| 0    0 |")
        print("|        |")
        print("----------")
    if Number == 3:
        print("----------")
        print("|      0|")
        print("|   0   |")
        print("|0      |")
        print("----------")
    if Number == 4:
        print("----------")
        print("|0     0|")
        print("|       |")
        print("|0     0|")
        print("----------")
    if Number == 5:
        print("----------")
        print("|0     0|")
        print("|   0   |")
        print("|0     0|")
        print("----------")
    if Number == 6:
        print("----------")
        print("|0     0|")
        print("|0     0|")
        print("|0     0|")
        print("----------")

    Answer = input("Press 'y' to toll the dice again 'n' to exit \n")







