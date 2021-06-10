# Removal of Duplicate String

String = 'Manas'
Str = ''
MStr = ''
length = int(len(String))
print(length)
Count = 0

for i in range(0, length):
    for j in range(i+1, length):
        if String[i] == String[j]:
            Count = Count + 1
            print("{} {} {}".format("The Matching Pair is", String[i], String[j]))
    if Count == 0:
        Str = Str + String[i]
    elif Count >= 1:
        MStr = MStr + String[i]
        Count = 0

print("Non Duplicate String is: " + Str)
print("Duplicate String is: " + MStr)
