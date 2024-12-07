input_file = "./input.txt"
similarity_score = 0
left = []
right = []

def find_occurances(seznam, num):
    occurances = 0

    for i in seznam:
        if i == num:
            occurances += 1

    return occurances

with open(input_file, 'r') as file:
    for line in file:
        seznam = [int(a) for a in line.split()]
        left.append(seznam[0])
        right.append(seznam[1])

for i in left:
    similarity_score += i * find_occurances(right, i)

print(similarity_score)