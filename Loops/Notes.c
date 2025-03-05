// Sasha Rinitra, Loops Notes C
#include <stdio.h>


int main(void) {

//What is a loop? 
    //Section of code that repeats
//What are the two types of loops?
    //for loops
    int x;
    for(x=0; x<10; x++){
        printf("Hello\n");
    }
    //while loops
    int i = 1;
    while(i<10){
        printf("%d\n", i);
        i++;
    }
//What is iteration?
    //the act of repeating
    //reference on iteration as a specific time through the loop
//What are lists (arrays)? 
    //bunch of values in the same variable
//How do you make lists in C?
    int grades[] = {97, 95, 100, 70, 94, 98, 64};
    // in the brackets we say how long the list is gonna be, if list is set then brackets can be blank
    //Data type is given as whatever is in the list (All list items must be the same data type)
    //List is surrounded by curly brackets {} with commas , between each item
    printf("%d\n", grades[3]); //To print one item we put the index number in the brackets when we print
    grades[2] = 73; //update grades one at a time using the index number
    printf("%d\n", grades[2]);
    //this tells me the number of bytes in my array
        //printf("%lu", sizeof(grades)); 
    //how to get the size of an array
    int length = sizeof(grades)/sizeof(grades[0]);
    printf("%d\n", length);
//How do you make for loops in C? 
    // iterators should be x or i
    int t;
    // in parenthesis 1.starting point, 2.end point/go until point, 3. what we count by (i+=3) if any different numberto skip ykyk
    for(t=0; t<5; t++){
        printf("%d\n", t);
    }
    int l;
    for(l=0; l<length; l++){
        printf("%d\n", grades[l]);
    }
//How do you make while loops in C?
    //use iterator to set start point
    int iterator = 0;
    //while line sets the stop point/ how long it goes
    while(iterator<=100){
        printf("%d\n", iterator);
        //sets what I count by
        iterator+=10;
    }
    int iterator2 = 100;
    while(iterator>=0){
        printf("%d\n", iterator);
        iterator-=10;
    }
    //strings
    char movies[][20] = {"Cinderella", "The Smurf Movie", "Transformers", "Cars", "Up", "1984"};
    int mlength = sizeof(movies)/ sizeof(movies[0]);
    int m = 0;
    while(m<mlength){
        printf("%s\n", movies[m]);
        m++;
    }
  return 0;
}