def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


def instructions():
    print("****How to play****")
    print()
    print('Rules go here')
    print()
    return ""


while True:
    show_instructions = yes_no("Do you want to see the instructions? ")

    if show_instructions == "yes":
        instructions()
    else:
        print("Program continues")
