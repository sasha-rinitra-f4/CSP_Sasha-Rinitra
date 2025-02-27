// Sasha Rinitra, Template
#include <stdio.h>
#include <string.h>

int age;

int main(void){
  printf("Welcome! In this program, you will check if you are old enough for certain categories!\n");
  printf("How old are you?\n");
  scanf("%d", &age);


  if(age >= 15){
    printf("You are eligible to go to school, get your permit, drive or vote:(");
  }else if (age >= 17){
    printf("You are eligible to get your learners permit, go to school and drive but you can't vote yet:(");
  }else if (age >= 18){
    printf("You are eligible to get your learners permit, go to school, drive and vote!");
    }else{
    printf("You are not eligible to get your permit, drive, go to school and vote :(");
    }

  return 0;
}