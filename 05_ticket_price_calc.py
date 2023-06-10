def calc_ticket_price(var_age):
    if var_age < 16:
        price = 7.5
    elif var_age < 65:
        price = 10.5
    else:
        price = 6.5
    return price
        
    
while True:
    age = int(input("Age: "))
    ticket_cost = round(calc_ticket_price(age),2)
    print(f"Age: {age}, Ticket Price: ${ticket_cost}")
    