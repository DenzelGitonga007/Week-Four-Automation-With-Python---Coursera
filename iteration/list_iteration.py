# define a list, and a loop parameter/condition
animals, chars = ["monkey", "lion", "zebra", "dolphin"], 0
for animal in animals:
    chars += len(animal) #iterate over each string value, finding it's length as chars
print("Total characters in the list: {}, average length of the strings: {}".format(chars, chars/len(animals)))

# using the enumerate function to obtain the index of an element and it's value-- a tuple of index, and value
winners = ["Denzel", "Catherine", "Junne", "Francis"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1,person))