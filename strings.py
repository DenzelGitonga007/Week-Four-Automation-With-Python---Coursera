# Replacing the contents of a string by creating a new variable of the same previous variable
message = "A kong string with a silly typo"
print(message)
new_message = message[0:2] + "l" + message[3:]
print("The replaced string reads:")
print(new_message)
