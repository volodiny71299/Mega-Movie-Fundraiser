# initialise snack lists...

names = ['Rangi', 'Manaia', 'Talia', 'Arihi', 'Fetu']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

snack_menu_dict = {
    'Popcorn': popcorn,
    'Pita Chips': pita_chips,
    'Water': water,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
}

test_data = [
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],
    [[1, 'Water']],
    [[1, 'Popcorn'], [1, 'Orange Juice']],
    [[1, 'Water'], [1, 'Pita Chips'], [3, 'Orange Juice']]
]

count = 0
for client_order in test_data:

    # assume no snacks have been bought
    for item in snack_lists:
        item.append(0)

    # print(snack_lists)

    # get order (hard coded for easy testing)...
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        to_find = (item[1])
        amount = (item[0])
        add_list = snack_menu_dict[to_find]
        add_list[-1] = amount

print(snack_lists)
