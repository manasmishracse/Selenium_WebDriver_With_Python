String = "Manas"
split = int(input("Enter the split number"))
length = len(String)
new = ""

for i in range(0, split):
    new = new + String[i]

print(new)