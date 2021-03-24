# import statements
import re
import pandas
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


# getting ticket
def get_ticket_price():

    # get age (between 12 and 130)
    age = num_check("Age: ")

    # check that age is valid
    if age < 12:
        print("Sorry you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print("You are too old!")
        return "invalid choice"

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price


# Ticket limits
def check_tickets(tickets_sold, ticket_limit):
    # tells user how many seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats left".format(ticket_limit - tickets_sold))

    # warns user that only one seat is left!
    else:
        print("***There is one seat left!!***")
        return ""


# string checker
def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return the full
        if choice in var_list:

            # get full name of snack and put it in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not ok - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# get snacks
def get_snack():

    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # Valid snack holds list of all snacks
    # Each item in valid snacks is a list with valid options for each snack <full name, letter code (a - e)
    # and possible abbreviations eto>

    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&M's", "m&m's", "mms", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
        ["orange juice", "OJ", "oj", "juice", "orange", "o", "e"],
    ]

    # holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number, separate it into two (number/item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # removes white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack AND amount to list...

        snack_row.append(amount)
        snack_row.append(snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)


# set up dictionaries / lists needed to hold data

# list for valid yes / no response
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# list of valid responses for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "ca"]
]

MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# initialise lists (to make data-frame in due courses)
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Data frame dictionaries
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    }

# cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    "M&Ms": 3,
    'Orange Juice': 3.25
}


# ask user if they have used the program before and show instructions

# loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # check numbers of ticket limit has not bee exceeded
    check_tickets(ticket_count, MAX_TICKETS)

    # *** get details for each ticket ***

    # get name (can't be blank)
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # get ticket price based on age
    ticket_price = get_ticket_price()
    # if age is invalid, restart loop (and get the name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # ask user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)

        if check_snack == "invalid choice":
            print("Please say yes / no")

    # if they say yes, ask what snacks they want (and add to our snack_order list)
    if check_snack == "Yes":
        get_order = get_snack()
    else:
        get_order = []

    print()
    if len(get_order) == 0:
        print("Snacks Ordered: None")

    else:
        print("Snacks Ordered:")

        print(get_order)

    # get payment method (ie: work out if surcharge is needed)

# end of tickets / snacks / payment loop

# print details...
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# calculate ticket profit...
ticket_profit = ticket_sales - (5*ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# tell user if they have unsold tickets...
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")

elif ticket_count == 1:
    print("You have sold 1 ticket\nThere are still 4 seats still available".format(ticket_count))

elif MAX_TICKETS - ticket_count == 1:
    print("You have sold {} tickets\nThere is still {} seat available".format(ticket_count, MAX_TICKETS-ticket_count))

else:
    print("You have sold {} tickets\nThere are still {} seats available".format(ticket_count, MAX_TICKETS-ticket_count))
