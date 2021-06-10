lists = [1, 2, -1, 3, -3, 4]
length = int(len(lists))
print(length)

for i in range(0, length):
    for j in range(i+1, length):
        if lists[i] + lists[j] == 0:
            print("{} {} {}".format("The Pair is", lists[i], lists[j]))

#list = [1, 3, 5, 6, -1, -3]
#for i in range [0, 5]:
#	if:
#		list[i] + list[i+1] == 0
#		count ++
#		i++
#	else:
#		i = i + 1



