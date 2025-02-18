// Sasha Rinitra, Silly Sentences C
#include <stdio.h>
// String variables for my user inputs (minimum of 3)
char name[20];
char color[20];
char fruit[20];
char cartoon_character[20];
char place[20];

int main(void) {
    // introduce user to program... tell them what is hapening (print statement)
    printf("Hello user, Please tell me your name:\n"); 
    scanf("%s", name);
    printf("Welcome to Silly Sentences, %s\n", name);
    printf("Please answer the folowing questions:) Have Fun!\n");
    // create user inputs (print statements with questions AND scanf to collect the info)(same as the number of variales)
    printf("What is your favorie color?\n");
    scanf("%s", color);

    printf("What is your favorite fruit?\n");
    scanf("%s", fruit);
    
    printf("Who is your favorite cartoon character?\n");
    scanf("%s", cartoon_character);

    printf("What is your favorite place to go to during vacations and etc?\n");
    scanf("%s", place);
    // insert variables into the sentence to show the user (only one print statement) example: "Hello %s", name
    printf("Here is your sentence:\n");
    printf("%s was eating a %s colored %s in %s", cartoon_character, color, fruit, place);

  return 0;
}