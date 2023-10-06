def winnerConditions(user_action, computer_action):
    if user_action == computer_action:
        return ("It's a TIE!", True, True)
    elif user_action == 1:
        if computer_action == 3:
            return ("Rock smashes Scissors. You WON!", True, False)
        else:
            return ("Paper covers Rock. You LOST!", False, True)
    elif user_action == 2:
        if computer_action == 1:
            return ("Paper covers Rock. You WON!", True, False)
        else:
            return ("Scissors cuts Paper. You LOST!", False, True)
    elif user_action == 3:
        if computer_action == 2:
            return ("Scissors cuts Paper. You WON!", True, False)
        else:
            return ("Rock smashes Scissors. You LOST!", False, True)