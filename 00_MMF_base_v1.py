# import statements

# functions go here


# number checker
def num_check(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response <= 0:
                print("error")
            else:
                return response

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
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0


while name != "xxx" and ticket_count < MAX_TICKETS:

    # tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))

    else:
        print("*** you have one seat left ***")

    # get details

    # get name (can't be blank)
    name = not_blank("Name: ")

    # end loop if the exit code is entered
    if name == "xxx":
        break

    # get age between 12 and 130
    age = num_check("Age: ")

    # check that age is valid
    if age < 12:
        print("Sorry you are too young to view this movie")
        continue

    elif age > 130:
        print("You are too old")
        continue

    # Calculate ticket price
    if age < 16:
        ticket_price = 7.5

    elif age < 65:
        ticket_price = 10.5

    else:
        ticket_price = 6.5

    ticket_count += 1
    ticket_sales += ticket_price

# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# prints that all tickets are sold
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets")

else:
    print("You have sold {} tickets.\n"
          "There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))

    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge of necessary)

# Calculate total sales and profit

# output data to text file
