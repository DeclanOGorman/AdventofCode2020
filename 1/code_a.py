with open('./1/input_a.txt', 'r') as f:
    input = [int(line.strip()) for line in f]

# yes, i know theres a more efficient way than O(n^2)
for num1 in input:
    for num2 in input:
        if num1 + num2 == 2020:
            print (f'Part a: {num1}, {num2} = {num1 * num2}') 

for num1 in input:
    for num2 in input:
        for num3 in input:
            if num1 + num2 + num3 == 2020:
                print (f'Part b: {num1}, {num2}, {num3} = {num1 * num2 * num3}') 
