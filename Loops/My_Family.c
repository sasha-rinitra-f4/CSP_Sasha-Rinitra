// Sasha Rinitra, Template
#include <stdio.h>


int main(void) {
    char movies[4][20] = {"Ajash", "Alishya", "Sasha", "Shan"};
    int mlength = sizeof(movies)/ sizeof(movies[0]);
    int m = 0;
    while(m<mlength){
        printf("Hello %s\n", movies[m]);
        m++;
    }
  return 0;
}