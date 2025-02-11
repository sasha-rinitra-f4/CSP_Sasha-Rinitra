// Sasha Rinitra, Strings notes C
#include <stdio.h>
#include <string.h>

char name[20];

int main(void) {
    //printf("Please tell me your full name:\n");
    //scanf("%s", name); doesn't work or full name, only puts first name
    //fgets(name, 20, stdin);
    //printf("Hello %s, Welcome to my program", name);

    //char sentence[] = "The quick brown fox jumps over the lazy dog";
    //printf("%c\n", sentence[16]); // to print just 'f'
    //printf("%lu\n", sizeof(sentence)); //said 44, because it gives indexes
    //printf("%d\n", strien(sentence)); //says 43

    char one[] = "Hello ";
    char two[] = "World!";
    char three[] = "This is my program. ";
    two[5] = '?';
    printf("%s\n", one); //before concatination
    strcat(one, two);
    printf("%s\n", one);  //after concatination
    strcat(three, one);
    printf("%s", three);
  return 0;
}