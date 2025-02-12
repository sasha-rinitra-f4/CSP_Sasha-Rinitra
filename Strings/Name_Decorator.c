// Sasha Rinitra, Name Decorator C
#include <stdio.h>
#include <string.h>

char name[20];

int main(void) {
    printf("Please tell me your name:\n"); 
    scanf("%s", name);
    printf("Welcome to Name Decorator, %s\n", name);

    char dec1[] = "<<<";
    char dec2[]= ">>>";
  
    strcat(dec1, name);
    strcat(dec1, dec2);
    printf("%s\n", dec1);
  return 0;
}