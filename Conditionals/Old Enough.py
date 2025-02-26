# Sasha Rinitra, Old Enough Python

print("Welcome! In this program, you will check if you are old enough for certain categories!\n")

age = int(input("How old are you?\n"))

if age >= 18:
    print("You are eligible to vote, get your permit, drive, and go to school!")
elif age >= 16:
    print("You are eligible to get your permit, drive and go to school! But you can't vote yet:(")
elif age >= 15:
    print("You are eligible to get your learners permit and go to school! But you can't drive or vote yet:(")
elif age >= 4:
    print("You are eligible to go to school! But you can't get your permit, drive or vote:(")
else:
    print("Sorry you are sadly not eligible to go to school, get your permit, drive or vote yet:(")