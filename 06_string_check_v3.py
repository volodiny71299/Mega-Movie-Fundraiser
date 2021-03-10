import re


# function goes here
def string_check(choice, options):

    for var_list in options:

        #if the snack is in one of the lists, return the full
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
]

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# holds snack order for a single user
snack_order = []

# ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

# if they say yes, ask what snacks they want (and add to our snack_order list)
if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":
        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        # if item has a number, separate it into two (number/item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # removies white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack AND amount to list...
        amount_snack = "{} {}".format(amount, snack_choice)

        # check

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)
        print("snack choice: ",snack_choice)

        # add snack to list

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)

# show snack orders
print()
if len(snack_order) == 0:
    print("Snack ordered: None")

else:
    print("Snacks Ordered: ")

    for item in snack_order:
        print(item)
