import random


def choice(a):
    if (a == 1):
        print("Stone")
    elif (a == 2):
        print("Paper")
    else:
        print("Scissors")


def game(a, b):

    print("Your Choice : ", end="")
    choice(a)
    print("Computer's Choice : ", end="")
    choice(b)

    if (a == b):
        print("Draw !")
    elif ((a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1)):
        print("You Lose !")
    else:
        print("You Win !")


user = int(input("1.Stone \n2.Paper \n3.Scissors \nEnter Choice : "))

computer = random.randint(1, 3)

game(user, computer)
