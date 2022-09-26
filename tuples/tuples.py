# Returning data with multiple values with tuples
def average_marks(mean_score):
    cat_1, cat_2, main_exam = mean_score
    return("{:.2f}".format((cat_1 + cat_2 + main_exam)))

# Test
print("Your average score is: ", end = '\n') #spacing between two print statements on one line
print(average_marks((15, 15, 70))) #Have the parameters inside parenthesis to count them as one argument