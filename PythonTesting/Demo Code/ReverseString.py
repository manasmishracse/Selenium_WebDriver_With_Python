# Taking User Input For Reversing the String

Str = input("Enter the String You want to reverse!")
rev = ""

for i in Str:
    rev = i + rev

print("Your Reversed String is " + rev)
