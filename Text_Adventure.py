#Sasha Rinitra, Josephine Chiu, Adelle Ponczoch, Malu Estevam: Text Based Adventure in Python- Stranded on


# Requirements:
    # A variable
    # 2 Functions → 10 pts, Program has 2 connected functions
    # A loop
    # A conditional → 10 pts, Conditional has at least 3 different outputs

# Malu and Sasha worked on this while loop with conditionals
while True:  
    print("Oh no! You are the sole survivor of a terrible shipwreck and you are stranded on an island. You must make tough choices to go home. You will be given 3 choices for every situation and only 2 of them will be right, if you die, you have to restart. Good luck! Hope you survive and get home!")  
      
    # Get the first choice  
    day_one = input("Are you hungry, thirsty, or do you want to find shelter?\n").lower()  
      
    # DAY ONE  
    if day_one == "shelter":  
        shelter_choice = input("Do you choose leaves, bark, or a cave?\n").lower()  
        if shelter_choice == "leaves" or shelter_choice == "bark":  
            print("You survived, keep going.\n")  
        elif shelter_choice == "cave":  
            print("You got eaten by a bear. Restart.\n")  
            break  # Ends the loop, player has to restart  
        else:  
            print("That is not an option.\n")  
          
    elif day_one == "hungry":  
        hungry_choice = input("Do you want berries, nuts, or insects?\n").lower()  
        if hungry_choice == "nuts" or hungry_choice == "insects":  
            print("You survived, keep going.\n")  
        elif hungry_choice == "berries":  
            print("The berries were poisonous. Restart, you died.\n")  
            break  # Ends the loop, player has to restart  
        else:  
            print("That is not an option.\n")  
  
    elif day_one == "thirsty":  
        thirsty_choice = input("Do you want to go to a river, lake, or pond?\n").lower()  
        if thirsty_choice == "river" or thirsty_choice == "lake":  
            print("You survived, keep going.\n")  
        elif thirsty_choice == "pond":  
            print("That water was nasty. You died, restart.\n")  
            break  # Ends the loop, player has to restart  
        else:  
            print("Not an option.\n")  
    else:  
        print("That is not an option\n")  
        break  # Ends the loop     

# DAY TWO
print("It's the next day and you survived the first night. Keep going. Now, do you want to find civilization, gather weapons, or signal for help?")
day_two = ["find civilization", "gather wapons", "signal for help"]



if day_two == "civilization":
    input("Do you want to take a hill trail, river trail, or forest trail?\n")
elif day_two == "gather weapons":
    input("Do you want an axe, a spear, or a net?\n")
elif day_two == "signal for help":
    input("Do you want to gather leaves to create smoke, run to the beach and scream for help, or build a giant SOS sign with rocks?\n")


# DAY THREE

print("It’s the third day, if you survive today, help will come. A tsunami is coming!")
day_three = ["climb a tree", "go to shelter", "run for your life"]

# Adelle did the following input + parameter function
#def user(day3):
    #return (input(f"Do you want {day3}"))"Do you want "
#print(input("to climb a palm tree, an oak tree, or a bamboo tree?"))

#def user(word):
#    return input(f"Do you want {word}:\n")
#food = user("food")
#water = user("water")
#shelter = user("shelter")


# Josephine did the following function:
#def result(choices):
#    return "You survived! " + choices
#print(result())
#print(result("You chose leaves."))
#print(result(choices))

# Josephine did the following function:
#def input(choices):
#    return "Do you want " + choices + "?"
#print(input("food, water, or shelter"))
#print(input("to find civilization, gather weapons, or signal for help"))
#print(input("to find leaves, bark, or a cave"))
#print(input("to find berries, nuts, or insects"))
#print(input("to go to a river, lake, or pond"))



   
  
