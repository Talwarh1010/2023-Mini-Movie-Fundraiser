import pandas

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
print(f"Total Ticket Sales: ${total} ")
print(f"Total Profit: ${profit}")