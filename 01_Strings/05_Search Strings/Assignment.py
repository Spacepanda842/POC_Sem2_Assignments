text = input("Enter some text:")
result = text.find("the")
if result == -1:
    print("The word isn't in the text.")
else:
    print("This text has the word in it.")
    print("The word the is at position", result)

