#method 1:
number = [5,2,5,2,2]
for x_count in number:
    print('x' * x_count)



#method 2:
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)