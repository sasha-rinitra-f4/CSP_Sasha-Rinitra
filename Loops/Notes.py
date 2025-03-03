# Sasha Rinitra, Loops Notes Python

#1. What is a loop? 
    #Loop is a section of code that is going to repeat

#2. What are the two types of loops?
    # -While Loop
x = 0
while x < 10:
    print("Hello", x)
    x += 1

    # -for loop
nums = [1,2,3,4,5,6]
for num in nums:
    print(num)

#3. What is iteration?
    #Iterartion is the act of repeating

#4. What are lists? 
    #List is a bunch of values in the same variable
    siblings = ["Alex", "Katie", "Andrew", "Vienna", "Tori", "Treyson", "Jeff", "Hailey"]
        #print(siblings) #dont print the whole list
    #print js one item from the list
    print(siblings[3])
    #change an item in the list
    siblings[7] = "Jake"
    print(siblings[7])
    #remove an item from the list
    siblings.pop(5)
    print(siblings)
    #proper list printing with a for loop
    for sibling in siblings: #always put plural for variables in lists
        print(sibling)
        print(sibling, "LaRose")
    num = 1
    for sibling in siblings: #always put plural for variables in lists
        print(sibling)
        print(f"{num}. {sibling} LaRose")
        num +=1
    for num in range(1,11, 2):
        print(num)

#5. How do you make lists in python? 
    siblings = ["Alex", "Katie", "Andrew", "Vienna", "Tori", "Treyson", "Jeff", "Hailey"]

#6. How do you make for loops in python? 
    nums = [1,2,3,4,5,6]
for num in nums:
    print(num)
    num +=1

#7. How do you make while loops in python?
num = 1
while num < 21:
    print(num)
    num+=1

#duck duck goose
import random

num = 1
rand = random.randint(1,20)
while num < 21:
    if num == rand:
        print(f"Goose!")
        break #continue  #Tells the loop to be done
    else:
        print("Duck")
        num +=1
#continue tells the loop to stop that iterartion and start again