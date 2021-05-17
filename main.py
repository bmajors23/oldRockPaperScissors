import random

print("\nLet's play Rock Paper Scissors!\n")

win = 0
lose = 0
tie = 0

while True:

    n = random.randint(0, 2)

    print("Rock, Paper or Scissors?\n")

    RPS = input("")

    if RPS.upper() == "ROCK" and n == 0:
        tie += 1
        print("\nYou played Rock, and the computer played Rock. It's a draw!\n"
              "\nYour current W/L/T record is: " + str(win) + "/" + str(lose) + "/" + str(tie) + ".\n")
    elif RPS.upper() == "ROCK" and n == 1:
        lose += 1
        print("\nYou played Rock, and the computer played Paper. You lose!\n"
              "\nYour current W/L/T record is: " + str(win) + "/" + str(lose) + "/" + str(tie) + ".\n")
    elif RPS.upper() == "ROCK" and n == 2:
        win += 1
        print("\nYou played Rock, and the computer played Scissors. You win!\n"
              "\nYour current W/L/T record is: " + str(win) + "/" + str(lose) + "/" + str(tie) + ".\n")
    elif RPS.upper() == "PAPER" and n == 0:
        win += 1
        print("\nYou played Paper, and the computer played Rock. You win!\n"
              "\nYour current W/L/T record is: " + str(win) + "/" + str(lose) + "/" + str(tie) + ".\n")
    elif RPS.upper() == "PAPER" and n == 1:
        tie += 1
        print("\nYou played Paper, and the computer played Paper. It's a draw!\n"
              "\nYour current W/L/T record is: " + str(win) + "/" + str(lose) + "/" + str(tie) + ".\n")
    elif RPS.upper() == "PAPER" and n == 2:
        lose += 1
        print("\nYou played Paper, and the computer played Scissors. You lose!\n"
              "\nYour current W/L/T record is: " + str(win) + "/" + str(lose) + "/" + str(tie) + ".\n")
    elif RPS.upper() == "SCISSORS" and n == 0:
        lose += 1
        print("\nYou played Scissors, and the computer played Rock. You lose!\n"
              "\nYour current W/L/T record is: " + str(win) + "/" + str(lose) + "/" + str(tie) + ".\n")
    elif RPS.upper() == "SCISSORS" and n == 1:
        win += 1
        print("\nYou played Scissors, and the computer played Paper. You win!\n"
              "\nYour current W/L/T record is: " + str(win) + "/" + str(lose) + "/" + str(tie) + ".\n")
    elif RPS.upper() == "SCISSORS" and n == 2:
        tie += 1
        print("\nYou played Scissors, and the computer played Scissors. It's a draw!\n"
              "\nYour current W/L/T record is: " + str(win) + "/" + str(lose) + "/" + str(tie) + ".\n")
    else:
        print("\nInvalid Response, please answer with the word 'rock' 'paper' or 'scissors'\n")

