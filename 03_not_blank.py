def not_blank(question):
    while True:
        response = input(question)
        if response == "":
            print("Sorry this can't be blank. Please try again")
            print()
        else:
            return response

while True:
    name = not_blank("Enter your name (or 'xxx' to quit): ")
    if name == "xxx":
        break
print("We are done")