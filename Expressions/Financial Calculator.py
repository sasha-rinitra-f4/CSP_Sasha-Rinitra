# Sasha Rinitra, Financial Calculator Python

# Write a print statement telling the user what the program is (Budget Calculator)
print("Welcome to Budget Calculator!")
# Ask for monthly input (User input)
income_amount = float(input("What is your monthly income\n"))
# Ask for rent/mortgage amount (User input)
rent_amount = float(input("How much do you pay or your rent ever month?\n"))
# Ask for utilities amount (User input)
utilities_amount = float(input("How much do you spend on utilities every month?\n"))
# Ask for groceries amount (User input)
groceries_amount = float(input("How much do you spend on groceries every month?\n"))
# Ask for transportation amount (User input)
transportation_amount = float(input("How much do you spend on your transportation?\n"))
# Calculate savings as 10% income (variable)
savings = income_amount*0.1
# Calculate spending money, income - (rent+utilities+groceries+transportations+savings) (variable)
income_spending = rent_amount+utilities_amount+groceries_amount+transportation_amount+savings
# Calculate percent of rent (rent/income[divide])*100 (variable)
percent_rent = (rent_amount/income_amount)*100
# Calculate percent of utilities (utilities/income[divide])*100 (variable)
percent_utilities = (utilities_amount/income_amount)*100
# Calculate percent of groceries (groceries/income[divide])*100 (variable)
percent_groceries = (groceries_amount/income_amount)*100
# Calculate percent of transportation (transportation/income[divide])*100 (variable)
percent_transportation = (transportation_amount/income_amount)*100
# Calculate percent of spending money (spending/income[divide])*100 (variable)
percent_spending_income = (income_spending/income_amount)*100
# Tell user category spending amount and percent for rent ("You spend", rent, "on rent and that is", percent_rent, "percent of your income")
print("You spend", (f"{rent_amount:.2f}"), "on rent and that is", (f"{percent_rent:.1f}"), "percent of your income")
# Tell user category spending amount and percent for utilities ("You spend $xx.xx on utilities and that is xx% of your income")
print("You spend", (f"{utilities_amount:.2f}"), "on utilities and that is", (f"{percent_utilities:.1f}"), "percent of your income")
# Tell user category spending amount and percent for groceries ("You spend $xx.xx on groceries and that is xx% of your income")
print("You spend", (f"{groceries_amount:.2f}"), "on groceries and that is", (f"{percent_groceries:.1f}"), "percent of your income")
# Tell user category spending amount and percent for transportation ("You spend $xx.xx on transportaion and that is xx% of your income")
print("You spend", (f"{transportation_amount:.2f}"), "on transportation and that is", (f"{percent_transportation:.1f}"), "percent of your income")
# Tell user category spending amount and percent for spending ("You spend $xx.xx on spending money and that is xx% of your income")
print("You spend", (f"{income_spending:.2f}"), "in total and that is", (f"{percent_spending_income:.1f}"), "percent of your income")
# Tell user category spending amount and percent for savings ("You spend $xx.xx on savings and that is 10% of your income")
print("You save", (f"{savings:.2f}"), "and that is 10 percent of your income")