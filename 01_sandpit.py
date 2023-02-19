# Video example but tweaked more freely
num_1 = int (input("Choose number: "))
num_2 = int (input("What do you want to times it by? "))
# print(Number, "x", Times, "=" .format(Number * Times))

magic_calc = input("Enter an expression")
calc_ans = eval(magic_calc)

print("{} x {} = {}".format(num_1, num_2, num_1 * num_2))

print(calc_ans)
