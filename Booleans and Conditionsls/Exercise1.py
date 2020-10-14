while True:
    user_input = input("How far would you like to travel in miles?: ")
    user_input_converted = int(user_input)
    if user_input_converted < 3:
        print("I suggest you walk to your destination")
    elif user_input_converted <= 300:
        print("I suggest you drive to your destination")
    else:
        print("I suggest flying to your destination")
    
    finish = input("Continue? Yes/No: ").capitalize().strip()
    if finish == 'Yes':
        continue
    else:
        break 