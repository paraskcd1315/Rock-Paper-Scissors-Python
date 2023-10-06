def winnerConditions(user_action, computer_action):
    if user_action == computer_action:
        return "It's a TIE!"
    elif user_action == 1:
        if computer_action == 3:
            return "Rock smashes Scissors. You WON!"
        else:
            return "Paper covers Rock. You LOST!"
    elif user_action == 2:
        if computer_action == 1:
            return "Paper covers Rock. You WON!"
        else:
            return "Scissors cuts Paper. You LOST!"
    elif user_action == 3:
        if computer_action == 2:
            return "Scissors cuts Paper. You WON!"
        else:
            return "Rock smashes Scissors. You LOST!"