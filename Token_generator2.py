import random

# Starting balance
STARTING_BALANCE = 100
bal = STARTING_BALANCE

# start loop
for item in range(0, 11):
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

    # print(item, "  You got a dead", chosen)

    # outputs round and result separated by two tabs
    print(f"Round: {item} \t\t You got a dead {chosen}")

    gain = bal - oldbal
    print(f"             Balance: ${bal:.2f} (gained ${gain:.2f})")
    print("                                                           |")
print(" __________           ______________________________________")
print(f"| Tokens             Token & balance  You now have: ${bal}")
print("|")
gain_stats = ''
if STARTING_BALANCE > bal:
    gain_stats = "you lost money"
elif STARTING_BALANCE < bal:
    gain_stats = "you gained coin"
else:
    print("You landed on $100 "
          "$4 bonus! 💹")
    bal += 4

print(f'| I think you started with {STARTING_BALANCE} now you {gain_stats} (${bal})')
