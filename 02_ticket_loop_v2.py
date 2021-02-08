# start of loop

# initial loop so that it runs at least once
name = ""
count = 1
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # get details
    name = input("Name: ")
    if name == "xxx":
        print("You have sold {} tickets There are {} places still available".format(count, MAX_TICKETS - count))

    else:
        print("You have {} seats left".format(MAX_TICKETS - count))
    count += 1

