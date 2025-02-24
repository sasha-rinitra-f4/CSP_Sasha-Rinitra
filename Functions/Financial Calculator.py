# Sasha Rinitra, Update Financial Calculator Python

# Write a print statement telling the user what the program is (Budget Calculator)
print("Welcome to Financial Calculator!")

def user(type):
    return float(input(f"How much is your monthly {type}? \n"))
    
income = user("income")
rent = user("rent")
utilities = user("utilities")
groceries = user("groceries")
transportation = user("transporation")

savings = income*0.1
expenses = rent+utilities+groceries+transportation+savings

def info(income, amount, type):
    percent_type = float(amount/income*100)
    print(f"You spend ${amount:.2f} on {type} and that is {percent_type:.1f}% of your income")

info(income, rent, "rent")
info(income, utilities, "utilities")
info(income, groceries, "groceries")
info(income, transportation, "transportation")
info(income, savings, "savings")

print(f"You saved ${savings:.2f} and that is 10% of your income")