
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


def calc_ticket_price(var_age):
    if var_age < 16:
        price = 7.5
    elif var_age < 65:
        price = 10.5
    else:
        price = 6.5
    return price


def string_checker(question, num_letters, valid_responses):
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item
        print(f"Please choose {valid_responses[0]} or {valid_responses[1]}")


MAX_TICKETS = 3
tickets_sold = 0
want_instructions = string_checker("Do you want to read the instructions? ", num_letters=0, valid_responses=["yes", "no"])

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
    
    ticket_cost = round(calc_ticket_price(age),2)
    pay_method = string_checker("How would you like to pay: ", num_letters = 2, valid_responses = ["cash", "credit"])
    
    tickets_sold += 1
if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} ticket/s "
          "remaining")
