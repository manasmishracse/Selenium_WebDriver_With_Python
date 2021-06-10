# A Running Basic Calculator:

def add():
    a = int(input("Enter Value of a: "))
    b = int(input("Enter value of b: "))
    c = a + b
    print("Summation of above two number is", c)


def subs():
    a = int(input("Enter Value of a: "))
    b = int(input("Enter value of b: "))
    c = a - b
    print("Substation of above two number is", c)


def mul():
    a = int(input("Enter Value of a: "))
    b = int(input("Enter value of b: "))
    c = a * b
    print("Multiplication of above two number is", c)


def div():
    a = int(input("Enter Value of a: "))
    b = int(input("Enter value of b: "))
    if a > b:
        c = a / b
    else:
        c = b / a

    print("Division of above two number is", c)


print("Welcome to Calculator! \n Select Option from below Details: \n 1.Sum \n 2.Subtraction \n 3.Multiplication \n "
      "4.Division \n")
try:
    user_input = int(input(print("Provide Your Input: ")))

    if user_input == 1:
        add()
    elif user_input == 2:
        subs()
    elif user_input == 3:
        mul()
    elif user_input == 4:
        div()
    else:
        print("None Matches!!")

except Exception as Exp:
    print("Encountered a Exception while Providing Input!")
    print("ACTUAL ERROR OCCURRED: " + Exp)

finally:
    print("Program Ends!!")
