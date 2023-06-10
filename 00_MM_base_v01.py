import pandas
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


def currency(x):
    return "${:.2f}".format(x)


MAX_TICKETS = 5
tickets_sold = 0
all_names = []
all_ticket_costs = []
all_surcharge = []

mini_movie_dict = {
      "Name": all_names,
      "Ticket Price": all_ticket_costs,
      "Surcharge": all_surcharge
}

want_instructions = string_checker("Do you want to read the instructions? ", num_letters=1, valid_responses=["yes", "no"])

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
    
    if pay_method == "cash":
        surcharge = 0
    
    else:
        surcharge = ticket_cost * 0.05
    
    tickets_sold += 1
    
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)
    
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index("Name")
mini_movie_frame["Total"] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] -5
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()
add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)
    
print("---- Ticket Data ----")
print()
print(mini_movie_frame)
print()
print("---- Ticket Cost / Profit ----")
print()
print(f"Total Ticket Sales: ${total:.2f} ")
print(f"Total Profit: ${profit:.2f}")


if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} ticket/s "
          "remaining")
