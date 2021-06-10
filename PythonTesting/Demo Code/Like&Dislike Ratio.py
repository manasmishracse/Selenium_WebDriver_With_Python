# Let User1 has submitted [011001] and User2 has Submitted [101011]. Where 1 is like and 0 as Dislike. Find the Like and DISLIKE Ratio

ratio = 0
User1 = [1, 0, 1, 0, 1]
User2 = [1, 1, 1, 0, 0]

for i in range(0, len(User1)):
    if User1[i] == User2[i]:
        ratio = ratio + 1
print(ratio)

