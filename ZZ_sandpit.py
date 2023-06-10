

def string_checker(question, num_letters, valid_responses):
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item
        print(f"Please choose {valid_responses[0]} or {valid_responses[1]}")
    
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
for case in range(0,5):
    want_instructions = string_checker("Do you want to see the instructions (y/n): ", num_letters = 1, valid_responses = yes_no_list)
    print(f"You chose {want_instructions}")
    
for case in range(0,5):
    pay_method = string_checker("How would you like to pay: ", num_letters = 2, valid_responses = payment_list)
    print(f"You chose {pay_method}")
