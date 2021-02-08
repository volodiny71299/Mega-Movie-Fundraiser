# import statements

# functions go here

def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response

        else:
            print("sorry - this cannot be blank")

# **********main routine**********

name = not_blank("name: ")

# Set up dictionaries/lists needed to hold data

# Ask user if they have used the program before and show instructions if necessary

# loop to get ticket details

    # get name (can't be blank)

    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge of necessary)

# Calculate total sales and profit

# output data to text file
