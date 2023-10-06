"""
--------------------
Rock, Paper, Scissor
--------------------

- Will be played with user and machine

- Should have a container where user and machine both needs to choose from
    - This container will save the values of Rock, Paper and Scissor

- Both user and machine can only choose one value from this container.
    - Program should be able to ask input from the user
    - Machine should be able to choose a random value from the container automatically.

- Program should check both values and provide a winner in the end.

"""

import random
import constants
from winningConditions import winnerConditions
import os

userScore = 0
machineScore = 0

while True:
    try:
        user_action = int(input(constants.MENU))
        computer_action = random.randint(1, 3)

        if 0 < user_action <= 3:
            print(f"\nYou chose {constants.POSSIBLE_ACTIONS[user_action]}, Computer chose {constants.POSSIBLE_ACTIONS[computer_action]}")
            winner = winnerConditions(user_action, computer_action)

            if winner[1] == True:
                userScore += 1
            else:
                if userScore != 0:
                    userScore -= 1

            if winner[2] == True:
                machineScore += 1
            else:
                if machineScore != 0:
                    machineScore -= 1

            print("\n" + winner[0])
            print(f"""
-----------------------------
            SCORE
Your Score      Machine Score
    {userScore}                 {machineScore}
-----------------------------
            """)

            askUser = input("\nWould you like to play again? y for yes n for no - ")
            if askUser.lower() == "y":
                os.system('cls')
                continue
            elif askUser.lower() == "n":
                os.system('cls')
                print(f"""
-----------------------------
            SCORE
Your Score      Machine Score
    {userScore}                 {machineScore}
-----------------------------
            """)
                print("\nThanks for playing")
                break
            else:
                raise

        elif user_action == 4:
            os.system('cls')
            print(f"""
-----------------------------
            SCORE
Your Score      Machine Score
    {userScore}                 {machineScore}
-----------------------------
            """)
            print("\nThanks for playing.")
            break

        else:
            raise

    except:
        os.system('cls')
        print("\nIncorrect Option. Closing game.")
        break
        
