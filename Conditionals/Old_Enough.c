// Sasha Rinitra, Template
#include <stdio.h>
#include <string.h>

int age;

int main(void){
  printf("Welcome! In this program, you will check if you are old enough for certain categories!\n");
  printf("How old are you?\n");
  scanf("%d", &age);


  if(age < 5){
    printf("You are not eligible to go to school, get your permit, drive or vote yet:(");
  }else if (age == 5){
    printf("You aren't eligible to get your learners permit, vote and drive but you can go to school!");
  }else if (age <= 14){
    printf("You aren't eligible to get your learners permit, vote and drive but you can go to school!");
    }else if (age == 15){
    printf("You are  eligible to get your permit, drive, go to school but can't vote yet:(");
    }else if (age == 16){
    printf("You are  eligible to get your permit, drive, go to school but can't vote yet:(");
    }else if (age == 17){
    printf("You are  eligible to get your permit, drive, go to school but can't vote yet:(");
    }else{
      printf("You are eligible to go to school, get your permit, drive and vote!");
    }

  return 0;
}