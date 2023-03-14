bal = 5

rounds_played = 0

play_again = input("Press enter to start playing").lower()

while play_again == "":
    rounds_played += 1
    print("")
    print("| Round", "#" + str(rounds_played) + ":")
    bal -= 1
    print(f"| Balance: ${bal:.2f}")
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
