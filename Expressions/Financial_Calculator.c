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
    scanf("%f", &income_amount);

    printf("How much do you pay for rent every month?\n");
    scanf("%f", &rent_amount);

    printf("How much do you spend for utilities every month?\n");
    scanf("%f", &utilities_amount);

    printf("How much do you spend on groceries every month?\n");
    scanf("%f", &groceries_amount);

    printf("How much do you spend on transportation every month?\n");
    scanf("%f", &transportation_amount);

    float savings = income_amount*0.1;
    float income_spending = rent_amount+utilities_amount+groceries_amount+transportation_amount+savings;

    float percent_rent = (rent_amount/income_amount)*100;
    float percent_utilities = (utilities_amount/income_amount)*100;
    float percent_groceries = (groceries_amount/income_amount)*100;
    float percent_transportation = (transportation_amount/income_amount)*100;
    float percent_spending_income = (income_spending/income_amount)*100;
    float percent_savings = (savings/income_amount)*100;

    printf("The amount of money you spend on rent is $%.2f and that is %.2f%% of your income\n", rent_amount, percent_rent);
    printf("The amount of money you spend on utilities is $%.2f and that is %.2f%% of your income\n", utilities_amount, percent_utilities);
    printf("The amount of money you spend on groceries is $%.2f and that is %.2f%% of your income\n", groceries_amount, percent_groceries);
    printf("The amount of money you spend on transportation is $%.2f and that is %.2f%% of your income\n", transportation_amount, percent_transportation);
    printf("The amount of money you spend on a total of $%.2f and that is %.2f%% of your income\n", income_spending, percent_spending_income);
    printf("You save $%.2f which is %.1f%% of your income\n", savings, percent_savings);
    
    return 0;
}