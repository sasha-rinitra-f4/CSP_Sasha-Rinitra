// Sasha Rinitra, Template
#include <stdio.h>


int main(void) {
    char cousins[4][20] = {"Ajash", "Alishya", "Sasha", "Shan"};
    int clength = sizeof(cousins)/ sizeof(cousins[0]);
    int c = 0;
    while(c<clength){
        printf("Hello %s\n", cousins[c]);
        c++;
    }
  return 0;
}