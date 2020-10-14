while True:
    user_input = input("Please type something and press enter: ")
    print("You entered:")
    print(user_input)
    finish = input("Continue? Yes/No: ").capitalize().strip()
    if finish == 'Yes':
        continue
    else:
        break 