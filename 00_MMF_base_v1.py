# import statements

# functions go here

# checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response

        # if name is blank, show error (and repeat loop)
        else:
            print("sorry - this can't be blank, please enter your name")

# **********main routine**********

# Set up dictionaries/lists needed to hold data

# Ask user if they have used the program before and show instructions if necessary

# loop to get ticket details

    # get name (can't be blank)
    name = not_blank("name: ")

    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge of necessary)

# Calculate total sales and profit

# output data to text file
