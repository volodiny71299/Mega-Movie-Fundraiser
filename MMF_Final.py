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
        ["popcorn", "p", "pop", "corn", "a"],
        ["M&Ms", "m&ms", ["M&M's"], "mms", "mm", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "h2o", "d"],
        ["orange juice", "OJ", "oj", "juice", "orange", "o", "e"],
    ]

    # holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx" or desired_snack != "n":

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
        # snack_choice = string_check(desired_snack, valid_snacks)

        snack_choice = string_check(desired_snack, valid_snacks)
        if snack_choice == "invalid choice":
            print("please choose a valid snack")

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


def currency(x):
    return "${:.2f}".format(x)


def instructions(option):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions? ")
        show_help = string_check(show_help, option)

    if show_help == "Yes":
        print()
        print("*** Mega Movie Fundraiser Instructions ***")
        print()
        print("Instructions go here. They are brief but helpful")

    return ""


# set up dictionaries / lists needed to hold data

# list for valid yes / no response
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# list of valid responses for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

MAX_TICKETS = 150

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

# store surcharge multiplier
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# List to store summary data...

summary_headings = ["Popcorn", "M&M's", "Pita Chips", "Water", "Orange Juice"]

summary_data = []

profit_names = ["Snack", "Ticket", "Total"]
profit_data = []

# store surcharge multiplier
surcharge_mult_list = []

# Data frame dictionaries
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_mult_list
    }

summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

profit_data_dict = {
    'Profit': profit_names,
    'Amount': profit_data
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
instructions(yes_no)

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

    # get snack
    snack_order = get_snack()

    # assume no snacks have been bought
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # get payment method (ie: work out if surcharge is needed)
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit)? ").lower()
        how_pay = string_check(how_pay, pay_method)
        if how_pay == "invalid choice":
            print("Please try again")

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_mult_list.append(surcharge_multiplier)

# end of tickets / snacks / payment loop

# print details...
# create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it price for snacks and ticket

pandas.set_option('precision', 2)

# print out snack dataframe
movie_frame["Snacks"] = \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Snacks']

movie_frame["Surcharge"] = movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# movie_frame

# shorten column names
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ', 'Pita Chips': 'Chips', 'Surcharge_Multiplier': 'SM'})

# set up summary dataframe
# populate snack items
for item in snack_lists:
    # sum items in each snack list
    summary_data.append(sum(item))


# get snack profit
# get snack total from pandas
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2

# get ticket profit and add to list
ticket_profit = ticket_sales - (5 * ticket_count)

# work out total profit and add to list
total_profit = snack_profit + ticket_profit

"""
profit_data.append(snack_profit)
profit_data.append(ticket_profit)
profit_data.append(total_profit)
"""

dollar_amount = [snack_profit, ticket_profit, total_profit]
for item in dollar_amount:
    item = "${:.2f}".format(item)
    profit_data.append(item)


# Create summary frame
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

# Create profit frame
profit_frame = pandas.DataFrame(profit_data_dict)
profit_frame = profit_frame.set_index('Profit')

# set up columns to be printed
pandas.set_option('display.max_columns', None)

# *** Pre Printing / Export ***
# Format currenct Values so they have $'s

# ticket details formatting (uses currency function)
add_dollars = ['Ticket', 'Snacks', 'Surcharge', 'Total', 'Sub Total']
for item in add_dollars:
    movie_frame[item] = movie_frame[item].apply(currency)

# write each frame to a separate csv files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_details.csv")
profit_frame.to_csv("profit_summary.csv")


print()
print("*** Ticket / Snack Information ***")
print("Note: for full details, please see the excel file called 'Ticket_Summary'")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total', 'Surcharge', 'Total']])

print()

print("*** Snack / Profit Summary ***")
print()
print(summary_frame)

print()

print(profit_frame)

print()


# tell user if they have unsold tickets...
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")

elif ticket_count == 1:
    print("You have sold 1 ticket\nThere are still 4 seats still available")

elif MAX_TICKETS - ticket_count == 1:
    print("You have sold {} tickets\nThere is still {} seat available".format(ticket_count, MAX_TICKETS-ticket_count))

else:
    print("You have sold {} tickets\nThere are still {} seats available".format(ticket_count, MAX_TICKETS-ticket_count))
