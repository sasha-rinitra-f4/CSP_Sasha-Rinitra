# Sasha Rinitra, Update Financial Calculator Python

# Write a print statement telling the user what the program is (Budget Calculator)
print("Welcome to Financial Calculator!")

def user(type):
    print(input(f"How much is your monthly {type}?"))
    
print(user("income"))
print(user("rent"))
print(user("utilities"))
print(user("groceries"))
print(user("transporation"))

savings = income*0.1
# Calculate spending money, income - (rent+utilities+groceries+transportations+savings) (variable)
expenses = rent+utilities+groceries+transportation+savings

def info(income, amount, type):
    percent_type = amount/income*100
    print(f"You spend ${amount:.2f} on {type} and that is {percent_type:.1f} of your income")

income, rent, utilities, groceries, transportation = float(input(f"What is your monthly {type}"))
info(income, rent, "rent")
info(income, utilities, "utilities")
info(income, groceries, "groceries")
info(income, transportation, "transportation")
info(income, savings, "savings")

