# Used for dataframes
import pandas
# Used for generating a random winner
import random
# Used to find today's date
from datetime import date

# Function that checks that name is not blank.
def not_blank(question):
    while True:
        response = input(question)
        if response == "":
            print("Sorry, this can't be blank. Please try again.")
        else:
            return response

# Checks if age is an integer and not letters
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer.")

# Cost calculator. 
def calc_ticket_price(var_age):
    # Calculate ticket price based on age
    if var_age < 16:
        price = 7.5
    elif var_age < 65:
        price = 10.5
    else:
        price = 6.5
    return price

# Used for yes no and cash payment method
def string_checker(question, num_letters, valid_responses):
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item
        print(f"Please choose {valid_responses[0]} or {valid_responses[1]}")

# Converts all numbers into currency
def currency(x):
    return "${:.2f}".format(x)

# Displays instructions for user
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
    
    Have fun! ''')



# Maximum tickets allowed
MAX_TICKETS = 150

# Initialise variables. There will change as program continues
tickets_sold = 0
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary that holds all the lists for the framework
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}


# Welcome the user
print("***** WELCOME TO MEGA MOVIE FUNDRAISER *****")
print()
# Asks user if they would like to view the instructions
want_instructions = string_checker("Do you want to read the instructions? ", num_letters=1, valid_responses=["yes", "no"])

# Shows instructions to user if they said "yes" or "y"
if want_instructions == "yes" or want_instructions == "y":
    show_instructions()
print()

# Loop which stops when the maximum number of tickets is reached or when user enters "xxx"
while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

# Asks user for age
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

# Increment the number of tickets sold
tickets_sold += 1

# Add ticket details to empty lists
all_names.append(name)
all_ticket_costs.append(ticket_cost)
all_surcharge.append(surcharge)

# Create a DataFrame to hold the ticket details
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame["Total"] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# Calculate the total sales and profit
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Choose a random winner from the list of names
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Format numerical values as currency
add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Set the index of the DataFrame to the 'Name' column
mini_movie_frame = mini_movie_frame.set_index("Name")

# Get the current date
today = date.today()
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Create the heading for the ticket data
heading = "----Mini Movie Fundraiser Ticket data--- ({}/{}/{})".format(day, month, year)

# Generate the filename for the output text file
filename = "MMF_{}_{}_{}".format(year, month, day)

# Convert the DataFrame to a string representation
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Prepare the headings and summaries for ticket costs, sales, and profit
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Total Profit : ${:.2f}".format(profit)

# Determine the sales status based on the number of tickets sold
if tickets_sold == MAX_TICKETS:
    sales_status = "\n*** All the tickets have been sold ***"
else:
    sales_status = "\n **** You have sold {} out of {} tickets *****".format(tickets_sold, MAX_TICKETS)

# Create the heading and text for the raffle winner
winner_heading = "\n---- Raffle Winner -----"
winner_text = "The winner of the raffle is {}!. They have won ${:.2f}. i.e., Their ticket is free!".format(winner_name, total_won)

# Gather all the output text items in a list
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
