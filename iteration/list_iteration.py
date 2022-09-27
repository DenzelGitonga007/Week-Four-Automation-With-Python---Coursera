# define a list, and a loop parameter/condition
animals, chars = ["monkey", "lion", "zebra", "dolphin"], 0
for animal in animals:
    chars += len(animal) #iterate over each string value, finding it's length as chars
print("Total characters in the list: {}, average length of the strings: {}".format(chars, chars/len(animals)))
