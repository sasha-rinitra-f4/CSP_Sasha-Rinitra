# Sasha Rinitra, Functions Notes Python

# Function is an action stored in a key word

def add():
    numOne = int(input("Give me a number:\n"))
    numTwo = int(input("Give me a number:\n"))
    print(numOne+numTwo)

add()

#parameters go in parenthesis separated by commas
number = int(input("Can I get a number:\n"))
def add(numOne, numTwo):
    print(numOne+numTwo)

add(12,20) #arguments are given when the function is called AND must match the number of parameters
add(int(input("Give me a number:\n")), number)



def user(word):
    return input(f"Tell me a {word}:\n")
     

answer1 = user("name")
answer2 = user("verb")
answer3 = user("place")
print(f"{answer1} was {answer2} and somehow got to {answer3}.")