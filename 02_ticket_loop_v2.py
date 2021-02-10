# start of loop

# initial loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    if MAX_TICKETS - count == 1:
        print("You have 1 seat left".format(MAX_TICKETS - count))

    else:
        print("You have {} seats left".format(MAX_TICKETS - count))
    # get details
    name = input("Name: ")

    print()

    if name == "xxx":
        print("You have sold {} tickets\nThere are {} places still available".format(count, MAX_TICKETS - count))

    count += 1

if count == MAX_TICKETS:
    print("You have sold all the tickets available")
