import pandas
import random
from datetime import date

def currency(x):
    return "${:.2f}".format(x)


all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0,0,0.53,0.53, 0]

mini_movie_dict = {
      "Name": all_names,
      "Ticket Price": all_ticket_costs,
      "Surcharge": surcharge
}
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame["Total"] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] -5

winner_name = random.choice(all_names)
win_index = all_names.index (winner_name)
total_won = mini_movie_frame.at [win_index, 'Total']
mini_movie_frame = mini_movie_frame.set_index("Name")
today = date.today()
day = today.strftime("%d")
month= today.strftime("%m")
year = today.strftime("%Y")
heading = "----Mini Movie Fundraiser Ticket data ({}/{}/{})" .format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()
add_dollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Ticket Sales: ${}" .format(total)
total_profit = "Total Profit : ${}".format(profit)
sales_status = "\n*** All the tickets have been sold ***"
winner_heading = "\n---- Raffle Winner -----"
winner_text = "The winner of the raffle is {}. \
            They have won ${}. ie: Their ticket is \
            free!".format(winner_name, total_won)
            
            
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]
# print output
for item in to_write:
    print(item)
#write output to file
#create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
    
text_file.close()
