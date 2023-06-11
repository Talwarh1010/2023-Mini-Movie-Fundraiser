import pandas
import random
from datetime import date


def not_blank(question):
    while True:
        response = input(question)
        if response == "":
            print("Sorry, this can't be blank. Please try again.")
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
    # Calculate ticket price based on age
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


def show_instructions():
    print('''\n
    ***** Instructions *****
    For each ticket, enter...
    - The person's name (can't be blank)
    - Age (between 12 and 120)
    - Payment method (cash/credit)

    When you have entered all the users, press 'xxx' to quit.
    The program will then display the ticket details
    including the cost of each ticket, the total cost,
    and the total profit.

    This information will also be automatically written to
    a text file.
    ***********************''')


MAX_TICKETS = 150
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
    show_instructions()
print()

while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

    age = num_check("Age: ")
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry, you are too young for this movie")
        print()
        continue
    else:
        print("?? That looks like a typo, please try again.")
        print()
        continue

    ticket_cost = round(calc_ticket_price(age), 2)
    pay_method = string_checker("How would you like to pay: ", num_letters=2, valid_responses=["cash", "credit"])

    if pay_method == "cash":
        surcharge = 0
    else:
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame["Total"] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()


winner_name = random.choice(all_names)
win_index = all_names.index (winner_name)
total_won = mini_movie_frame.at [win_index, 'Total']


add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)
    

mini_movie_frame = mini_movie_frame.set_index("Name")


today = date.today()
day = today.strftime("%d")
month= today.strftime("%m")
year = today.strftime("%Y")
heading = "----Mini Movie Fundraiser Ticket data--- ({}/{}/{})" .format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)
print()
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Ticket Sales: ${:.2f}" .format(total)
total_profit = "Total Profit : ${:.2f}".format(profit)

if tickets_sold == MAX_TICKETS:
      sales_status = "\n*** All the tickets have been sold ***"
else:
      sales_status = "\n **** You have sold {} out of {} " \
                        "tickets *****".format(tickets_sold, MAX_TICKETS)
                        
winner_heading = "\n---- Raffle Winner -----"
winner_text = "The winner of the raffle is {}. They have won ${:.2f}. ie: Their ticket is free!".format(winner_name, total_won)
            
            
            
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]
# print output
for item in to_write:
    print(item)
# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
    
text_file.close()
