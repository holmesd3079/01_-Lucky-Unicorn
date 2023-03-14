import random


# Decoration around animal
def statement_generator(statement, decoration):
    middle = f'{decoration.upper() * 3} | {statement}! | {decoration.upper() * 3}'
    top_bottom = decoration.upper() * len(middle)

    print(top_bottom)
    print(middle)
    print(top_bottom)


# checks users enter yes / no to a given question
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


# Displays the instructions (returns None)
def instructions():
    print("****How to play****")
    print()
    print('Rules go here')
    print()
    return ""


# checks users enter an integer between a low and high number
def num_check(question, low, high):
    error: str = "Please enter a whole Number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here
welcome = "Welcome to lucky Unicorn"
statement_generator(welcome, "*")

print()
show_instructions = yes_no("Do you want to see the instructions? ")

if show_instructions == "yes":
    instructions()

how_much = num_check("How much would you like "
                     "to play with? ", 0, 10)

bal = how_much

rounds_played = 0

play_again = input("Press enter to start playing").lower()

while play_again == "":
    rounds_played += 1
    print("")
    print("| Round", "#" + str(rounds_played) + ":")

    oldbal = bal
    chosen_num = random.randint(1, 100)
    horse_zebra = ["horse", "zebra"]

    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        bal += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        bal -= 1
    else:
        chosen = random.choice(horse_zebra)
        bal -= 0.5

    feedback = f'You got a {chosen}'
    statement_generator(feedback, chosen[0])

    gain = bal - oldbal
    print(f" Balance: ${bal:.2f} (gained ${gain:.2f})")

    if bal > 1:
        print("|")
        print("|")
        print()
        play_again = input("| Press Enter to play again or 'xxx' to quit")
    else:
        print("|___________________")
        print("| You're now poor come back when you beg for more")
        play_again = "xxx"

print(" ______________________")
print(f"| Final Balance: ${bal:.2f} |")
