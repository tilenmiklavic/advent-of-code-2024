input_file = "./input2.txt"
sum_if_true = 0

def check_num(seznam, index, acc):
    if index + 1 >= len(seznam):
        return (acc + seznam[index] == seznam[0] or 
                acc * seznam[index] == seznam[0] or 
                int(str(acc) + str(seznam[index])) == seznam[0])
    else:
        return (check_num(seznam, index + 1, acc + seznam[index]) or 
                check_num(seznam, index + 1, acc * seznam[index]) or 
                check_num(seznam, index + 1, int(str(acc) + str(seznam[index]))))

with open(input_file, 'r') as file:
    # Read each line in the file
    for line in file:
        seznam = [int(a.replace(':', '')) for a in line.split()]

        if check_num(seznam, 2, seznam[1]):
            sum_if_true += seznam[0]

print(sum_if_true)