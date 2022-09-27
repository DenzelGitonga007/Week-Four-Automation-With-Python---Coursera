# using the enumerate function to obtain the index of an element and it's value-- a tuple of index, and value
winners = ["Denzel", "Catherine", "Junne", "Francis"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1,person))