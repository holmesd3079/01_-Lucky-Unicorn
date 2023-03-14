def num_check(question,low,high):
    error: str = "Please enter a whole Number between 1 and 10\n"
    
    valid = False
    while not valid:
        try:
                response = int(input(question))
                if low < response <= high:
                    print("You have asked to play "
                          "with ${}".format(response))
    
    
                else:
                    print(error)
    
        except ValueError:
            print(error)






how_much = num_check("How much would you like "
                     "to play with", 0 , 10)