#Sasha Rinitra, Josephine Chiu, Adelle Ponczoch, Malu Estevam: Text Based Adventure in Python

# Requirements:
    # A variable
    # 2 Functions → 10 pts, Program has 2 connected functions
    # A loop
    # A conditional → 10 pts, Conditional has at least 3 different outputs

print("Oh no! You are the sole survivor of a terrible shipwreck and you are stranded on an island. You must make tough choices to go home. You will be given 3 choices for every situation and only 2 of them will be right, if you die, you have to restart! Good luck! Hope you survive and get home!")

choices = input("Are you hungry, thirsty, or do you want to find shelter?\n")
choices2 = input("Do you want to find civilization, gather weapons, or signal for help?\n")
choices3 = input("Do you choose leaves, bark, or a cave?\n")
choices4 = input("Do you want berries, nuts, or insects?\n")
choices5 = input("Do you want to go to a river, lake or pond?\n")


# Malu did the following conditional
if choices == "shelter":
    input("Do you choose leaves, bark, or a cave?\n")
    if choices3 == "leaves":
        print("You survived, keep going\n")
    elif choices3 == "bark":
        print("You survived, keep going\n")
    elif choices3 == "cave":
        print("You got eaten by a bear, restart\n")
    else:
        ("That is not an option\n")
        
elif choices == "hungry":
    input("Do you want berries, nuts, or insects?\n")
    if choices4 == "berries":
        print("The berries were poisonous. Restart, you died\n")
    elif choices4 == "nuts":
        print("You survived, keep going\n")
    elif choices4 == "insects":
        print("That was gross, but you survived. Keep going.\n")

elif choices == "thirsty":
    input("Do you want to go to a river, lake, or pond?\n")
    if choices5 == "river":
        print("You survived, keep going\n")
    
else:
    print("That is not an option.\n")
    
# Josephine did the following function:
def result(choices):
    return "You survived " + choices
    print(f"You survived. Good choice.")
result(f"You chose leaves.")
result(choices)



if choices7 == "civilization":
    input("Do you want to take a hill trail, river trail, or forest trail?\n")
elif choices7 == "gather weapons":
    input("Do you want an axe, a spear, or a net?\n")
elif choices7 == "signal for help":
    input("Do you want to gather leaves to create smoke, run to the beach and scream for help, or build a giant SOS sign with rocks?\n")

# Adelle did the following input + parameter function
say1 = "You survived!"
say2 = "You died. Restart."
def choice2(say1, say2):
    if choice2 == "find civilization":
        print
    print(f"{say1}")
    print(f"{say2}")

# Sasha did the following loop
for choice in choices:
    print(choice)
