
while True:
    show_instructions = input("Do you want to see the instructions? ").lower()

    if show_instructions == "yes" or show_instructions == "y":
        print("Instructions go here")
    elif show_instructions == "no" or show_instructions == "n":
        print("Game starts here")
    else:
        print('Your supposed to answer properly')
