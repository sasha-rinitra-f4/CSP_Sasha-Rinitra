#Sasha Rinitra, FizzBuzz Python
num = 0
for num in range(1,51):
    if num % 3 and num % 5:
        print("FizzBuzz")
    elif num % 3:
        print("Fizz")
    elif num % 5:
        print("Buzz")
    else:
        print(num)