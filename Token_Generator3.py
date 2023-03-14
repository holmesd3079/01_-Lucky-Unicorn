def statement_generator(statement, decoration):
    middle = f'{decoration * 3} {statement} {decoration * 3}'
    top_bottom = decoration * len(middle)

    print(top_bottom)
    print(middle)
    print(top_bottom)


# main routine goes here
tokens = ["unicorn", "zebra", "horse", "donkey"]

for item in tokens:
    feedback = f'You got a {item}'
    statement_generator(feedback, item[0].upper())
    print()
