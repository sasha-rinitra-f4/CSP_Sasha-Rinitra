// Sasha Rinitra, Financial Calculator C

#include <stdio.h>

char welcome[] = "Welcome to Budget Calculator!";
float income;
float rent;
float utilities;
float groceries;
float transportation;

float user(float){
    printf("How much is your monthly %f?\n");
    scanf("%f", income);
}



int main(void){

    printf("%s\n", welcome);
    user();

    return 0;
}