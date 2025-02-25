// Sasha Rinitra, Financial Calculator C

#include <stdio.h>

char welcome[] = "Welcome to Budget Calculator!";
float income, rent, utilities, groceries, transportation;


float user(char type[]){
    float amount;
    printf("How much is your %s amount monthly?\n", type);
    scanf("%f", &amount);
    return amount;
}

void info(float income, float amount){
    float percent = (amount/income)*100;
    printf("You spend $%.2f on rent which is %.2f%% your income\n", amount, percent);
}

int main(void){
    printf("%s\n", welcome);
    
    income = user("income");
    rent = user("rent");
    utilities = user("utilities");
    groceries = user("groceries");
    transportation = user("transporation");

    float savings = income/10;
    float expenses = income - (rent+utilities+groceries+transportation+savings);
    float expenses_percent = (expenses/income)*100;

    info(income, rent);
    info(income, utilities);
    info(income, groceries);
    info(income, transportation);
    info(income, savings);
    printf("You have $%.2f for savvings which is 10%% of your income\n", savings);
    printf("You have $%.2f left for spending which is %.2f%% of your income\n", expenses, expenses_percent);

    return 0;
}