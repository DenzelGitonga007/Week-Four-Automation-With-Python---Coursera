#To replace the contents of a list using list comprehension
plural_cars= ["Benzs", "Funcargos", "Mazdas", "Prados"]
# Creating a new list without the "s" in the string contents
singular_cars = [singular_strings.replace("s", "") for singular_strings in plural_cars]
# Call the new list, singular_cars
print(singular_cars)