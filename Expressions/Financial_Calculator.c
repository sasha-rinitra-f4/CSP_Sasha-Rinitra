// Sasha Rinitra, Financial Calculator C

#include <stdio.h>

char welcome[] = "Welcome to Budget Calculator!";
float income_amount;
float rent_amount;
float utilities_amount;
float groceries_amount;
float transportation_amount;

float percent_rent;
float percent_utilities;
float percent_groceries;
float percent_transportation;
float percent_spending_income;
float percent_savings;

int main(void){

    printf("%s\n", welcome);

    printf("What is your monthly income?\n");
    scanf("%d", &income_amount);

    printf("How much do you pay for rent every month?\n");
    scanf("%d", &rent_amount);

    printf("How much do you spend for utilities every month?\n");
    scanf("%d", &utilities_amount);

    printf("How much do you spend on groceries every month?\n");
    scanf("%d", &groceries_amount);

    printf("How much do you spend on transportation every month?\n");
    scanf("%d", &transportation_amount);

    float savings = income_amount*0.1;
    float income_spending = rent_amount+utilities_amount+groceries_amount+transportation_amount+savings;

    float percent_rent = (rent_amount/income_amount)*100;
    float percent_utilities = (utilities_amount/income_amount)*100;
    float percent_groceries = (groceries_amount/income_amount)*100;
    float percent_transportation = (transportation_amount/income_amount)*100;
    float percent_spending_income = (income_spending/income_amount)*100;
    float percent_savings = (savings/income_amount)*100;

    printf("The amount of money you spend on rent is %.2f%% of your income\n", percent_rent);
    printf("The amount of money you spend on utilities is %.2f%% of your income\n", percent_utilities);
    printf("The amount of money you spend on groceries is %.2f%% of your income\n", percent_groceries);
    printf("The amount of money you spend on transportation is %.2f%% of your income\n", percent_transportation);
    printf("Your total amount of money spent is %.2f%% of your income\n", percent_spending_income);
    printf("You save %.1f%% of your income\n", percent_savings);
    
    return 0;
}