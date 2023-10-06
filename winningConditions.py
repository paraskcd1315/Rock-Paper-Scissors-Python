def winnerConditions(user_action, computer_action):
    if user_action == computer_action:
        return ("It's a TIE!", True, True)
    elif user_action == 1:
        if computer_action == 3:
            return ("🪨 smashes ✂️. You WON!", True, False)
        else:
            return ("📃 covers 🪨. You LOST!", False, True)
    elif user_action == 2:
        if computer_action == 1:
            return ("📃 covers 🪨. You WON!", True, False)
        else:
            return ("✂️ cuts 📃. You LOST!", False, True)
    elif user_action == 3:
        if computer_action == 2:
            return ("✂️ cuts 📃. You WON!", True, False)
        else:
            return ("🪨 smashes ✂️. You LOST!", False, True)