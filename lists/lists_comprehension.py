# appending multiples of a number
multiples = [ x*7 for x in range(0,11)]
num = 7 # the divisor being tested
print("Testing for list comprehension to append multiples of a number ({}): ".format(num) + str(multiples))

# finding the length of the strings in a list
languages = ["Python", "Java", "Php", "HTML"]
lengths = [len(language) for language in languages]
len_in_list_compreh = "Using list comprehension to find the length of strings in a list eg: "
print("{}".format(len_in_list_compreh) + str(lengths))

# Using conditional clause in list comprehension
# To get all the numbers divisible by 3 from 0 to 100
three_multiples = [z for z in range(0,101) if z % 3 == 0]
print(three_multiples)
