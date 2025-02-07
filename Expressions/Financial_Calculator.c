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

    printf("You spend, %f\n rent_amount);
    return 0;
}