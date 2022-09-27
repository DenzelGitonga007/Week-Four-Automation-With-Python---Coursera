# define a function to take in the name  and email addresses
def full_emails(person):
    # A list to hold the email and the name
    result = []
    # Append the name and email, onto a tuple
    for name, email in person:
        result.append("{} <{}>".format(name, email))
    return result

# Testing to see if it works
print(full_emails([("gitongadenzel@gmail.com", "Denzel Gitonga"), ("catherinemarigu@gmail.com", "Catherine Marigu")]))