input_file = "./input.txt"
sum_distance = 0
left = []
right = []

def find_smallest(seznam):
    smallest = seznam[0]

    for i in seznam:
        smallest = min(smallest, i)
    
    return smallest

def remove_smallest(seznam):
    seznam.remove(find_smallest(seznam))

with open(input_file, 'r') as file:
    for line in file:
        seznam = [int(a) for a in line.split()]
        left.append(seznam[0])
        right.append(seznam[1])

while (len(left) > 0 and len(right) > 0): 
    sum_distance += abs(find_smallest(left) - find_smallest(right))
    remove_smallest(left)
    remove_smallest(right)

print(sum_distance)