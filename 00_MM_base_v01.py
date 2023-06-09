def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return response
        elif response == "no" or response == "n":
            return response
        else:
            print("Please enter yes or no")


def not_blank(question):
    while True:
        response = input(question)
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


MAX_TICKETS = 3
tickets_sold = 0
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes" or want_instructions == "y":
    print("Instructions go here")
print()
while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break
    
    age = num_check("Age: ")
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        print()
        continue
    else:
        print("?? That looks like a typo, please try again.")
        print()
        continue
    
    tickets_sold += 1
if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} ticket/s "
          "remaining")
