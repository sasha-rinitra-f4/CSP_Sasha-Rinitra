#Sasha Rinitra, Strings Notes

# Strings are words in programming, specifically data types "" ''

print("Hello WRLD")
print('Hello WRLD')

# it will show error if ==> print('Hello to Sasha's World')

# People are stupid
name = input("What is your name?\n").strip().lower()
name = input("What is your name?\n").strip().upper()
name = input("What is your name?\n").strip().capitalize()

print(f"Hello {name}, Welcome to my Program!")

# Stupid proofing
name = input("What is your (first) name?\n").strip().capitalize()
print(f"Hello {name}, Welcome to my Program!")

# Syntax Error: error in te structure or punctuation
# Logic Error: sometimes 8+2 = 82
# In python, input is a string
name = input("Give me a number\n").strip().capitalize()
print(name + "2") #this doesn't work

# Concantination is when 2 strings are put together with a + symbol
# Debugging is finding errors in the system and fixing it
# Bug is a error in the system

name = input("Give me a number\n").strip().capitalize()
num = 5*2+name
print(num)
print(name + "2") #type error

# index number

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.find("fox"))

word = sentence.find("fox")

