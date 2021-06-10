# Fibonacci Series till nth Term

term = int(input("Enter the nth term you want the Fibonacci Series: "))

n1 = 0
n2 = 1
count = 0
Sum = 0

if term < 0:
    print("Not a Positive Number, Enter A positive Number")
else:
    print("The Series is : ")
    print(Sum)
    while count < term:
        Sum = n1 + n2
        print(Sum)
        count = count + 1
        n1 = n2
        n2 = Sum
