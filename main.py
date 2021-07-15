import random


def main():
    print("Welcome to Rock Paper Scissors")
    print("Select: (1)Rock (2)Paper (3)Scissors")
    userChoice = input()
    cpuChoice = random.randint(1, 3)
    if (int(userChoice) == cpuChoice):
        print("You both chose the same. Try again.")
    elif (int(userChoice) == 1 and cpuChoice == 2):
        print("Paper beats rock. CPU wins.")
    elif (int(userChoice) == 1 and cpuChoice == 3):
        print("Rock beats scissors. You win.")
    elif (int(userChoice) == 2 and cpuChoice == 1):
        print("Paper beats rock. You win.")
    elif (int(userChoice) == 2 and cpuChoice == 3):
        print("Scissors beats paper. CPU wins.")


main()
