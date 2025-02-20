# Sasha Rinitra, Update Financial Calculator Python

def info(income, amount, type):
    percent_type = amount/income_amount*100
    print(f"You spend ${amount:.2f} on {type} and that is {percent_type:.1f} of your income")


# Write a print statement telling the user what the program is (Budget Calculator)
print("Welcome to Budget Calculator!")
# Ask for monthly input (User input)
income = float(input("What is your monthly income\n"))
# Ask for rent/mortgage amount (User input)
rent = float(input("How much do you pay or your rent ever month?\n"))
# Ask for utilities amount (User input)
utilities = float(input("How much do you spend on utilities every month?\n"))
# Ask for groceries amount (User input)
groceries = float(input("How much do you spend on groceries every month?\n"))
# Ask for transportation amount (User input)
transportation = float(input("How much do you spend on your transportation?\n"))
# Calculate savings as 10% income (variable)
savings = income*0.1
# Calculate spending money, income - (rent+utilities+groceries+transportations+savings) (variable)
expenses = rent+utilities+groceries+transportation+savings

info(income, rent, "rent")




# Tell user category spending amount and percent for rent ("You spend", rent, "on rent and that is", percent_rent, "percent of your income")
print("You spend", (f"{rent:.2f}"), "on rent and that is", (f"{percent_rent:.1f}"), "percent of your income")
# Tell user category spending amount and percent for utilities ("You spend $xx.xx on utilities and that is xx% of your income")
print("You spend", (f"{utilities:.2f}"), "on utilities and that is", (f"{percent_utilities:.1f}"), "percent of your income")
# Tell user category spending amount and percent for groceries ("You spend $xx.xx on groceries and that is xx% of your income")
print("You spend", (f"{groceries_amount:.2f}"), "on groceries and that is", (f"{percent_groceries:.1f}"), "percent of your income")
# Tell user category spending amount and percent for transportation ("You spend $xx.xx on transportaion and that is xx% of your income")
print("You spend", (f"{transportation_amount:.2f}"), "on transportation and that is", (f"{percent_transportation:.1f}"), "percent of your income")
# Tell user category spending amount and percent for spending ("You spend $xx.xx on spending money and that is xx% of your income")
print("You spend", (f"{income_spending:.2f}"), "in total and that is", (f"{percent_spending_income:.1f}"), "percent of your income")
# Tell user category spending amount and percent for savings ("You spend $xx.xx on savings and that is 10% of your income")
print("You save", (f"{savings:.2f}"), "and that is 10 percent of your income")