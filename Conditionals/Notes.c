// Sasha Rinitra, Conditionals Notes C
#include <stdio.h>
#include <string.h>
char name[] = "Sasha";
int num = 8;


int main(void) {
  if(strcmp(name, "Sasha")== 0){ // strcmp is to compare strings
    printf("Hello Ms.Rinitra, Welcome to class!\n");
  }else{
    printf("Hello %s, Welcome to class!\n", name);
  }
// && = and
// || = or
// != = not
  if(num > 5 && num < 10){
    //nested conditional
    if (num == 7){
        printf("%d is an unlucky number\n", num)
    }else{
        printf("%d is a large single digit number\n", num);
    }
    
  }else if(num > 10){
    printf("%d is not a single digit number\n", num);
  }else{
    printf("%d is a small single digit number\n", num);
  }
  return 0;
}