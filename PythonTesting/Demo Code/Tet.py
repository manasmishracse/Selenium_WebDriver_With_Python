# In any String Find the Duplicate String and count the Number of Strings it has Occured

String = "apple"
Freq = " "

length = int(len(String))
Count = 0

for i in range(0, length):
    if String[i] in Freq:
        break
    else:
        for j in range(i+1, length):
            if String[i] == String[j]:
                Count = Count + 1
                Freq = Freq + String[j]

    if Count > 0:
        print("{} {} {}".format("String and Count is:", String[i], Count+1))
    else:
        print("There is No Repeated Strings!")

    Count = 0