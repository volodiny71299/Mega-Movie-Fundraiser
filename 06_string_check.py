# Valid snack holds list of all snacks
# Each item in valid snacks is a list with valid options for each snack <full name, letter code (a - e)
# and possible abbreviations eto>

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
]

# initialise variable
snack_ok = ""
snack = ""

# loop three times to make testing quicker
for item in range(0, 3):

    # ask user for desired snack and put it in lowercase
    desired_snack = input("Snack: ".lower())

    for var_list in valid_snacks:

        # if the snack is in one