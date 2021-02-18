# import statements

# functions go here


# number checker
def num_check(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                valid = True
                return response

            # Tells user if they are too old or too young for the movie
            else:
                if response > high:
                    print("Age entered is too high")
                else:
                    print("You are too young for this movie")

        except ValueError:
            print("Invalid input")


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

# start of loop

# initial loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
        print("You have {} seats left".format(MAX_TICKETS - count))

    else:
        print("*** you have one seat left ***")

    # get details

    # get name (can't be blank)
    name = not_blank("Name: ")
    print()

    if name == "xxx":
        print("You have sold {} tickets\nThere are {} places still available".format(count, MAX_TICKETS - count))

    count += 1

    age = num_check("Age: ", 12, 130)

if count == MAX_TICKETS:
    print("You have sold all the available tickets")

    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge of necessary)

# Calculate total sales and profit

# output data to text file
