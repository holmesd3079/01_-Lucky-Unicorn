import random
bal = 5

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

    print("You got a dead", chosen + "!")
    gain = bal - oldbal
    print(f" Balance: ${bal:.2f} (gained ${gain:.2f})")
    if bal > 1:
        print("|")
        print("|")
        print()
        play_again = input("| Press Enter to play again or 'xxx' to quit")
    else:
        print("|___________________")
        print("| Your now poor come back when you beg for more")
        play_again = "xxx"

print(" ______________________")
print(f"| Final Balance: ${bal:.2f} |")
