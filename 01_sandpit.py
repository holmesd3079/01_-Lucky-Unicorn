# to join strings (string concatenation)
import time

my_name = "Miss G"
fav_food = "Coffee"

print(f"{my_name} really, really, loves {fav_food}")
print("{} really loves her {}".format(my_name, fav_food))
print(my_name, fav_food)
print(my_name + fav_food)

welcome = "Typing this text be inpatient..."

type_welcome = ""

for letters in welcome:

    type_welcome = type_welcome + letters

    for number in range(1,21):
        print()
    print(type_welcome)
    if letters == ".":
        time.sleep(0.4)
    else:
        time.sleep(0.1)
