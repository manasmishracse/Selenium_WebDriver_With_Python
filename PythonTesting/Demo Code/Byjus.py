# In any String Find the Duplicate String and count the Number of Duplicate Strings has Occurred

String = input("Please Enter the String: ")
Freq = ""
Occ = 0

length = int(len(String))
Count = 0

for i in range(0, length):
    if String[i] in Freq:
        i = i+1
    else:
        for j in range(i+1, length):
            if String[i] == String[j]:
                Count = Count + 1
                Occ = Occ + 1
                Freq = Freq + String[j]
            else:
                pass

    if Count > 0:
        print("{} {} {} {}".format("Duplicate String and Count is:", String[i], Count+1, "Respectively"))
    else:
        pass

    Count = 0

if Occ == 0:
    print("THERE IS NO DUPLICATE CHARACTER PRESENT IN PROVIDED STRING!!!")