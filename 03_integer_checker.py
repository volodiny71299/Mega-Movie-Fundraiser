# number checker


def num_check(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                valid = True
                return response
            else:
                print("Please enter a number between {} and {}".format(low, high))

        except ValueError:
            print("Invalid input")

age = num_check("How old are you: ", 12, 130)
print("\nYou are {} years old".format(age))
