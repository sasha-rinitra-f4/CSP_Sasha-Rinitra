// Sasha Rinitra, Functions Notes C
#include <stdio.h>
// void add(){
//  }
//int add(void){
    //printf("%d\n", 6+8); 
    //return 6+8;
//}
//parameters
//void add(int num1, int num2){
  // printf("%d\n", num1+num2)
//}
// continued?
char input(char type[20]){
    char answer[50];
    printf("Please give me a %s:\n", type);
    scanf("%s", answer);
    return answer;
}
int main(void) {
  //printf("Hello World\n");
  //add();
  //add(3+5);
  printf("%s was %s until they somehow reached %s". input("name"), input("verb"), input("place"));
  return 0;
}