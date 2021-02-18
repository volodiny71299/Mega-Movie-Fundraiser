# work out the ticket price based on age


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


# sets profit to 0 (starting number)
profit = 0

# How much user needs to pay
price = 0

# start of loop
name = ""
while name != "xxx":
    name = input("Name: ")

    # If name is exit code, break out of loop
    if name == "xxx":
        break

    age = num_check("Age: ", 12, 130)

    if age < 16:
        ticket_price = 7.5

    elif age < 65:
        ticket_price = 10.5

    else:
        ticket_price = 6.5

    profit_made = ticket_price - 5
    profit += profit_made

    print("{} : ${:.2f}".format(name, ticket_price))

print("Profit from tickets: ${:.2f}".format(profit))

