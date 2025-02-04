#include <stdio.h>

char name[12];

int main(void) {
  printf("Welcome to the Fruit World! Whats your name?");
  scanf("%s\n", name);
  printf("%s\n", name);
  printf("WELCOME!!!!");

  return 0;
}