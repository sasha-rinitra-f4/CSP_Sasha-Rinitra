// Sasha Rinitra, FizzBuzz C
#include <stdio.h>
int num;
int main(void) {
  for(num=0; num<51; num++){
    if(num % 3){
        printf("Fizz\n");
    }else if(num % 5){
        printf("Buzz\n");
    }else if(num % 3 && num % 5){
        printf("FizzBuzz\n");
    }else{
        printf("%d\n", num);
    }
        
  }
  return 0;
}