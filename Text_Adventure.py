#Sasha Rinitra, Josephine Chiu, Adelle Ponczoch, Malu Estevam: Text Based Adventure in Python- Stranded on

# DAY ONE- Sasha worked on the while loop
# Adelle did the function
# Malu did the conditional
def day1():
    while True:  
        # print statement introduces our program.t
        print("Oh no! You are the sole survivor of a terrible shipwreck and you are stranded on an island. You must make tough choices to go home. You will be given 3 choices for every situation and only 2 of them will be right, if you die, you have to restart that day. Good luck! Hope you survive and get home!")  
        #This creates a variab
        day_one = input("Are you hungry, thirsty, or do you want to find shelter?\n").lower()  
        if day_one == "shelter" or day_one == "find shelter":  
            shelter_choice = input("Do you choose leaves, bark, or a cave?\n").lower()  
            if shelter_choice == "leaves" or shelter_choice == "bark":  
                print("You survived, keep going.\n")
                break  # Ends the loop, player has to restart   
            elif shelter_choice == "cave":  
                print("You got eaten by a bear. Restart.\n")  
            else:  
                print("That is not an option. Choose again. \n")  
        # This is the elif of the c
        elif day_one == "hungry":  
            hungry_choice = input("Do you want berries, nuts, or insects?\n").lower()  
            if hungry_choice == "nuts" or hungry_choice == "insects":  
                print("You survived, keep going.\n")
                break  # Ends the loop, player has to restart   
            elif hungry_choice == "berries":  
                print("The berries were poisonous. Choose again, you died.\n")  
            else:  
                print("That is not an option. Choose again.\n")  
                
        elif day_one == "thirsty":  
            thirsty_choice = input("Do you want to go to a river, lake, or pond?\n").lower()  
            if thirsty_choice == "river" or thirsty_choice == "lake":  
                print("You survived, keep going.\n")
                break  # Ends the loop, player has to restart  
            elif thirsty_choice == "pond":  
                print("That water was nasty. Choose again.\n")  
            else:  
                print("Not an option. Choose again.\n")  
        else:  
            print("That is not an option. Choose again.\n")  
            break  # Ends the loop   
    

# DAY TWO- Sasha worked on the loop
# Josephine did the function
# Malu did the conditional


def day2(): #the function
    while True: #the loop is  for when the user chooses a wrong choice and has to restart   
        day_two = input("It's the next day and you survived the first night. Keep going. Now, do you want to find civilization, gather weapons, or signal for help?\n")
        if day_two == "find civilization":  
            civ_choice = input("Do you choose  hill trail, river trail, or forest trail?\n").lower()  
            if civ_choice == "forest trail" or civ_choice == "hill trail":  
                print("You survived, keep going.\n")
                break  # Ends the loop, player has to restart   
            elif civ_choice == "river trail":  
                print("The water was too deep for you to swim in, the currents killed you. Choose again!\n")  
            else:  
                print("That is not an option. Choose again.\n") 
                 
        elif day_two == "gather weapons":  
            weapon_choice = input("Do you want to collect an axe, net, or spear?\n").lower()  
            if weapon_choice == "axe" or weapon_choice == "net":  
                print("You survived, keep going.\n")
                break  # Ends the loop, player has to restart   
            elif weapon_choice == "spear":  
                print(" You accidentally stabbed yourself, that’s embarrassing. Choose again.\n")  
            else:  
                print("That is not an option.\n") 
                 
        elif day_two == "signal for help":  
            help_choice = input("If you want to signal for help, do you want to, gather leaves to create smoke, run to the beach and scream for help, or build a giant SOS sign with rocks?\n").lower()  
            if help_choice == "gather leaves to create smoke" or help_choice == "build a giant SOS sign with rocks":  
                print("You survived, keep going.\n")
                break  # Ends the loop, player has to restart  
            elif help_choice == "run to the beach and scream for help":  
                print("A unicorn heard you and stabbed you with its horn. Your scream was so ugly. Choose again!\n")  
            else:  
                print("Not an option.\n")  
                
        else:  
            print("That is not an option\n")  
            break  # Ends the loop  

#DAY THREE- Malu wrote the conditional part, Ad and Josephine did the function, Sasha wrote the while loop

def day3():    
    while True:
        day_three = input("There is a tsunami, do you want to climb a tree, go to shelter, or run for your life\n").lower() 
        if day_three == "climb a tree":  
            tree_choice = input("Do you climb an oak, bamboo, or palm tree\n").lower()  
            if tree_choice == "oak" or tree_choice == "palm":  
                print("You survived, on every single level. Help will now come! You win\n")
                break  # Ends the loop, player has to restart   
            elif tree_choice == "bamboo":  
                print("You died. That tree was weaker than you. Choose again, bud.\n")  
            else:  
                print("That is not an option. Choose again.\n")  
                
        elif day_three == "go to shelter":  
            shelters_choice = input("Do you want to go to a cliff over hang, tunnel, or climb a mountain? \n").lower()  
            if shelters_choice == "cliff over hang" or shelters_choice == "mountain":  
                print("You survived, on every single level. Help will now come! Winner winner, chicken dinner.\n")
                break  # Ends the loop, player has to restart   
            elif shelters_choice == "tunnel":  
                print("The berries were poisonous. Choose again, you died.\n")  
            else:  
                print("That is not an option. Choose again.\n")  
                
        elif day_three == "run for your life" or day_three == "run":  
            life_choice = input("Do you run in the opposite direction of the tsunami, into a dense forest, or into the tsunami\n").lower()  
            if life_choice == "opposite direction" or life_choice == "dense forest":  
                print("You survived, on every single level. Help will now come! You win\n")
                break  # Ends the loop, player has to restart  
            elif life_choice == "into the tsunami":  
                print("I don’t know if you have a death wish or are just dumb, but you’re dead. Restrart.\n")  
            else:  
                print("Not an option. Choose again.\n") 
                break 
                
        else:  
            print("That is not an option. Choose again.\n")  
            break  # Ends the loop
            
# calling the functions so that each day can be called in the correct order- called by adelle and josephine
day1()
day2()
day3()