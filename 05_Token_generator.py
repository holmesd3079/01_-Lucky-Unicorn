import random

STARTING_BALANCE = 100
bal = STARTING_BALANCE

for item in range(0, 21):
    oldbal = bal
    tokens = ["unicorn", "horse", "horse", "horse", "zebra", "zebra", "zebra", "donkey", "donkey", "donkey"]
    chosen = random.choice(tokens)
    if chosen == "unicorn":
        bal += 4
    elif chosen == "donkey":
        bal -= 1
    else:
        bal -= 0.5

    print(chosen, end="\t")
    gain = bal - oldbal
    print(f"             Balance: ${bal} (gained ${gain})")
print(" __________           ________________________________________________")
print(f"| Tokens                  Token & balance  You now have: ${bal}")
print("|")
gain_stats = ''
if STARTING_BALANCE > bal:
    gain_stats = "you lost money"
elif STARTING_BALANCE < bal:
    gain_stats = "you gained coin"
else:
    print("You landed on 100!"
          "$4 bonus")
    bal += 4

print(f'| I think you started with {STARTING_BALANCE} now you {gain_stats} (${bal})')
