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

age = num_check("How old are you: ", 12, 130)
print("\nYou are {} years old".format(age))
