// Sasha Rinitra, Template
#include <stdio.h>
#include <time.h>

int main(void) {

    time_t now = time(NULL);
    struct tm *tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    if (hour >= 12 && hour <= 16){
        printf("Good Afternoon!");
    }else if(hour > 16 && hour <= 19){
        printf("Good Evening!!");
    }else if(hour > 19){
        printf("Good night!!");
    }else{
        printf("Good morning!!");
    }
  
  return 0;
}