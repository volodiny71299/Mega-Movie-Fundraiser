

def yes_no(question):

    error = "please answer yes/no"

    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input(question).lower()
        if response == "yes" or response == "y":
            return response
        elif response == "no" or response == "n":
            return response
        else:
            print(error)



# Main routine goes here

for item in range(0, 6):
    want_snacks = yes_no("Do you want snacks? ")
    print("Answer ok, you said: ", want_snacks)
    print()