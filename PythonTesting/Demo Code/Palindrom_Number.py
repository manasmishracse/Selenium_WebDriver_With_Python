#String = input("Enter the Number to Check Palindrom")

String = 123454321
temp = String
rev = 0

while String > 0:
    rem = String % 10
    rev = rev * 10 + rem
    String = String//10

if rev == temp:
    print("Number is Palindrom")
else:
    print("Number is not Palindrom")





