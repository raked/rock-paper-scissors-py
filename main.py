import random


def main():
    print("Welcome to Rock Paper Scissors")
    print("Select: (1)Rock (2)Paper (3)Scissors")
    userChoice = input()
    cpuChoice = random.randint(1, 3)
    if (int(userChoice) == cpuChoice):
        print("You both chose the same. Try again.")


main()
