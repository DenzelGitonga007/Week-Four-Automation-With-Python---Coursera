# Iterating over a dictionary of courses with the students who have passed
pass_list = {"BIT 314": 14, "BCS 313": 19, "ESM 101": 1}
for courses in pass_list:
    print(courses)

# To iterate over both the keys and their values, use the item function
for extension, amount in pass_list.items():
    print("There are {} values with the .{} extension".format(amount, extension))

# To access just the values
value = pass_list.values()
print(value)
# or
for value in pass_list.values():
    print(value)
#  To access just keys
value_keys = pass_list.keys()
print(value_keys)


