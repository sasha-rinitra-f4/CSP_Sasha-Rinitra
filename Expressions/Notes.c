// Sasha Rinitra, Expression Notes C
#include <stdio.h> 
#include <math.h> //is what lets us do exponents
// integers in when we set the variables and 5d when we print
// floats float when we set the variables and 5f when we print
// strings (words) have char (character) when we set the variabl and %s when we print
int mynum;
float percent;
int add = 4+6;
int sub = 4-6;
int mul = 4*6;
float div = 4/6;
int mod = 6%4;
float ex = pow(5, 2); //exponent for c

int main(void){
    //printf("Type a number: \n");
    //scanf("%d", &mynum);
    //printf("You inputed %d\n", mynum);
    //printf("give me a percent as a decimal: \n");
    //scanf("%f", &percent);
    //printf("Your percent is %f\n", percent);

    printf("%d\n", add);
    printf("%d\n", sub);
    mul = 7*4; //resettin the variable and has t happen inside the main
    printf("%d\n", mul);
    printf("%.2f\n", div);


    printf("%d\n", mod);
    printf("%f\n", ex);


    return 0;
}