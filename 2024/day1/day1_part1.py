list_1 = []
list_2 = []
total_difference = 0

with open('day1.txt', 'r') as file:
    for line in file:
        list_1.append(line.strip().split()[0])
        list_2.append(line.strip().split()[1])

for x in range(len(list_1)):
    list_1_min = int(min(list_1))
    list_2_min = int(min(list_2))
    difference = abs(list_1_min - list_2_min)
    total_difference += difference
    list_1.remove(min(list_1))
    list_2.remove(min(list_2))

print(total_difference)

