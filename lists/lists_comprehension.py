# appending multiples of a number
multiples = [ x*7 for x in range(0,11)]
num = 7
print("Testing for list comprehension to append multiples of a number ({}): ".format(num) + str(multiples))

# finding the length of the strings in a list
languages = ["Python", "Java", "Php", "HTML"]
lengths = [len(language) for language in languages]
len_in_list_compreh = "Using list comprehension to find the length of strings in a list eg: "
print("{}".format(len_in_list_compreh) + str(lengths))