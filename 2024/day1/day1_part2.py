list_1 = []
list_2 = []
similarity_score = 0

with open('day1.txt', 'r') as file:
    for line in file:
        list_1.append(line.strip().split()[0])
        list_2.append(line.strip().split()[1])

for x in list_1:
    num_occurence = list_2.count(x)
    multiply = int(x) * int(num_occurence)
    similarity_score += multiply

print(similarity_score)
